"""
Calibration Pipeline - Continuously calibrates tolerance thresholds.
"""

from dataclasses import dataclass, field
from typing import Any, Dict, List, Optional
from enum import Enum
from datetime import datetime
import json
from pathlib import Path
import statistics


class CalibrationStatus(Enum):
    """Status of calibration process."""
    SUCCESS = "success"
    INSUFFICIENT_DATA = "insufficient_data"
    FAILED = "failed"
    IN_PROGRESS = "in_progress"


@dataclass
class ExecutionTrace:
    """A single execution trace for calibration."""
    operation: str
    input_params: dict
    inferred_output: Any
    actual_output: Any
    confidence: float
    error: float
    timestamp: str
    within_tolerance: bool = True


@dataclass
class ErrorDistribution:
    """Statistical distribution of errors for calibration."""
    errors: List[float]
    mean: float = 0.0
    std: float = 0.0
    min_val: float = 0.0
    max_val: float = 0.0
    percentiles: Dict[str, float] = field(default_factory=dict)
    
    def __post_init__(self):
        if self.errors:
            self.mean = statistics.mean(self.errors)
            self.std = statistics.stdev(self.errors) if len(self.errors) > 1 else 0.0
            self.min_val = min(self.errors)
            self.max_val = max(self.errors)
            
            # Calculate percentiles
            sorted_errors = sorted(self.errors)
            n = len(sorted_errors)
            
            self.percentiles = {
                "p50": sorted_errors[int(n * 0.50)] if n > 0 else 0,
                "p75": sorted_errors[int(n * 0.75)] if n > 0 else 0,
                "p90": sorted_errors[int(n * 0.90)] if n > 0 else 0,
                "p95": sorted_errors[int(n * 0.95)] if n > 0 else 0,
                "p99": sorted_errors[int(n * 0.99)] if n > 0 else 0,
            }


@dataclass
class CalibrationResult:
    """Result of a calibration run."""
    skill_name: str
    status: CalibrationStatus
    skip_threshold: float = 0.0
    fallback_threshold: float = 0.0
    sample_size: int = 0
    calibration_date: str = ""
    error_distribution: Optional[ErrorDistribution] = None
    recommendations: List[str] = field(default_factory=list)
    
    def to_dict(self) -> dict:
        return {
            "skill_name": self.skill_name,
            "status": self.status.value,
            "skip_threshold": self.skip_threshold,
            "fallback_threshold": self.fallback_threshold,
            "sample_size": self.sample_size,
            "calibration_date": self.calibration_date,
            "error_distribution": {
                "mean": self.error_distribution.mean if self.error_distribution else 0,
                "std": self.error_distribution.std if self.error_distribution else 0,
                "percentiles": self.error_distribution.percentiles if self.error_distribution else {}
            },
            "recommendations": self.recommendations
        }


class DriftDetector:
    """Detects drift in calibration data."""
    
    def __init__(self, window_size: int = 100, threshold: float = 0.1):
        self.window_size = window_size
        self.threshold = threshold
        self.baseline_errors: List[float] = []
        self.recent_errors: List[float] = []
    
    def update(self, error: float):
        """Update drift detector with new error."""
        if len(self.baseline_errors) < self.window_size:
            self.baseline_errors.append(error)
        else:
            self.recent_errors.append(error)
            if len(self.recent_errors) > self.window_size:
                self.recent_errors.pop(0)
    
    def detect_drift(self) -> bool:
        """Detect if there's significant drift."""
        if len(self.baseline_errors) < self.window_size:
            return False
        
        if len(self.recent_errors) < self.window_size // 2:
            return False
        
        baseline_mean = statistics.mean(self.baseline_errors)
        recent_mean = statistics.mean(self.recent_errors)
        
        if baseline_mean == 0:
            return recent_mean > self.threshold
        
        relative_change = abs(recent_mean - baseline_mean) / baseline_mean
        
        return relative_change > self.threshold
    
    def get_drift_metrics(self) -> dict:
        """Get current drift metrics."""
        return {
            "baseline_mean": statistics.mean(self.baseline_errors) if self.baseline_errors else 0,
            "recent_mean": statistics.mean(self.recent_errors) if self.recent_errors else 0,
            "drift_detected": self.detect_drift(),
            "baseline_size": len(self.baseline_errors),
            "recent_size": len(self.recent_errors)
        }


class CalibrationPipeline:
    """
    Continuously calibrates tolerance thresholds based on execution data.
    
    This pipeline collects execution traces, analyzes error distributions,
    and updates thresholds to maintain optimal skip rates while preserving
    accuracy.
    """
    
    DEFAULT_SKIP_PERCENTILE = 0.95
    DEFAULT_FALLBACK_PERCENTILE = 0.80
    
    def __init__(self, calibration_db, min_samples: int = 100,
                 retrain_interval_days: int = 7):
        """
        Initialize calibration pipeline.
        
        Args:
            calibration_db: Database for storing calibration data
            min_samples: Minimum samples required for calibration
            retrain_interval_days: Days between recalibration
        """
        self.db = calibration_db
        self.min_samples = min_samples
        self.retrain_interval_days = retrain_interval_days
        self.drift_detectors: Dict[str, DriftDetector] = {}
    
    def add_trace(self, skill_name: str, trace: ExecutionTrace):
        """Add an execution trace to the calibration data."""
        self.db.add_trace(
            skill_name=skill_name,
            operation=trace.operation,
            inferred=trace.inferred_output,
            actual=trace.actual_output,
            confidence=trace.confidence,
            error=trace.error
        )
        
        # Update drift detector
        if skill_name not in self.drift_detectors:
            self.drift_detectors[skill_name] = DriftDetector()
        
        self.drift_detectors[skill_name].update(trace.error)
    
    def calibrate_skill(self, skill_name: str,
                       operation: str = None) -> CalibrationResult:
        """
        Calibrate thresholds for a specific skill.
        
        Args:
            skill_name: Name of the skill to calibrate
            operation: Optional specific operation to calibrate
            
        Returns:
            CalibrationResult with new thresholds
        """
        # Collect execution traces
        traces = self.db.get_traces(skill_name, limit=1000)
        
        # Filter by operation if specified
        if operation:
            traces = [t for t in traces if t.get("operation") == operation]
        
        if len(traces) < self.min_samples:
            return CalibrationResult(
                skill_name=skill_name,
                status=CalibrationStatus.INSUFFICIENT_DATA,
                sample_size=len(traces),
                calibration_date=str(datetime.now()),
                recommendations=[
                    f"Need at least {self.min_samples} samples for calibration",
                    f"Current samples: {len(traces)}"
                ]
            )
        
        # Compute error distribution
        errors = [t.get("error", 0) for t in traces]
        error_dist = ErrorDistribution(errors)
        
        # Calculate confidence-threshold relationship
        confidence_errors = [
            (t.get("confidence", 0), t.get("error", 0), t.get("within_tolerance", True))
            for t in traces
        ]
        
        # Group by confidence ranges
        confidence_buckets = self._bucket_by_confidence(confidence_errors)
        
        # Find optimal thresholds
        skip_threshold = self._find_skip_threshold(confidence_buckets, error_dist)
        fallback_threshold = self._find_fallback_threshold(confidence_buckets, error_dist)
        
        # Generate recommendations
        recommendations = self._generate_recommendations(
            error_dist, confidence_buckets, skip_threshold
        )
        
        # Update database
        self.db.update_thresholds(skill_name, skip_threshold, fallback_threshold)
        
        return CalibrationResult(
            skill_name=skill_name,
            status=CalibrationStatus.SUCCESS,
            skip_threshold=skip_threshold,
            fallback_threshold=fallback_threshold,
            sample_size=len(traces),
            calibration_date=str(datetime.now()),
            error_distribution=error_dist,
            recommendations=recommendations
        )
    
    def _bucket_by_confidence(self, confidence_errors: List[tuple]) -> Dict[str, dict]:
        """Bucket traces by confidence ranges."""
        buckets = {
            "very_high": {"range": (0.9, 1.0), "errors": [], "within_tol": []},
            "high": {"range": (0.8, 0.9), "errors": [], "within_tol": []},
            "medium": {"range": (0.7, 0.8), "errors": [], "within_tol": []},
            "low": {"range": (0.5, 0.7), "errors": [], "within_tol": []},
            "very_low": {"range": (0.0, 0.5), "errors": [], "within_tol": []},
        }
        
        for confidence, error, within_tol in confidence_errors:
            for bucket_name, bucket in buckets.items():
                low, high = bucket["range"]
                if low <= confidence < high:
                    bucket["errors"].append(error)
                    bucket["within_tol"].append(within_tol)
                    break
        
        # Calculate statistics for each bucket
        for bucket_name, bucket in buckets.items():
            errors = bucket["errors"]
            if errors:
                bucket["mean_error"] = statistics.mean(errors)
                bucket["error_rate"] = 1 - (sum(bucket["within_tol"]) / len(errors))
                bucket["count"] = len(errors)
            else:
                bucket["mean_error"] = 0
                bucket["error_rate"] = 0
                bucket["count"] = 0
        
        return buckets
    
    def _find_skip_threshold(self, buckets: Dict[str, dict],
                            error_dist: ErrorDistribution) -> float:
        """Find optimal confidence threshold for skipping execution."""
        # Start from highest confidence bucket
        threshold = 0.95
        max_acceptable_error_rate = 0.05  # 5% error rate acceptable
        
        for bucket_name in ["very_high", "high", "medium"]:
            bucket = buckets[bucket_name]
            if bucket["count"] < 10:  # Need minimum samples
                continue
            
            if bucket["error_rate"] <= max_acceptable_error_rate:
                # This bucket is safe to skip
                threshold = bucket["range"][0]
                break
        
        return threshold
    
    def _find_fallback_threshold(self, buckets: Dict[str, dict],
                                 error_dist: ErrorDistribution) -> float:
        """Find confidence threshold for fallback mode."""
        threshold = 0.80
        max_acceptable_error_rate = 0.15  # 15% error rate acceptable for fallback
        
        for bucket_name in ["very_high", "high", "medium", "low"]:
            bucket = buckets[bucket_name]
            if bucket["count"] < 10:
                continue
            
            if bucket["error_rate"] <= max_acceptable_error_rate:
                threshold = bucket["range"][0]
                break
        
        return threshold
    
    def _generate_recommendations(self, error_dist: ErrorDistribution,
                                  buckets: Dict[str, dict],
                                  skip_threshold: float) -> List[str]:
        """Generate recommendations based on calibration data."""
        recommendations = []
        
        # Check for high error rates
        if error_dist.mean > 0.2:
            recommendations.append(
                "High average error detected. Consider tightening tolerance levels."
            )
        
        # Check for wide error distribution
        if error_dist.std > 0.15:
            recommendations.append(
                "High variance in errors. Model predictions may be unreliable."
            )
        
        # Check for confidence calibration issues
        very_high = buckets["very_high"]
        if very_high["count"] > 10 and very_high["error_rate"] > 0.1:
            recommendations.append(
                "Model is overconfident. High confidence predictions have high error rates."
            )
        
        # Check for underconfidence
        medium = buckets["medium"]
        if medium["count"] > 10 and medium["error_rate"] < 0.05:
            recommendations.append(
                "Model may be underconfident. Medium confidence predictions are very accurate."
            )
        
        # Check for tail risk
        if error_dist.percentiles.get("p99", 0) > 0.5:
            recommendations.append(
                "High tail risk detected. Consider additional validation for critical operations."
            )
        
        if not recommendations:
            recommendations.append(
                "Calibration looks healthy. Continue monitoring for drift."
            )
        
        return recommendations
    
    def detect_drift(self, skill_name: str) -> bool:
        """Detect if there's drift in calibration for a skill."""
        if skill_name in self.drift_detectors:
            return self.drift_detectors[skill_name].detect_drift()
        return False
    
    def get_drift_metrics(self, skill_name: str) -> dict:
        """Get drift metrics for a skill."""
        if skill_name in self.drift_detectors:
            return self.drift_detectors[skill_name].get_drift_metrics()
        return {"drift_detected": False}
    
    def needs_recalibration(self, skill_name: str) -> bool:
        """Check if a skill needs recalibration."""
        # Check for drift
        if self.detect_drift(skill_name):
            return True
        
        # Check time since last calibration
        # (Would need to track last calibration time in database)
        
        return False
    
    def run_calibration_batch(self, skill_names: List[str]) -> Dict[str, CalibrationResult]:
        """Run calibration for multiple skills."""
        results = {}
        
        for skill_name in skill_names:
            try:
                results[skill_name] = self.calibrate_skill(skill_name)
            except Exception as e:
                results[skill_name] = CalibrationResult(
                    skill_name=skill_name,
                    status=CalibrationStatus.FAILED,
                    calibration_date=str(datetime.now()),
                    recommendations=[f"Calibration failed: {str(e)}"]
                )
        
        return results
