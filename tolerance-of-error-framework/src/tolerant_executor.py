"""
Tolerant Skill Executor - Wraps skill execution with tolerance-based optimization.
"""

from dataclasses import dataclass
from typing import Any, Callable, Optional, Dict
import asyncio
from datetime import datetime

from .tolerance_evaluator import (
    ToleranceEvaluator, ToleranceDecision, SkillRegistry
)
from .confidence_scorer import ConfidenceScorer
from .output_comparator import OutputComparator
from .calibration_pipeline import CalibrationPipeline, ExecutionTrace


@dataclass
class ExecutionResult:
    """Result of a tolerant skill execution."""
    output: Any
    was_skipped: bool
    confidence: float
    decision: str
    execution_time_ms: float
    fallback_used: bool = False
    comparison_score: Optional[float] = None


class TolerantSkillExecutor:
    """
    Wraps skill execution with tolerance-based optimization.
    
    This executor enables approximate execution by evaluating whether
    inferred outputs are within tolerance before executing tools.
    """
    
    def __init__(self,
                 skill_registry: SkillRegistry = None,
                 evaluator: ToleranceEvaluator = None,
                 confidence_scorer: ConfidenceScorer = None,
                 comparator: OutputComparator = None,
                 calibration_pipeline: CalibrationPipeline = None,
                 embedding_model: Any = None):
        """
        Initialize the tolerant executor.
        
        Args:
            skill_registry: Registry for skill configurations
            evaluator: Tolerance evaluator for decisions
            confidence_scorer: Confidence scoring component
            comparator: Output comparison component
            calibration_pipeline: Pipeline for continuous calibration
            embedding_model: Optional embedding model for semantic comparison
        """
        self.registry = skill_registry or SkillRegistry()
        self.evaluator = evaluator or ToleranceEvaluator(self.registry)
        self.scorer = confidence_scorer or ConfidenceScorer()
        self.comparator = comparator or OutputComparator(embedding_model)
        self.calibration = calibration_pipeline
        
        # Statistics tracking
        self.stats = {
            "total_executions": 0,
            "skipped_executions": 0,
            "fallback_executions": 0,
            "full_executions": 0,
            "total_time_saved_ms": 0,
        }
    
    async def execute(self,
                      skill_name: str,
                      operation: str,
                      params: dict,
                      execute_fn: Callable,
                      inferred_output: Any = None,
                      confidence: float = None,
                      context: dict = None) -> ExecutionResult:
        """
        Execute a skill operation with tolerance-based optimization.
        
        Args:
            skill_name: Name of the skill
            operation: Operation to perform
            params: Parameters for the operation
            execute_fn: Async function that performs actual execution
            inferred_output: Optional pre-inferred output
            confidence: Optional confidence score for inferred output
            context: Additional context for decision-making
            
        Returns:
            ExecutionResult with output and execution metadata
        """
        start_time = datetime.now()
        self.stats["total_executions"] += 1
        context = context or {}
        
        # Calculate confidence if not provided
        if confidence is None and inferred_output is not None:
            confidence = self.scorer.score(
                skill_name, operation, inferred_output, context
            )
        
        # Evaluate tolerance decision
        decision = None
        if inferred_output is not None and confidence is not None:
            decision = self.evaluator.evaluate(
                skill_name, operation, inferred_output, confidence, context
            )
        
        # Handle skip decision
        if decision == ToleranceDecision.SKIP_EXECUTION:
            execution_time = (datetime.now() - start_time).total_seconds() * 1000
            
            self.stats["skipped_executions"] += 1
            self.stats["total_time_saved_ms"] += max(0, 100 - execution_time)
            
            # Log skip for calibration (if we have calibration pipeline)
            self._log_skip(skill_name, operation, params, inferred_output, confidence)
            
            return ExecutionResult(
                output=inferred_output,
                was_skipped=True,
                confidence=confidence,
                decision="skipped",
                execution_time_ms=execution_time
            )
        
        # Handle fallback decision
        if decision == ToleranceDecision.FALLBACK:
            result = await self._execute_with_fallback(
                skill_name, operation, params, execute_fn, 
                inferred_output, confidence
            )
            self.stats["fallback_executions"] += 1
            return result
        
        # Full execution
        actual_output = await self._execute_tool(execute_fn, params)
        execution_time = (datetime.now() - start_time).total_seconds() * 1000
        
        self.stats["full_executions"] += 1
        
        # Compare inferred vs actual for calibration
        comparison_score = None
        if inferred_output is not None:
            comparison = self._compare_outputs(
                skill_name, operation, inferred_output, actual_output
            )
            comparison_score = comparison.similarity
            
            # Store for calibration
            self._store_comparison(
                skill_name, operation, params,
                inferred_output, actual_output,
                confidence, comparison.error
            )
        
        return ExecutionResult(
            output=actual_output,
            was_skipped=False,
            confidence=confidence or 0.0,
            decision="executed",
            execution_time_ms=execution_time,
            comparison_score=comparison_score
        )
    
    async def _execute_tool(self, execute_fn: Callable, params: dict) -> Any:
        """Execute the actual tool function."""
        if asyncio.iscoroutinefunction(execute_fn):
            return await execute_fn(**params)
        else:
            return execute_fn(**params)
    
    async def _execute_with_fallback(self,
                                     skill_name: str,
                                     operation: str,
                                     params: dict,
                                     execute_fn: Callable,
                                     inferred_output: Any,
                                     confidence: float) -> ExecutionResult:
        """
        Execute with fallback handling.
        
        Fallback mode executes the tool but also validates the inferred output.
        """
        start_time = datetime.now()
        
        # Execute actual tool
        actual_output = await self._execute_tool(execute_fn, params)
        
        # Compare with inferred output
        comparison = self._compare_outputs(
            skill_name, operation, inferred_output, actual_output
        )
        
        # Store for calibration
        self._store_comparison(
            skill_name, operation, params,
            inferred_output, actual_output,
            confidence, comparison.error
        )
        
        execution_time = (datetime.now() - start_time).total_seconds() * 1000
        
        return ExecutionResult(
            output=actual_output,
            was_skipped=False,
            confidence=confidence,
            decision="fallback",
            execution_time_ms=execution_time,
            fallback_used=True,
            comparison_score=comparison.similarity
        )
    
    def _compare_outputs(self,
                        skill_name: str,
                        operation: str,
                        inferred: Any,
                        actual: Any):
        """Compare inferred output to actual output."""
        skill_config = self.registry.get(skill_name)
        tolerance_config = skill_config.get_tolerance(operation)
        
        return self.comparator.compare(
            inferred, actual, tolerance_config.tolerance_level
        )
    
    def _log_skip(self, skill_name: str, operation: str,
                  params: dict, inferred: Any, confidence: float):
        """Log a skipped execution for future calibration."""
        if self.calibration:
            trace = ExecutionTrace(
                operation=operation,
                input_params=params,
                inferred_output=inferred,
                actual_output=None,  # Not known since we skipped
                confidence=confidence,
                error=0.0,  # Assume 0 since we skipped
                timestamp=str(datetime.now())
            )
            # Note: We don't add to calibration since we don't have actual output
            # This could be enhanced with periodic validation runs
    
    def _store_comparison(self,
                          skill_name: str,
                          operation: str,
                          params: dict,
                          inferred: Any,
                          actual: Any,
                          confidence: float,
                          error: float):
        """Store comparison result for calibration."""
        if self.calibration:
            trace = ExecutionTrace(
                operation=operation,
                input_params=params,
                inferred_output=inferred,
                actual_output=actual,
                confidence=confidence,
                error=error,
                timestamp=str(datetime.now())
            )
            self.calibration.add_trace(skill_name, trace)
    
    def get_stats(self) -> Dict[str, Any]:
        """Get execution statistics."""
        total = self.stats["total_executions"]
        
        return {
            "total_executions": total,
            "skipped_executions": self.stats["skipped_executions"],
            "fallback_executions": self.stats["fallback_executions"],
            "full_executions": self.stats["full_executions"],
            "skip_rate": self.stats["skipped_executions"] / total if total > 0 else 0,
            "fallback_rate": self.stats["fallback_executions"] / total if total > 0 else 0,
            "total_time_saved_ms": self.stats["total_time_saved_ms"],
            "avg_time_saved_ms": (
                self.stats["total_time_saved_ms"] / self.stats["skipped_executions"]
                if self.stats["skipped_executions"] > 0 else 0
            )
        }
    
    def reset_stats(self):
        """Reset execution statistics."""
        self.stats = {
            "total_executions": 0,
            "skipped_executions": 0,
            "fallback_executions": 0,
            "full_executions": 0,
            "total_time_saved_ms": 0,
        }


class SkillExecutionWrapper:
    """
    Convenience wrapper for making any skill tolerance-aware.
    
    Usage:
        wrapper = SkillExecutionWrapper("pdf", executor)
        result = await wrapper.execute("extract_text", {"file": "doc.pdf"})
    """
    
    def __init__(self, skill_name: str, executor: TolerantSkillExecutor):
        self.skill_name = skill_name
        self.executor = executor
    
    async def execute(self,
                      operation: str,
                      params: dict,
                      execute_fn: Callable,
                      inferred_output: Any = None,
                      confidence: float = None,
                      context: dict = None) -> ExecutionResult:
        """Execute with skill name pre-filled."""
        return await self.executor.execute(
            skill_name=self.skill_name,
            operation=operation,
            params=params,
            execute_fn=execute_fn,
            inferred_output=inferred_output,
            confidence=confidence,
            context=context
        )


# Utility functions for integration

def create_tolerant_executor(embedding_model=None) -> TolerantSkillExecutor:
    """
    Factory function to create a fully configured executor.
    
    Args:
        embedding_model: Optional embedding model for semantic comparison
        
    Returns:
        Configured TolerantSkillExecutor
    """
    from .tolerance_evaluator import SkillRegistry, CalibrationDatabase
    
    registry = SkillRegistry()
    db = CalibrationDatabase()
    evaluator = ToleranceEvaluator(registry, db)
    scorer = ConfidenceScorer()
    comparator = OutputComparator(embedding_model)
    
    return TolerantSkillExecutor(
        skill_registry=registry,
        evaluator=evaluator,
        confidence_scorer=scorer,
        comparator=comparator,
        calibration_pipeline=None  # Optional: add calibration pipeline
    )


async def execute_with_tolerance(skill_name: str,
                                  operation: str,
                                  params: dict,
                                  execute_fn: Callable,
                                  inferred_output: Any = None,
                                  confidence: float = None) -> ExecutionResult:
    """
    Convenience function for one-off tolerant execution.
    
    Creates an executor on the fly and executes.
    For repeated use, create and reuse an executor instance.
    """
    executor = create_tolerant_executor()
    return await executor.execute(
        skill_name=skill_name,
        operation=operation,
        params=params,
        execute_fn=execute_fn,
        inferred_output=inferred_output,
        confidence=confidence
    )
