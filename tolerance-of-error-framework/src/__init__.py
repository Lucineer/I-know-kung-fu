"""
Tolerance-of-Error Framework for Agent Reasoning

This framework enables approximate execution for AI agents by determining
if inferred reasoning produces outputs within acceptable tolerance of
actual code execution.
"""

from .tolerance_evaluator import ToleranceEvaluator, ToleranceDecision, ToleranceLevel
from .confidence_scorer import ConfidenceScorer
from .output_comparator import OutputComparator, ComparisonResult
from .calibration_pipeline import CalibrationPipeline, CalibrationResult
from .tolerant_executor import TolerantSkillExecutor

__version__ = "1.0.0"
__all__ = [
    "ToleranceEvaluator",
    "ToleranceDecision",
    "ToleranceLevel",
    "ConfidenceScorer",
    "OutputComparator",
    "ComparisonResult",
    "CalibrationPipeline",
    "CalibrationResult",
    "TolerantSkillExecutor",
]
