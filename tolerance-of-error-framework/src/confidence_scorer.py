"""
Confidence Scorer - Computes confidence scores for inferred reasoning outputs.
"""

from dataclasses import dataclass
from typing import Any, Dict, Optional
import re


@dataclass
class ConfidenceComponents:
    """Individual components that contribute to the confidence score."""
    self_reported: float
    historical_accuracy: float
    output_coherence: float
    context_alignment: float
    uncertainty_signals: float
    
    def to_dict(self) -> Dict[str, float]:
        return {
            "self_reported": self.self_reported,
            "historical_accuracy": self.historical_accuracy,
            "output_coherence": self.output_coherence,
            "context_alignment": self.context_alignment,
            "uncertainty_signals": self.uncertainty_signals
        }


class ConfidenceScorer:
    """
    Computes confidence score for inferred reasoning outputs.
    
    Uses an ensemble of heuristics and learned models to estimate
    how likely the inferred output is to be correct.
    """
    
    # Default weights for ensemble scoring
    DEFAULT_WEIGHTS = {
        "self_reported": 0.30,
        "historical_accuracy": 0.25,
        "output_coherence": 0.20,
        "context_alignment": 0.15,
        "uncertainty_signals": 0.10
    }
    
    # Patterns that indicate uncertainty in model output
    UNCERTAINTY_PATTERNS = [
        r"\b(might|maybe|perhaps|possibly|could be|seems like|i think|i believe)\b",
        r"\b(approximately|roughly|around|about)\b",
        r"\b(i'm not sure|uncertain|unclear)\b",
        r"\b(may|might|could)\s+(vary|differ|change)\b",
        r"\?\s*$",  # Ends with question mark
    ]
    
    # Patterns that indicate high confidence
    CONFIDENCE_PATTERNS = [
        r"\b(definitely|certainly|clearly|obviously|exactly|precisely)\b",
        r"\b(the output is|the result is|the answer is)\b",
        r"\b(without doubt|undoubtedly|absolutely)\b",
    ]
    
    def __init__(self, model_weights: Dict[str, float] = None,
                 historical_accuracy_db: dict = None):
        self.weights = model_weights or self.DEFAULT_WEIGHTS.copy()
        self.historical_accuracy = historical_accuracy_db or {}
        
        # Normalize weights
        total = sum(self.weights.values())
        self.weights = {k: v/total for k, v in self.weights.items()}
    
    def score(self, skill_name: str, operation: str,
              inferred_output: Any, context: dict = None) -> float:
        """
        Compute confidence score for an inferred output.
        
        Args:
            skill_name: Name of the skill
            operation: Operation being performed
            inferred_output: The inferred/estimated output
            context: Additional context from the inference process
            
        Returns:
            Confidence score in [0, 1]
        """
        context = context or {}
        
        components = ConfidenceComponents(
            self_reported=self._get_self_reported_confidence(context),
            historical_accuracy=self._get_historical_accuracy(skill_name, operation),
            output_coherence=self._check_output_coherence(inferred_output),
            context_alignment=self._check_context_alignment(context, inferred_output),
            uncertainty_signals=self._detect_uncertainty_signals(inferred_output, context)
        )
        
        return self._weighted_ensemble(components)
    
    def get_components(self, skill_name: str, operation: str,
                       inferred_output: Any, context: dict = None) -> ConfidenceComponents:
        """
        Get individual confidence components for transparency.
        
        Returns the breakdown of how each factor contributed to the score.
        """
        context = context or {}
        
        return ConfidenceComponents(
            self_reported=self._get_self_reported_confidence(context),
            historical_accuracy=self._get_historical_accuracy(skill_name, operation),
            output_coherence=self._check_output_coherence(inferred_output),
            context_alignment=self._check_context_alignment(context, inferred_output),
            uncertainty_signals=self._detect_uncertainty_signals(inferred_output, context)
        )
    
    def _get_self_reported_confidence(self, context: dict) -> float:
        """
        Extract self-reported confidence from context.
        
        Many LLMs can report their own confidence when asked.
        """
        if not context:
            return 0.5
        
        # Check for explicit confidence in context
        if "confidence" in context:
            return float(context["confidence"])
        
        if "self_reported_confidence" in context:
            return float(context["self_reported_confidence"])
        
        # Check for confidence indicators in reasoning
        if "reasoning" in context:
            reasoning = context["reasoning"].lower()
            
            # Look for confidence statements
            for pattern in self.CONFIDENCE_PATTERNS:
                if re.search(pattern, reasoning, re.IGNORECASE):
                    return 0.85
            
            for pattern in self.UNCERTAINTY_PATTERNS:
                if re.search(pattern, reasoning, re.IGNORECASE):
                    return 0.45
        
        # Default moderate confidence
        return 0.5
    
    def _get_historical_accuracy(self, skill_name: str, operation: str) -> float:
        """
        Get historical accuracy for this skill/operation combination.
        
        Uses past execution data to estimate likely accuracy.
        """
        key = f"{skill_name}:{operation}"
        
        if key in self.historical_accuracy:
            return self.historical_accuracy[key]
        
        # Skill-level fallback
        if skill_name in self.historical_accuracy:
            return self.historical_accuracy[skill_name]
        
        # Default based on operation type
        operation_defaults = {
            "extract": 0.75,
            "generate": 0.60,
            "transform": 0.70,
            "analyze": 0.65,
            "calculate": 0.80,
            "search": 0.70,
            "read": 0.85,
            "write": 0.60,
        }
        
        for op_type, default in operation_defaults.items():
            if op_type in operation.lower():
                return default
        
        return 0.65  # Moderate default
    
    def _check_output_coherence(self, inferred_output: Any) -> float:
        """
        Check if the output is coherent and well-formed.
        
        Incoherent outputs suggest lower confidence.
        """
        if inferred_output is None:
            return 0.0
        
        output_str = str(inferred_output)
        
        # Empty output
        if not output_str.strip():
            return 0.0
        
        # Very short output (might be incomplete)
        if len(output_str) < 10:
            return 0.5
        
        # Check for error indicators
        error_indicators = ["error", "exception", "failed", "unable", "cannot"]
        output_lower = output_str.lower()
        error_count = sum(1 for e in error_indicators if e in output_lower)
        if error_count > 0:
            return max(0.3, 0.7 - (error_count * 0.1))
        
        # Check for structure in expected formats
        score = 0.7
        
        # JSON-like structure
        if output_str.strip().startswith("{") and output_str.strip().endswith("}"):
            try:
                import json
                json.loads(output_str)
                score = max(score, 0.85)
            except:
                pass
        
        # List-like structure
        if output_str.strip().startswith("[") and output_str.strip().endswith("]"):
            score = max(score, 0.80)
        
        # Code-like structure
        if any(kw in output_str for kw in ["def ", "class ", "function ", "import "]):
            score = max(score, 0.75)
        
        # Well-formed sentences
        sentences = re.split(r'[.!?]+', output_str)
        if len(sentences) > 1 and all(len(s.strip()) > 10 for s in sentences[:3]):
            score = max(score, 0.75)
        
        return min(score, 1.0)
    
    def _check_context_alignment(self, context: dict, inferred_output: Any) -> float:
        """
        Check if the output aligns with the request context.
        
        Outputs that don't match what was requested have lower confidence.
        """
        if not context:
            return 0.6  # No context to check against
        
        score = 0.7
        
        # Check if output type matches expected type
        if "expected_type" in context:
            expected = context["expected_type"]
            actual = type(inferred_output).__name__
            
            if expected.lower() in actual.lower() or actual.lower() in expected.lower():
                score = 0.85
            else:
                score = 0.50
        
        # Check if output format matches expected format
        if "expected_format" in context:
            expected_format = context["expected_format"].lower()
            output_str = str(inferred_output).lower()
            
            format_checks = {
                "json": lambda s: s.strip().startswith("{"),
                "list": lambda s: s.strip().startswith("["),
                "number": lambda s: s.replace(".", "").replace("-", "").isdigit(),
                "boolean": lambda s: s.lower() in ["true", "false", "yes", "no"],
                "url": lambda s: s.startswith("http"),
                "email": lambda s: "@" in s and "." in s.split("@")[-1],
            }
            
            if expected_format in format_checks:
                if format_checks[expected_format](output_str):
                    score = 0.90
                else:
                    score = 0.45
        
        return score
    
    def _detect_uncertainty_signals(self, inferred_output: Any, context: dict) -> float:
        """
        Detect signals of uncertainty in the output.
        
        Higher score = less uncertainty detected.
        """
        output_str = str(inferred_output).lower()
        
        # Count uncertainty patterns
        uncertainty_count = 0
        for pattern in self.UNCERTAINTY_PATTERNS:
            matches = re.findall(pattern, output_str, re.IGNORECASE)
            uncertainty_count += len(matches)
        
        # Count confidence patterns
        confidence_count = 0
        for pattern in self.CONFIDENCE_PATTERNS:
            matches = re.findall(pattern, output_str, re.IGNORECASE)
            confidence_count += len(matches)
        
        # Calculate uncertainty score
        # More uncertainty patterns -> lower score
        # More confidence patterns -> higher score
        base_score = 0.7
        uncertainty_penalty = min(uncertainty_count * 0.1, 0.4)
        confidence_bonus = min(confidence_count * 0.05, 0.2)
        
        final_score = base_score - uncertainty_penalty + confidence_bonus
        
        return max(0.3, min(final_score, 1.0))
    
    def _weighted_ensemble(self, components: ConfidenceComponents) -> float:
        """
        Combine confidence components using weighted ensemble.
        """
        weighted_sum = (
            components.self_reported * self.weights["self_reported"] +
            components.historical_accuracy * self.weights["historical_accuracy"] +
            components.output_coherence * self.weights["output_coherence"] +
            components.context_alignment * self.weights["context_alignment"] +
            components.uncertainty_signals * self.weights["uncertainty_signals"]
        )
        
        return round(weighted_sum, 4)
    
    def update_historical_accuracy(self, skill_name: str, operation: str, 
                                   accuracy: float):
        """Update historical accuracy for a skill/operation."""
        key = f"{skill_name}:{operation}"
        self.historical_accuracy[key] = accuracy
        
        # Update skill-level average
        skill_keys = [k for k in self.historical_accuracy if k.startswith(f"{skill_name}:")]
        if skill_keys:
            self.historical_accuracy[skill_name] = sum(
                self.historical_accuracy[k] for k in skill_keys
            ) / len(skill_keys)
