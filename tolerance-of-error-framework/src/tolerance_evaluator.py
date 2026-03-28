"""
Tolerance Evaluator - Core decision engine for skip/execute decisions.
"""

from dataclasses import dataclass
from enum import Enum
from typing import Any, Optional, Dict
import json
from pathlib import Path


class ToleranceLevel(Enum):
    """Tolerance levels for different task types."""
    EXACT = "exact"          # ε < 0.001
    CLOSE = "close"          # ε < 0.05
    APPROXIMATE = "approximate"  # ε < 0.20
    BEHAVIORAL = "behavioral"    # ε < 0.50


class ToleranceDecision(Enum):
    """Decision outcomes from tolerance evaluation."""
    SKIP_EXECUTION = "skip_execution"
    FALLBACK = "fallback"
    EXECUTE_ANYWAY = "execute_anyway"


@dataclass
class ToleranceThreshold:
    """Thresholds for a specific skill/operation combination."""
    skip_threshold: float
    fallback_threshold: float
    tolerance_level: ToleranceLevel
    comparison_method: str
    
    @classmethod
    def from_dict(cls, data: dict) -> "ToleranceThreshold":
        return cls(
            skip_threshold=data["skip_threshold"],
            fallback_threshold=data.get("fallback_threshold", data["skip_threshold"] - 0.1),
            tolerance_level=ToleranceLevel(data["tolerance"]),
            comparison_method=data.get("comparison", "semantic")
        )


@dataclass
class SkillConfig:
    """Configuration for a skill's tolerance settings."""
    skill_name: str
    default_tolerance: ToleranceLevel
    default_threshold: float
    operation_thresholds: Dict[str, ToleranceThreshold]
    fallback_policy: str
    never_skip_operations: list
    
    def get_tolerance(self, operation: str) -> ToleranceThreshold:
        """Get tolerance configuration for a specific operation."""
        if operation in self.operation_thresholds:
            return self.operation_thresholds[operation]
        
        # Return default
        return ToleranceThreshold(
            skip_threshold=self.default_threshold,
            fallback_threshold=self.default_threshold - 0.1,
            tolerance_level=self.default_tolerance,
            comparison_method="semantic"
        )


class SkillRegistry:
    """Registry for skill tolerance configurations."""
    
    DEFAULT_CONFIGS = {
        "document-processing": {
            "default_tolerance": ToleranceLevel.CLOSE,
            "default_threshold": 0.90,
            "fallback_policy": "execute_with_validation",
            "never_skip": ["fill_form"]
        },
        "web-operations": {
            "default_tolerance": ToleranceLevel.APPROXIMATE,
            "default_threshold": 0.80,
            "fallback_policy": "execute_with_retry",
            "never_skip": []
        },
        "financial-analysis": {
            "default_tolerance": ToleranceLevel.EXACT,
            "default_threshold": 0.98,
            "fallback_policy": "always_execute",
            "never_skip": ["get_price", "calculate_metrics"]
        },
        "content-generation": {
            "default_tolerance": ToleranceLevel.BEHAVIORAL,
            "default_threshold": 0.70,
            "fallback_policy": "execute_if_requested",
            "never_skip": []
        },
        "code-operations": {
            "default_tolerance": ToleranceLevel.CLOSE,
            "default_threshold": 0.92,
            "fallback_policy": "execute_and_validate",
            "never_skip": ["test"]
        },
        "media-generation": {
            "default_tolerance": ToleranceLevel.BEHAVIORAL,
            "default_threshold": 0.60,
            "fallback_policy": "execute_if_confidence_low",
            "never_skip": []
        },
        "data-analysis": {
            "default_tolerance": ToleranceLevel.APPROXIMATE,
            "default_threshold": 0.85,
            "fallback_policy": "execute_with_spot_check",
            "never_skip": []
        }
    }
    
    def __init__(self, config_path: Optional[Path] = None):
        self.skills: Dict[str, SkillConfig] = {}
        self._load_defaults()
        if config_path:
            self._load_config(config_path)
    
    def _load_defaults(self):
        """Load default configurations for known skill categories."""
        # Map specific skills to categories
        skill_to_category = {
            "pdf": "document-processing",
            "docx": "document-processing",
            "xlsx": "document-processing",
            "pptx": "document-processing",
            "web-search": "web-operations",
            "web-reader": "web-operations",
            "agent-browser": "web-operations",
            "finance": "financial-analysis",
            "stock-analysis-skill": "financial-analysis",
            "blog-writer": "content-generation",
            "content-strategy": "content-generation",
            "coding-agent": "code-operations",
            "image-generation": "media-generation",
            "video-generation": "media-generation",
            "TTS": "media-generation",
            "ASR": "media-generation",
            "market-analyst": "data-analysis",
            "sentiment-analyzer": "data-analysis",
        }
        
        for skill, category in skill_to_category.items():
            config = self.DEFAULT_CONFIGS[category]
            self.skills[skill] = SkillConfig(
                skill_name=skill,
                default_tolerance=config["default_tolerance"],
                default_threshold=config["default_threshold"],
                operation_thresholds={},
                fallback_policy=config["fallback_policy"],
                never_skip_operations=config["never_skip"]
            )
    
    def _load_config(self, config_path: Path):
        """Load custom configurations from file."""
        with open(config_path) as f:
            data = json.load(f)
        
        for skill_config in data.get("skills", []):
            self.skills[skill_config["skill_name"]] = SkillConfig(
                skill_name=skill_config["skill_name"],
                default_tolerance=ToleranceLevel(skill_config["default_tolerance"]),
                default_threshold=skill_config["confidence_threshold"],
                operation_thresholds={
                    op: ToleranceThreshold.from_dict(thresh)
                    for op, thresh in skill_config.get("tolerance_by_operation", {}).items()
                },
                fallback_policy=skill_config.get("fallback_policy", "execute_with_validation"),
                never_skip_operations=skill_config.get("never_skip_operations", [])
            )
    
    def get(self, skill_name: str) -> SkillConfig:
        """Get configuration for a skill."""
        if skill_name not in self.skills:
            # Return default config
            return SkillConfig(
                skill_name=skill_name,
                default_tolerance=ToleranceLevel.APPROXIMATE,
                default_threshold=0.85,
                operation_thresholds={},
                fallback_policy="execute_with_validation",
                never_skip_operations=[]
            )
        return self.skills[skill_name]


class CalibrationDatabase:
    """Database for storing and retrieving calibration data."""
    
    def __init__(self, db_path: Optional[Path] = None):
        self.db_path = db_path or Path("/tmp/tolerance_calibration.json")
        self._data: Dict[str, list] = {}
        self._thresholds: Dict[str, Dict[str, ToleranceThreshold]] = {}
        
        if self.db_path.exists():
            self._load()
    
    def _load(self):
        """Load calibration data from disk."""
        with open(self.db_path) as f:
            data = json.load(f)
        
        self._data = data.get("traces", {})
        
        for skill, thresholds in data.get("thresholds", {}).items():
            self._thresholds[skill] = {
                level: ToleranceThreshold.from_dict(thresh)
                for level, thresh in thresholds.items()
            }
    
    def _save(self):
        """Save calibration data to disk."""
        data = {
            "traces": self._data,
            "thresholds": {
                skill: {
                    level: {
                        "skip_threshold": thresh.skip_threshold,
                        "fallback_threshold": thresh.fallback_threshold,
                        "tolerance": thresh.tolerance_level.value,
                        "comparison": thresh.comparison_method
                    }
                    for level, thresh in levels.items()
                }
                for skill, levels in self._thresholds.items()
            }
        }
        
        with open(self.db_path, "w") as f:
            json.dump(data, f, indent=2)
    
    def add_trace(self, skill_name: str, operation: str, 
                  inferred: Any, actual: Any, confidence: float, error: float):
        """Add an execution trace to the database."""
        if skill_name not in self._data:
            self._data[skill_name] = []
        
        self._data[skill_name].append({
            "operation": operation,
            "inferred": str(inferred)[:1000],  # Truncate for storage
            "actual": str(actual)[:1000],
            "confidence": confidence,
            "error": error,
            "timestamp": str(datetime.now())
        })
        
        self._save()
    
    def get_traces(self, skill_name: str, limit: int = 1000) -> list:
        """Get traces for a skill."""
        traces = self._data.get(skill_name, [])
        return traces[-limit:]
    
    def get_threshold(self, skill_name: str, 
                      tolerance_level: ToleranceLevel) -> ToleranceThreshold:
        """Get calibrated threshold for a skill/tolerance combination."""
        key = tolerance_level.value
        
        if skill_name in self._thresholds and key in self._thresholds[skill_name]:
            return self._thresholds[skill_name][key]
        
        # Return defaults based on tolerance level
        defaults = {
            ToleranceLevel.EXACT: ToleranceThreshold(1.0, 1.0, tolerance_level, "exact"),
            ToleranceLevel.CLOSE: ToleranceThreshold(0.95, 0.85, tolerance_level, "structural"),
            ToleranceLevel.APPROXIMATE: ToleranceThreshold(0.85, 0.75, tolerance_level, "semantic"),
            ToleranceLevel.BEHAVIORAL: ToleranceThreshold(0.70, 0.60, tolerance_level, "behavioral"),
        }
        return defaults[tolerance_level]
    
    def update_thresholds(self, skill_name: str, skip_threshold: float, 
                         fallback_threshold: float, tolerance_level: ToleranceLevel = None):
        """Update thresholds for a skill."""
        if skill_name not in self._thresholds:
            self._thresholds[skill_name] = {}
        
        level = tolerance_level or ToleranceLevel.APPROXIMATE
        self._thresholds[skill_name][level.value] = ToleranceThreshold(
            skip_threshold=skip_threshold,
            fallback_threshold=fallback_threshold,
            tolerance_level=level,
            comparison_method="semantic"
        )
        
        self._save()


class ToleranceEvaluator:
    """
    Determines if inferred output is within tolerance of actual execution.
    
    This is the core decision engine that evaluates whether an agent's
    inferred reasoning is sufficiently accurate to skip actual code execution.
    """
    
    # Operations that should never be skipped regardless of confidence
    NEVER_SKIP_OPERATIONS = {
        "financial_transaction",
        "data_deletion", 
        "security_operation",
        "legal_document_signing",
        "medical_diagnosis",
        "authentication",
        "authorization"
    }
    
    def __init__(self, skill_registry: SkillRegistry = None, 
                 calibration_db: CalibrationDatabase = None):
        self.skill_registry = skill_registry or SkillRegistry()
        self.calibration_db = calibration_db or CalibrationDatabase()
    
    def evaluate(self, skill_name: str, operation: str,
                 inferred_output: Any, confidence: float,
                 context: dict = None) -> ToleranceDecision:
        """
        Evaluate whether to skip execution, use fallback, or execute fully.
        
        Args:
            skill_name: Name of the skill being invoked
            operation: Specific operation within the skill
            inferred_output: The agent's inferred output
            confidence: Confidence score in [0, 1]
            context: Additional context for decision-making
            
        Returns:
            ToleranceDecision indicating what action to take
        """
        # Safety check: never skip certain operations
        if operation in self.NEVER_SKIP_OPERATIONS:
            return ToleranceDecision.EXECUTE_ANYWAY
        
        # Get skill configuration
        skill_config = self.skill_registry.get(skill_name)
        
        # Check if this operation is in the never-skip list for this skill
        if operation in skill_config.never_skip_operations:
            return ToleranceDecision.EXECUTE_ANYWAY
        
        # Get tolerance threshold
        tolerance_config = skill_config.get_tolerance(operation)
        
        # Check calibrated threshold from database
        calibrated_threshold = self.calibration_db.get_threshold(
            skill_name, tolerance_config.tolerance_level
        )
        
        # Use the more conservative (higher) threshold
        skip_threshold = max(
            tolerance_config.skip_threshold,
            calibrated_threshold.skip_threshold
        )
        fallback_threshold = max(
            tolerance_config.fallback_threshold,
            calibrated_threshold.fallback_threshold
        )
        
        # Make decision based on confidence
        if confidence >= skip_threshold:
            return ToleranceDecision.SKIP_EXECUTION
        elif confidence >= fallback_threshold:
            return ToleranceDecision.FALLBACK
        else:
            return ToleranceDecision.EXECUTE_ANYWAY
    
    def get_comparison_method(self, skill_name: str, operation: str) -> str:
        """Get the appropriate comparison method for a skill/operation."""
        skill_config = self.skill_registry.get(skill_name)
        tolerance_config = skill_config.get_tolerance(operation)
        return tolerance_config.comparison_method


# Import datetime at the end to avoid circular imports
from datetime import datetime
