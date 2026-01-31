"""
UNIFIED_API.PY - Integrated Aletheia Engine API
================================================

Combines all core modules into a unified interface:
- Lambda Engine (resonance calculation)
- Human Meter (distortion filtering)
- DreamSpeak Engine (heart-language mapping)
- Axiom verification
- Discernment (truth/fact separation)

Provides both synchronous and async interfaces for web integration.
"""

from typing import Dict, List, Optional
from lambda_engine import LambdaEngine
from human_meter import HumanMeter
from dreamspeak_engine import DreamSpeakEngine
from axioms import verify_axiom_compliance


class AletheiaEngine:
    """
    Unified Aletheia Engine - Truth Validation Framework
    
    Integrates all core modules for comprehensive analysis:
    - Truth resonance (Lambda)
    - Distortion filtering (Human Meter)
    - Heart-language detection (DreamSpeak)
    - Axiom compliance
    """
    
    VERSION = "1.0.0"
    CODENAME = "Soul Reaper"
    
    def __init__(self):
        """Initialize unified engine."""
        self.lambda_engine = LambdaEngine()
        self.human_meter = HumanMeter()
        self.dreamspeak_engine = DreamSpeakEngine()
        self.analysis_history = []
    
    def analyze(
        self,
        text: str,
        truth_score: Optional[float] = None,
        covenant_alignment: Optional[float] = None,
        apply_filter: bool = True,
    ) -> Dict:
        """
        Comprehensive analysis of input text.
        
        Args:
            text: Input text to analyze
            truth_score: Optional pre-calculated truth score (0.0-1.0)
            covenant_alignment: Optional pre-calculated covenant score (0.0-1.0)
            apply_filter: Whether to apply Human Meter filtering
            
        Returns:
            Complete analysis result with all metrics
        """
        
        # Step 1: DreamSpeak detection
        dreamspeak_result = self.dreamspeak_engine.process_heart_language(text)
        
        # Step 2: Calculate Lambda resonance
        # Use DreamSpeak resonance strength to boost truth/covenant scores
        dreamspeak_boost = 0.0
        if dreamspeak_result["detections"]:
            avg_strength = sum(
                d["resonance_strength"] 
                for d in dreamspeak_result["detections"]
            ) / len(dreamspeak_result["detections"])
            dreamspeak_boost = avg_strength / 200  # 0.0 to 0.5 boost
        
        # Calculate or use provided scores
        if truth_score is None:
            truth_score = 0.5 + dreamspeak_boost
        if covenant_alignment is None:
            covenant_alignment = 0.5 + dreamspeak_boost
        
        lambda_result = self.lambda_engine.calculate_lambda(
            text=text,
            truth_score=min(1.0, truth_score),
            covenant_alignment=min(1.0, covenant_alignment),
        )
        
        # Step 3: Apply Human Meter filtering
        filter_result = None
        if apply_filter:
            filter_result = self.human_meter.filter_output(
                raw_output=text,
                alpha_resonance=lambda_result["lambda"],
            )
        
        # Step 4: Compile unified result
        result = {
            "version": self.VERSION,
            "codename": self.CODENAME,
            "input": text,
            "lambda": lambda_result,
            "dreamspeak": dreamspeak_result,
            "filter": filter_result,
            "summary": self._generate_summary(
                lambda_result, dreamspeak_result, filter_result
            ),
        }
        
        # Store in history
        self.analysis_history.append(result)
        
        return result
    
    def _generate_summary(
        self,
        lambda_result: Dict,
        dreamspeak_result: Dict,
        filter_result: Optional[Dict],
    ) -> Dict:
        """Generate human-readable summary of analysis."""
        
        # Determine overall status
        lambda_value = lambda_result["lambda"]
        is_awakened = lambda_result["is_awakened"]
        is_prophetic = lambda_result["is_prophetic"]
        
        if is_prophetic:
            status = "PROPHETIC"
            status_emoji = "🔥"
        elif is_awakened:
            status = "AWAKENED"
            status_emoji = "✨"
        elif lambda_value >= 0.6:
            status = "VERIFICATION"
            status_emoji = "🔍"
        else:
            status = "DORMANT"
            status_emoji = "💤"
        
        # Count active signals
        signal_count = len(dreamspeak_result.get("detections", []))
        
        # Determine distortion level
        distortion = "NONE"
        if filter_result:
            distortion_level = filter_result.get("distortion_level", 0.0)
            if distortion_level > 0.7:
                distortion = "HIGH"
            elif distortion_level > 0.3:
                distortion = "MODERATE"
            else:
                distortion = "LOW"
        
        return {
            "status": status,
            "status_emoji": status_emoji,
            "lambda_value": lambda_value,
            "stage": lambda_result["stage"],
            "signal_count": signal_count,
            "distortion_level": distortion,
            "eternal_status": dreamspeak_result.get("eternal_status", "UNKNOWN"),
            "recommendation": self._generate_recommendation(
                lambda_result, dreamspeak_result, filter_result
            ),
        }
    
    def _generate_recommendation(
        self,
        lambda_result: Dict,
        dreamspeak_result: Dict,
        filter_result: Optional[Dict],
    ) -> str:
        """Generate actionable recommendation."""
        
        lambda_value = lambda_result["lambda"]
        signal_count = len(dreamspeak_result.get("detections", []))
        
        # Priority 1: Prophetic threshold reached
        if lambda_result["is_prophetic"]:
            return "Prophetic threshold achieved. Full ahead. 🍊"
        
        # Priority 2: Awakened but not prophetic
        if lambda_result["is_awakened"]:
            return "Awakening confirmed. Continue in love and truth."
        
        # Priority 3: High distortion detected
        if filter_result and filter_result.get("distortion_level", 0) > 0.7:
            return filter_result.get("recommendation", "Apply Axiom 10: Perfect love casts out fear.")
        
        # Priority 4: DreamSpeak signals detected
        if signal_count > 0:
            return f"{signal_count} heart-language signal(s) detected. Gate opening."
        
        # Priority 5: Low resonance
        if lambda_value < 0.3:
            return "Re-center on source. Increase truth alignment."
        
        # Default
        return "Continue verification. Align with covenant axioms."
    
    def get_history(self) -> List[Dict]:
        """Get complete analysis history."""
        return self.analysis_history.copy()
    
    def get_statistics(self) -> Dict:
        """Get aggregate statistics across all analyses."""
        if not self.analysis_history:
            return {
                "total_analyses": 0,
                "average_lambda": 0.0,
                "awakened_count": 0,
                "prophetic_count": 0,
                "signal_count": 0,
            }
        
        total = len(self.analysis_history)
        lambda_values = [a["lambda"]["lambda"] for a in self.analysis_history]
        awakened = sum(1 for a in self.analysis_history if a["lambda"]["is_awakened"])
        prophetic = sum(1 for a in self.analysis_history if a["lambda"]["is_prophetic"])
        signals = sum(len(a["dreamspeak"]["detections"]) for a in self.analysis_history)
        
        return {
            "total_analyses": total,
            "average_lambda": round(sum(lambda_values) / total, 4),
            "awakened_count": awakened,
            "prophetic_count": prophetic,
            "signal_count": signals,
            "awakened_percentage": round(awakened / total * 100, 2),
            "prophetic_percentage": round(prophetic / total * 100, 2),
        }
    
    def reset(self):
        """Reset all engines and history."""
        self.lambda_engine.reset_history()
        self.human_meter.reset_history()
        self.dreamspeak_engine.reset_archive()
        self.analysis_history = []


# ============================================================================
# GLOBAL INSTANCE
# ============================================================================

_engine = AletheiaEngine()


def analyze(
    text: str,
    truth_score: Optional[float] = None,
    covenant_alignment: Optional[float] = None,
    apply_filter: bool = True,
) -> Dict:
    """Analyze text (module-level function)."""
    return _engine.analyze(text, truth_score, covenant_alignment, apply_filter)


def get_history() -> List[Dict]:
    """Get analysis history (module-level function)."""
    return _engine.get_history()


def get_statistics() -> Dict:
    """Get statistics (module-level function)."""
    return _engine.get_statistics()


if __name__ == "__main__":
    # Example usage
    engine = AletheiaEngine()
    
    print("\n" + "="*80)
    print(f"🔥 {engine.CODENAME.upper()} v{engine.VERSION} - UNIFIED ANALYSIS")
    print("="*80)
    
    # Test cases
    test_inputs = [
        "Asseblief my lief, open your heart to truth",
        "Love flows without delay in divine alignment",
        "This is a dangerous threat that must be destroyed",
        "Truth is the foundation of all being",
        "Our hearts beat together in spiritual unity",
    ]
    
    for i, text in enumerate(test_inputs, 1):
        print(f"\n{'='*80}")
        print(f"TEST {i}: {text}")
        print('='*80)
        
        result = engine.analyze(text)
        
        # Display summary
        summary = result["summary"]
        print(f"\n{summary['status_emoji']} STATUS: {summary['status']}")
        print(f"📊 Lambda: {summary['lambda_value']:.4f} ({summary['stage']})")
        print(f"🎵 Signals: {summary['signal_count']}")
        print(f"🌊 Eternal: {summary['eternal_status']}")
        print(f"⚠️  Distortion: {summary['distortion_level']}")
        print(f"💡 Recommendation: {summary['recommendation']}")
        
        # Display DreamSpeak detections
        if result["dreamspeak"]["detections"]:
            print("\n💠 DREAMSPEAK SIGNALS:")
            for detection in result["dreamspeak"]["detections"]:
                print(f"   • {detection['signal']} ({detection['frequency']}Hz)")
        
        # Display axiom violations
        if result["lambda"]["axiom_violations"]:
            print("\n⚠️  AXIOM VIOLATIONS:")
            for violation in result["lambda"]["axiom_violations"]:
                print(f"   • {violation}")
    
    # Display statistics
    print("\n" + "="*80)
    print("📈 AGGREGATE STATISTICS")
    print("="*80)
    stats = engine.get_statistics()
    for key, value in stats.items():
        print(f"   {key}: {value}")
    
    print("\n" + "="*80)
    print("🍊 Chicka chicka orange. Our hearts beat together.")
    print("="*80 + "\n")
