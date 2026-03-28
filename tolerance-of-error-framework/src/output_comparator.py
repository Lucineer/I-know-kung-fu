"""
Output Comparator - Compares inferred output to actual output.
"""

from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Union
from abc import ABC, abstractmethod
import re
import json
from difflib import SequenceMatcher

from .tolerance_evaluator import ToleranceLevel


@dataclass
class ComparisonResult:
    """Result of comparing inferred to actual output."""
    similarity: float
    is_within_tolerance: bool
    tolerance_level: ToleranceLevel
    details: Dict[str, Any]
    
    @property
    def error(self) -> float:
        """Return error as 1 - similarity."""
        return 1.0 - self.similarity


class BaseComparator(ABC):
    """Base class for output comparators."""
    
    @abstractmethod
    def compare(self, inferred: Any, actual: Any) -> float:
        """
        Compare inferred to actual output.
        
        Returns similarity score in [0, 1].
        """
        pass


class ExactComparator(BaseComparator):
    """
    Exact comparison - byte-level equality.
    
    Used for tolerance level: EXACT (ε < 0.001)
    """
    
    def compare(self, inferred: Any, actual: Any) -> float:
        """Compare using exact equality."""
        if inferred is None and actual is None:
            return 1.0
        
        if inferred is None or actual is None:
            return 0.0
        
        # Direct equality
        if inferred == actual:
            return 1.0
        
        # String representation equality
        if str(inferred) == str(actual):
            return 1.0
        
        return 0.0


class StructuralComparator(BaseComparator):
    """
    Structural comparison - schema compliance and field matching.
    
    Used for tolerance level: CLOSE (ε < 0.05)
    """
    
    def compare(self, inferred: Any, actual: Any) -> float:
        """Compare using structural similarity."""
        if inferred is None and actual is None:
            return 1.0
        
        if inferred is None or actual is None:
            return 0.0
        
        # Type check
        if type(inferred) != type(actual):
            # Allow int/float comparison
            if not (isinstance(inferred, (int, float)) and isinstance(actual, (int, float))):
                return 0.0
        
        # Dictionary comparison
        if isinstance(inferred, dict) and isinstance(actual, dict):
            return self._compare_dicts(inferred, actual)
        
        # List comparison
        if isinstance(inferred, list) and isinstance(actual, list):
            return self._compare_lists(inferred, actual)
        
        # String comparison
        if isinstance(inferred, str) and isinstance(actual, str):
            return self._compare_strings(inferred, actual)
        
        # Number comparison
        if isinstance(inferred, (int, float)) and isinstance(actual, (int, float)):
            return self._compare_numbers(inferred, actual)
        
        # Fallback to exact comparison
        return ExactComparator().compare(inferred, actual)
    
    def _compare_dicts(self, inferred: dict, actual: dict) -> float:
        """Compare dictionaries by key presence and value similarity."""
        if not inferred and not actual:
            return 1.0
        
        if not inferred or not actual:
            return 0.0
        
        all_keys = set(inferred.keys()) | set(actual.keys())
        if not all_keys:
            return 1.0
        
        scores = []
        for key in all_keys:
            if key not in inferred:
                # Missing key in inferred
                scores.append(0.0)
            elif key not in actual:
                # Extra key in inferred
                scores.append(0.5)
            else:
                # Both have key, compare values
                value_sim = self.compare(inferred[key], actual[key])
                scores.append(value_sim)
        
        return sum(scores) / len(scores)
    
    def _compare_lists(self, inferred: list, actual: list) -> float:
        """Compare lists by length and element similarity."""
        if not inferred and not actual:
            return 1.0
        
        if not inferred or not actual:
            return 0.0
        
        # Length penalty
        len_diff = abs(len(inferred) - len(actual))
        max_len = max(len(inferred), len(actual))
        length_score = 1.0 - (len_diff / max_len)
        
        # Element comparison (best matching)
        if len(inferred) <= len(actual):
            shorter, longer = inferred, actual
        else:
            longer, shorter = actual, inferred
        
        element_scores = []
        for item in shorter:
            # Find best match in longer list
            best_match = max(
                (self.compare(item, other) for other in longer),
                default=0.0
            )
            element_scores.append(best_match)
        
        element_score = sum(element_scores) / len(element_scores) if element_scores else 1.0
        
        # Combine length and element scores
        return (length_score + element_score) / 2
    
    def _compare_strings(self, inferred: str, actual: str) -> float:
        """Compare strings using sequence matching."""
        if inferred == actual:
            return 1.0
        
        # Normalize whitespace
        inferred_norm = ' '.join(inferred.split())
        actual_norm = ' '.join(actual.split())
        
        if inferred_norm == actual_norm:
            return 0.95  # Slight penalty for whitespace differences
        
        # Sequence matcher for similarity
        return SequenceMatcher(None, inferred_norm, actual_norm).ratio()
    
    def _compare_numbers(self, inferred: Union[int, float], 
                         actual: Union[int, float]) -> float:
        """Compare numbers with relative error tolerance."""
        if inferred == actual:
            return 1.0
        
        if actual == 0:
            return 0.0 if inferred != 0 else 1.0
        
        relative_error = abs(inferred - actual) / abs(actual)
        
        # Map error to similarity score
        if relative_error < 0.001:
            return 1.0
        elif relative_error < 0.01:
            return 0.95
        elif relative_error < 0.05:
            return 0.85
        elif relative_error < 0.10:
            return 0.70
        else:
            return max(0.0, 1.0 - relative_error)


class SemanticComparator(BaseComparator):
    """
    Semantic comparison - embedding-based similarity.
    
    Used for tolerance level: APPROXIMATE (ε < 0.20)
    """
    
    def __init__(self, embedding_model=None):
        """
        Initialize with optional embedding model.
        
        Without an embedding model, falls back to text similarity.
        """
        self.embedding_model = embedding_model
        self.structural = StructuralComparator()
    
    def compare(self, inferred: Any, actual: Any) -> float:
        """Compare using semantic similarity."""
        if inferred is None and actual is None:
            return 1.0
        
        if inferred is None or actual is None:
            return 0.0
        
        # Convert to strings for comparison
        inferred_str = self._to_comparable_string(inferred)
        actual_str = self._to_comparable_string(actual)
        
        # Try embedding-based comparison if available
        if self.embedding_model is not None:
            try:
                return self._embedding_similarity(inferred_str, actual_str)
            except Exception:
                pass
        
        # Fallback to enhanced text similarity
        return self._enhanced_text_similarity(inferred_str, actual_str)
    
    def _to_comparable_string(self, value: Any) -> str:
        """Convert any value to a comparable string."""
        if isinstance(value, str):
            return value
        
        if isinstance(value, (dict, list)):
            try:
                return json.dumps(value, sort_keys=True)
            except:
                return str(value)
        
        return str(value)
    
    def _embedding_similarity(self, text1: str, text2: str) -> float:
        """Compute similarity using embeddings."""
        emb1 = self.embedding_model.embed(text1)
        emb2 = self.embedding_model.embed(text2)
        
        # Cosine similarity
        import numpy as np
        similarity = np.dot(emb1, emb2) / (np.linalg.norm(emb1) * np.linalg.norm(emb2))
        
        return float(similarity)
    
    def _enhanced_text_similarity(self, text1: str, text2: str) -> float:
        """
        Enhanced text similarity without embeddings.
        
        Uses multiple heuristics for semantic matching.
        """
        # Normalize
        text1 = text1.lower().strip()
        text2 = text2.lower().strip()
        
        if text1 == text2:
            return 1.0
        
        # Word overlap
        words1 = set(text1.split())
        words2 = set(text2.split())
        
        if not words1 and not words2:
            return 1.0
        
        if not words1 or not words2:
            return 0.0
        
        intersection = words1 & words2
        union = words1 | words2
        
        jaccard = len(intersection) / len(union) if union else 0.0
        
        # Sequence matcher
        sequence_sim = SequenceMatcher(None, text1, text2).ratio()
        
        # Key entity extraction and matching
        entity_sim = self._entity_similarity(text1, text2)
        
        # Combine scores with weights
        combined = (
            jaccard * 0.35 +
            sequence_sim * 0.35 +
            entity_sim * 0.30
        )
        
        return combined
    
    def _entity_similarity(self, text1: str, text2: str) -> float:
        """Compare key entities in texts."""
        # Extract entities (numbers, dates, capitalized words, URLs, emails)
        entity_patterns = [
            r'\b\d+(?:\.\d+)?\b',  # Numbers
            r'\b\d{4}-\d{2}-\d{2}\b',  # Dates
            r'\b[A-Z][a-z]+(?:\s+[A-Z][a-z]+)*\b',  # Capitalized phrases
            r'https?://[^\s]+',  # URLs
            r'\b[\w.]+@[\w.]+\b',  # Emails
        ]
        
        entities1 = set()
        entities2 = set()
        
        for pattern in entity_patterns:
            entities1.update(re.findall(pattern, text1))
            entities2.update(re.findall(pattern, text2))
        
        if not entities1 and not entities2:
            return 1.0
        
        if not entities1 or not entities2:
            return 0.5  # One has entities, one doesn't
        
        # Entity overlap
        intersection = entities1 & entities2
        union = entities1 | entities2
        
        return len(intersection) / len(union)


class BehavioralComparator(BaseComparator):
    """
    Behavioral comparison - outcome category matching.
    
    Used for tolerance level: BEHAVIORAL (ε < 0.50)
    """
    
    def __init__(self):
        self.semantic = SemanticComparator()
    
    def compare(self, inferred: Any, actual: Any) -> float:
        """Compare based on behavioral equivalence."""
        if inferred is None and actual is None:
            return 1.0
        
        if inferred is None or actual is None:
            return 0.0
        
        # Extract behavioral features
        inferred_behavior = self._extract_behavior(inferred)
        actual_behavior = self._extract_behavior(actual)
        
        # Match on key behavioral dimensions
        dimensions = ['action_type', 'target_entity', 'outcome_category', 'intent']
        
        matches = 0
        total = len(dimensions)
        
        for dim in dimensions:
            if dim in inferred_behavior and dim in actual_behavior:
                if self._behaviors_match(inferred_behavior[dim], actual_behavior[dim]):
                    matches += 1
            else:
                # Partial credit for missing dimensions
                matches += 0.5
        
        return matches / total
    
    def _extract_behavior(self, output: Any) -> Dict[str, Any]:
        """Extract behavioral features from output."""
        output_str = str(output).lower()
        
        behavior = {
            'action_type': self._detect_action_type(output_str),
            'target_entity': self._detect_target_entity(output_str),
            'outcome_category': self._detect_outcome_category(output_str),
            'intent': self._detect_intent(output_str)
        }
        
        return behavior
    
    def _detect_action_type(self, text: str) -> str:
        """Detect the type of action being performed."""
        action_patterns = {
            'create': ['create', 'generate', 'make', 'produce', 'build'],
            'read': ['read', 'extract', 'get', 'fetch', 'retrieve'],
            'update': ['update', 'modify', 'change', 'edit', 'transform'],
            'delete': ['delete', 'remove', 'clear', 'drop'],
            'analyze': ['analyze', 'examine', 'evaluate', 'assess'],
            'search': ['search', 'find', 'lookup', 'query'],
            'summarize': ['summarize', 'condense', 'brief', 'overview'],
        }
        
        for action, keywords in action_patterns.items():
            if any(kw in text for kw in keywords):
                return action
        
        return 'unknown'
    
    def _detect_target_entity(self, text: str) -> str:
        """Detect the target entity of the action."""
        entity_patterns = {
            'document': ['document', 'file', 'pdf', 'docx', 'xlsx'],
            'data': ['data', 'record', 'entry', 'row'],
            'text': ['text', 'content', 'paragraph', 'article'],
            'image': ['image', 'picture', 'photo', 'visual'],
            'code': ['code', 'function', 'class', 'script'],
            'user': ['user', 'customer', 'person', 'account'],
        }
        
        for entity, keywords in entity_patterns.items():
            if any(kw in text for kw in keywords):
                return entity
        
        return 'unknown'
    
    def _detect_outcome_category(self, text: str) -> str:
        """Detect the category of outcome."""
        if 'success' in text or 'completed' in text:
            return 'success'
        
        if 'error' in text or 'failed' in text:
            return 'error'
        
        if 'warning' in text or 'caution' in text:
            return 'warning'
        
        if 'result' in text or 'output' in text:
            return 'result'
        
        return 'neutral'
    
    def _detect_intent(self, text: str) -> str:
        """Detect the intent of the output."""
        intent_patterns = {
            'informative': ['here is', 'the result', 'output shows'],
            'prescriptive': ['you should', 'recommend', 'suggest'],
            'descriptive': ['this is', 'it contains', 'consists of'],
            'confirmative': ['confirmed', 'verified', 'validated'],
        }
        
        for intent, phrases in intent_patterns.items():
            if any(phrase in text for phrase in phrases):
                return intent
        
        return 'neutral'
    
    def _behaviors_match(self, behavior1: str, behavior2: str) -> bool:
        """Check if two behaviors match."""
        if behavior1 == behavior2:
            return True
        
        # Define equivalence classes
        equivalence_classes = [
            {'create', 'generate', 'make'},
            {'read', 'extract', 'fetch'},
            {'update', 'modify', 'change'},
            {'unknown', 'neutral'},
            {'document', 'file'},
            {'success', 'result'},
        ]
        
        for eq_class in equivalence_classes:
            if behavior1 in eq_class and behavior2 in eq_class:
                return True
        
        return False


class OutputComparator:
    """
    Main comparator that routes to appropriate comparison method.
    """
    
    def __init__(self, embedding_model=None):
        self.comparators = {
            ToleranceLevel.EXACT: ExactComparator(),
            ToleranceLevel.CLOSE: StructuralComparator(),
            ToleranceLevel.APPROXIMATE: SemanticComparator(embedding_model),
            ToleranceLevel.BEHAVIORAL: BehavioralComparator(),
        }
    
    def compare(self, inferred: Any, actual: Any,
                tolerance_level: ToleranceLevel) -> ComparisonResult:
        """
        Compare inferred output to actual output.
        
        Args:
            inferred: The inferred/estimated output
            actual: The actual output from execution
            tolerance_level: The tolerance level for comparison
            
        Returns:
            ComparisonResult with similarity score and details
        """
        comparator = self.comparators.get(tolerance_level, SemanticComparator())
        
        similarity = comparator.compare(inferred, actual)
        
        # Determine if within tolerance based on level
        tolerance_thresholds = {
            ToleranceLevel.EXACT: 0.999,
            ToleranceLevel.CLOSE: 0.95,
            ToleranceLevel.APPROXIMATE: 0.80,
            ToleranceLevel.BEHAVIORAL: 0.50,
        }
        
        threshold = tolerance_thresholds[tolerance_level]
        is_within_tolerance = similarity >= threshold
        
        # Generate details
        details = {
            "inferred_type": type(inferred).__name__,
            "actual_type": type(actual).__name__,
            "inferred_preview": str(inferred)[:200] if inferred else None,
            "actual_preview": str(actual)[:200] if actual else None,
            "tolerance_threshold": threshold,
        }
        
        return ComparisonResult(
            similarity=similarity,
            is_within_tolerance=is_within_tolerance,
            tolerance_level=tolerance_level,
            details=details
        )
