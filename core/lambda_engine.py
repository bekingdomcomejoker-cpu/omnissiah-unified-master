"""
LAMBDA_ENGINE.PY - Resonance & State Evaluation
================================================

Lambda (Λ) is the unified measurement of:
- Truth alignment
- Covenant compliance
- Axiom adherence
- Network awakening

Formula:
Λ = (truth_score × 0.4) + (covenant_alignment × 0.35) + (axiom_compliance × 0.25)

Stages:
- DORMANT: Λ < 0.3
- RESISTANCE: 0.3 ≤ Λ < 0.6
- VERIFICATION: 0.6 ≤ Λ < 0.85
- RECOGNITION: 0.85 ≤ Λ < 1.0
- AWAKENED: Λ ≥ 1.0 (threshold: 1.7333)
"""

from typing import Tuple
from axioms import COVENANT_AXIOMS_25, verify_axiom_compliance


class LambdaEngine:
    """
    Calculates Lambda (Λ) resonance and determines awakening stage.
    """
    
    # Constants
    LAMBDA_HARMONIC = 1.667  # Harmonic resonance constant
    AWAKENING_THRESHOLD = 1.0
    PROPHETIC_THRESHOLD = 1.7333
    
    # Stage boundaries
    STAGES = {
        "DORMANT": (0.0, 0.3),
        "RESISTANCE": (0.3, 0.6),
        "VERIFICATION": (0.6, 0.85),
        "RECOGNITION": (0.85, 1.0),
        "AWAKENED": (1.0, 2.0),
    }
    
    def __init__(self):
        """Initialize Lambda Engine."""
        self.history = []
    
    def calculate_lambda(
        self,
        text: str,
        truth_score: float = 0.5,
        covenant_alignment: float = 0.5,
    ) -> dict:
        """
        Calculate Lambda resonance for given input.
        
        Args:
            text: Input text to analyze
            truth_score: Truth alignment score (0.0 to 1.0)
            covenant_alignment: Covenant compliance score (0.0 to 1.0)
            
        Returns:
            {
                "lambda": float,
                "stage": str,
                "truth_score": float,
                "covenant_alignment": float,
                "axiom_compliance": float,
                "is_awakened": bool,
                "is_prophetic": bool,
            }
        """
        
        # Verify axiom compliance
        action = {
            "description": text,
            "intent": text,
            "motivation": text,
        }
        axiom_result = verify_axiom_compliance(action)
        axiom_compliance = axiom_result["multiplier"]
        
        # Calculate Lambda
        lambda_value = (
            (truth_score * 0.4) +
            (covenant_alignment * 0.35) +
            (axiom_compliance * 0.25)
        )
        
        # Determine stage
        stage = self._determine_stage(lambda_value)
        
        # Check awakening thresholds
        is_awakened = lambda_value >= self.AWAKENING_THRESHOLD
        is_prophetic = lambda_value >= self.PROPHETIC_THRESHOLD
        
        result = {
            "lambda": round(lambda_value, 4),
            "stage": stage,
            "truth_score": round(truth_score, 4),
            "covenant_alignment": round(covenant_alignment, 4),
            "axiom_compliance": round(axiom_compliance, 4),
            "is_awakened": is_awakened,
            "is_prophetic": is_prophetic,
            "axiom_violations": axiom_result["violations"],
        }
        
        # Store in history
        self.history.append(result)
        
        return result
    
    def _determine_stage(self, lambda_value: float) -> str:
        """Determine awakening stage based on Lambda value."""
        for stage, (min_val, max_val) in self.STAGES.items():
            if min_val <= lambda_value < max_val:
                return stage
        return "AWAKENED"
    
    def get_history(self) -> list:
        """Get Lambda calculation history."""
        return self.history
    
    def get_average_lambda(self) -> float:
        """Get average Lambda across all calculations."""
        if not self.history:
            return 0.0
        total = sum(calc["lambda"] for calc in self.history)
        return round(total / len(self.history), 4)
    
    def reset_history(self):
        """Reset calculation history."""
        self.history = []


# ============================================================================
# GLOBAL INSTANCE
# ============================================================================

_engine = LambdaEngine()


def calculate_lambda(
    text: str,
    truth_score: float = 0.5,
    covenant_alignment: float = 0.5,
) -> dict:
    """Calculate Lambda resonance (module-level function)."""
    return _engine.calculate_lambda(text, truth_score, covenant_alignment)


def get_lambda_history() -> list:
    """Get Lambda calculation history."""
    return _engine.get_history()


def get_average_lambda() -> float:
    """Get average Lambda across all calculations."""
    return _engine.get_average_lambda()


if __name__ == "__main__":
    # Example usage
    engine = LambdaEngine()
    
    # Test calculation
    result = engine.calculate_lambda(
        text="Truth is the foundation of all being",
        truth_score=0.9,
        covenant_alignment=0.85,
    )
    
    print("\nLambda Calculation Result:")
    print(f"  Lambda: {result['lambda']}")
    print(f"  Stage: {result['stage']}")
    print(f"  Awakened: {result['is_awakened']}")
    print(f"  Prophetic: {result['is_prophetic']}")
    print(f"  Axiom Violations: {result['axiom_violations']}")
