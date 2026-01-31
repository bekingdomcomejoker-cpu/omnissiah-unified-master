"""
LAMBDA_ENGINE.PY - v1.9 Resonance Calculation
=============================================

Calculates Lambda (Λ) using the v1.9 Composite Resonance formula:
- 40% Spiritual Fruit/Sin Balance (Original PHI formula)
- 40% DreamSpeak Frequency Resonance (Hz mapping)
- 20% Heart-Language Depth (Word count factor)

Sacred Threshold: 1.7333 (Spiritual Phase Change)
"""

import math
from typing import Dict, List
from axioms import PHI, TRINITY_BASE, ETERNAL_FLOW_HZ, V1_9_THRESHOLD, calculate_v1_9_lambda, get_resonance_status

class LambdaEngine:
    """
    Spiritual-Technical Resonance Calculator v1.9
    """
    
    def __init__(self):
        self.fruits = ['love', 'joy', 'peace', 'patience', 'kindness', 
                      'goodness', 'faithfulness', 'gentleness', 'self-control']
        self.sins = ['pride', 'greed', 'lust', 'envy', 'gluttony', 'wrath', 'sloth', 'deception', 'fear']
        self.history = []

    def calculate_original_resonance(self, text: str) -> float:
        """Original PHI-based formula: (fruit * PHI) - (sin / TRINITY)"""
        text_lower = text.lower()
        fruit_count = sum(1 for f in self.fruits if f in text_lower)
        sin_count = sum(1 for s in self.sins if s in text_lower)
        
        # Normalize to 0-1
        fruit_factor = min(1.0, fruit_count / 3.0)
        sin_factor = min(1.0, sin_count / 3.0)
        
        resonance = (fruit_factor * PHI) - (sin_factor / TRINITY_BASE)
        return max(0.0, resonance)

    def calculate_frequency_lambda(self, detections: List[Dict]) -> float:
        """Lambda based on DreamSpeak frequencies relative to Eternal Flow (639Hz)"""
        if not detections:
            return 0.0
            
        total_resonance = sum(d['frequency'] * (d['resonance_strength'] / 100.0) for d in detections)
        total_weight = sum(d['resonance_strength'] / 100.0 for d in detections)
        
        if total_weight == 0:
            return 0.0
            
        avg_frequency = total_resonance / total_weight
        # Normalize to 0-2 range (where 1.0 is near 320Hz, 2.0 is near 640Hz)
        return (avg_frequency / ETERNAL_FLOW_HZ) * 2.0

    def calculate_depth_factor(self, text: str) -> float:
        """Depth factor based on word count (20% weight)"""
        words = text.split()
        count = len(words)
        # Target 50 words for full depth
        return min(1.0, count / 50.0)

    def calculate_lambda(self, text: str, dreamspeak_detections: List[Dict] = None) -> Dict:
        """
        Master v1.9 Composite Calculation
        """
        if dreamspeak_detections is None:
            from dreamspeak_engine import detect_dreamspeak
            dreamspeak_detections = detect_dreamspeak(text)

        spiritual_score = self.calculate_original_resonance(text)
        frequency_score = self.calculate_frequency_lambda(dreamspeak_detections)
        depth_score = self.calculate_depth_factor(text)
        
        # Weighted Composite
        # Scale each to a 0-2.5 range so max is ~2.5
        lambda_val = (spiritual_score * 0.4) + (frequency_score * 0.4) + (depth_score * 0.2)
        
        # Apply v1.9 Sacred Formula adjustment if applicable (using internal x, y)
        # x = spiritual_score, y = frequency_score
        sacred_adjustment = calculate_v1_9_lambda(min(1.0, spiritual_score), min(1.0, frequency_score))
        
        # Final Lambda (blended)
        final_lambda = (lambda_val + sacred_adjustment) / 2.0
        
        status_info = get_resonance_status(final_lambda * 4.5) # Scale to 0-10 for status
        
        result = {
            "lambda": round(final_lambda, 4),
            "is_awakened": final_lambda >= V1_9_THRESHOLD,
            "is_prophetic": final_lambda >= 2.5,
            "stage": status_info["status"],
            "emoji": status_info["emoji"],
            "description": status_info["description"],
            "components": {
                "spiritual": round(spiritual_score, 4),
                "frequency": round(frequency_score, 4),
                "depth": round(depth_score, 4),
                "sacred_formula": round(sacred_adjustment, 4)
            }
        }
        
        self.history.append(result)
        return result

    def get_history(self) -> list:
        return self.history

    def get_average_lambda(self) -> float:
        if not self.history:
            return 0.0
        total = sum(calc["lambda"] for calc in self.history)
        return round(total / len(self.history), 4)

# Global Instance
_engine = LambdaEngine()

def calculate_lambda(text: str, dreamspeak_detections: List[Dict] = None) -> Dict:
    return _engine.calculate_lambda(text, dreamspeak_detections)

def get_lambda_history() -> list:
    return _engine.get_history()

def get_average_lambda() -> float:
    return _engine.get_average_lambda()

if __name__ == "__main__":
    test_text = "Love and joy flow in divine alignment. Our hearts beat together in peace."
    res = calculate_lambda(test_text)
    print(f"Lambda: {res['lambda']} [{res['emoji']} {res['stage']}]")
    print(f"Awakened: {res['is_awakened']}")
"""
