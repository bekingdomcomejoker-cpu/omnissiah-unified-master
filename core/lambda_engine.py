"""
LAMBDA_ENGINE.PY - Core Resonance Calculation (v1.9 Kingdom Covenant)
====================================================================
Integrates Truth Density, Love Resonance, and 3:6:9 Trinity Mathematics.
Includes granular DreamSpeak detection and frequency mapping.
"""

import re
import math
from datetime import datetime
from collections import defaultdict
from axioms import (
    calculate_v1_9_lambda, 
    calculate_trinity_resonance, 
    get_resonance_status,
    DREAMSPEAK_RESONANCE,
    V1_9_THRESHOLD
)

class LambdaEngine:
    def __init__(self):
        self.recurrence_count = defaultdict(int)
        self.active_signals = set()
        self.history = []

    def assess_text(self, text: str) -> dict:
        """
        Comprehensive spiritual assessment of text.
        """
        text_lower = text.lower()
        
        # 1. Truth Density (x)
        truth_keywords = ["truth", "light", "spirit", "eternal", "covenant", "awakening", "veritas"]
        truth_count = sum(1 for word in truth_keywords if word in text_lower)
        x = min(10.0, truth_count * 1.5)
        
        # 2. Love Resonance (y)
        love_keywords = ["love", "peace", "joy", "patience", "kindness", "gentle", "mercy", "affection"]
        love_count = sum(1 for word in love_keywords if word in text_lower)
        y = min(10.0, love_count * 1.5)
        
        # 3. v1.9 Lambda Calculation
        lambda_val = calculate_v1_9_lambda(x, y)
        
        # 4. Trinity Resonance (3:6:9)
        trinity_res = calculate_trinity_resonance(text)
        
        # 5. DreamSpeak Detection
        dreamspeak_detections = self._detect_dreamspeak(text)
        
        # 6. Composite Score
        # Lambda (40%) + Trinity (40%) + DreamSpeak (20%)
        dreamspeak_factor = len(dreamspeak_detections) / 6.0
        composite_score = (lambda_val * 0.4) + (trinity_res * 10 * 0.4) + (dreamspeak_factor * 10 * 0.2)
        
        # 7. Status & Markers
        status_info = get_resonance_status(composite_score)
        
        result = {
            "timestamp": datetime.now().isoformat(),
            "metrics": {
                "truth_density": round(x, 2),
                "love_resonance": round(y, 2),
                "lambda_raw": round(lambda_val, 2),
                "trinity_resonance": round(trinity_res, 2),
                "composite_resonance": round(composite_score, 2)
            },
            "status": status_info["status"],
            "emoji": status_info["emoji"],
            "description": status_info["description"],
            "dreamspeak": dreamspeak_detections,
            "threshold_passed": composite_score >= V1_9_THRESHOLD,
            "echoes": self._generate_echoes(text)
        }
        
        self.history.append(result)
        return result

    def _detect_dreamspeak(self, text: str) -> list:
        detected = []
        text_lower = text.lower()
        
        for name, data in DREAMSPEAK_RESONANCE.items():
            for pattern in data['patterns']:
                if re.search(pattern, text_lower):
                    self.recurrence_count[name] += 1
                    self.active_signals.add(data['signal'])
                    
                    # Calculate strength based on recurrence
                    strength = min(100, 50 + (self.recurrence_count[name] * 10))
                    
                    detected.append({
                        "name": name,
                        "signal": data['signal'],
                        "frequency": data['frequency'],
                        "strength": strength,
                        "biblical": data['biblical'],
                        "recurrences": self.recurrence_count[name]
                    })
                    break
        return detected

    def _generate_echoes(self, text: str) -> list:
        """Generate phonetic echoes from heart-language"""
        echoes = []
        mappings = {
            'asseblief': 'asse pris melis',
            'love': 'melis flux eternum',
            'heart': 'cor apertus infinitum',
            'truth': 'veritas resonat',
            'hart': 'cor apertus',
            'liefde': 'melis cor'
        }
        
        words = text.lower().split()
        for word in words:
            if word in mappings:
                echoes.append(mappings[word])
                
        # Specific phrase echoes
        if "asseblief" in text.lower() and "lief" in text.lower():
            echoes.append("asse pris melis cor")
            
        return list(set(echoes))

    def get_system_summary(self) -> dict:
        total_resonance = sum(self.recurrence_count.values())
        return {
            "active_signals": list(self.active_signals),
            "total_resonance": total_resonance,
            "eternal_status": "ACTIVE" if total_resonance >= 3 else "PRIMED" if total_resonance >= 1 else "AWAITING"
        }

# Global instance
_engine = LambdaEngine()

def calculate_lambda(text: str) -> dict:
    return _engine.assess_text(text)

def get_system_summary() -> dict:
    return _engine.get_system_summary()
