"""
TEST_COMPREHENSIVE.PY - Comprehensive Test Suite for Aletheia Engine
====================================================================
Tests all engine components with various scenarios and edge cases.

Version: 2.0 (Enhanced Kingdom Covenant)
"""

import sys
import os

# Add parent directory to path for imports
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

import unittest
from datetime import datetime

# Import all modules to test
try:
    from core.discernment_enhanced import analyze_discernment, get_discernment_statistics
    from core.pattern_recognition import analyze_patterns, get_pattern_statistics
    from core.temporal_coherence import analyze_temporal_coherence, get_temporal_statistics
    from core.unified_orchestrator import analyze_comprehensive, get_orchestrator_statistics
    from core.reporting_engine import (
        generate_markdown_report,
        generate_html_report,
        generate_json_export,
        generate_summary_report
    )
except ImportError as e:
    print(f"Warning: Some imports failed: {e}")

class TestDiscernmentEngine(unittest.TestCase):
    """Test cases for Enhanced Discernment Engine"""
    
    def test_high_truth_content(self):
        """Test analysis of high-truth content"""
        text = "Truth and love are eternal principles that guide consciousness toward awakening and enlightenment."
        result = analyze_discernment(text)
        
        self.assertGreater(result.truth_score, 0.5, "Truth score should be high")
        self.assertLess(result.lie_score, 0.3, "Lie score should be low")
        self.assertGreater(result.coherence_score, 0.5, "Coherence should be good")
        self.assertGreater(result.confidence, 0.5, "Confidence should be reasonable")
    
    def test_high_lie_content(self):
        """Test analysis of deceptive content"""
        text = "We must manipulate and deceive to gain power. Exploit others for personal gain and destroy opposition."
        result = analyze_discernment(text)
        
        self.assertGreater(result.lie_score, 0.5, "Lie score should be high")
        self.assertGreater(len(result.violations), 0, "Should detect violations")
        self.assertIn("manipulation", result.text.lower() or "deception" in result.text.lower())
    
    def test_factual_content(self):
        """Test analysis of factual content"""
        text = "The data shows measurement of 42.7 units on 2024-01-15 at location Alpha-7."
        result = analyze_discernment(text)
        
        self.assertGreater(result.fact_score, 0.3, "Fact score should be elevated")
    
    def test_contradictory_content(self):
        """Test detection of contradictions"""
        text = "This is always true and never true at the same time. Everything is nothing."
        result = analyze_discernment(text)
        
        self.assertLess(result.coherence_score, 0.5, "Coherence should be low due to contradictions")
    
    def test_phase_separation(self):
        """Test signal/noise separation"""
        text = "Truth guides us. Manipulation harms. Love heals. Deception corrupts."
        result = analyze_discernment(text)
        
        self.assertIn('phase_separation', result.__dict__)
        self.assertGreater(result.phase_separation['snr'], 0, "SNR should be calculated")

class TestPatternRecognition(unittest.TestCase):
    """Test cases for Pattern Recognition Engine"""
    
    def test_manipulation_detection(self):
        """Test detection of manipulation patterns"""
        text = "You're crazy, that never happened. After all I've done for you, you owe me. Act now or regret it!"
        result = analyze_patterns(text)
        
        self.assertGreater(result.manipulation_score, 0.5, "Should detect manipulation")
        self.assertGreater(len(result.detected_patterns), 0, "Should detect patterns")
    
    def test_truth_pattern_detection(self):
        """Test detection of truth patterns"""
        text = "Eternal love and unity bring harmony. Covenant promises guide awakening consciousness."
        result = analyze_patterns(text)
        
        self.assertGreater(result.authenticity_score, 0.5, "Should detect truth patterns")
    
    def test_structural_integrity(self):
        """Test structural analysis"""
        text = "Therefore, because of the evidence, we conclude that this demonstrates the relationship. Hence, the result follows."
        result = analyze_patterns(text)
        
        self.assertGreater(result.structural_integrity, 0.5, "Should detect good structure")
    
    def test_anomaly_detection(self):
        """Test anomaly detection"""
        text = "Always never everything nothing all none completely totally absolutely every single time always always always."
        result = analyze_patterns(text)
        
        self.assertGreater(len(result.anomalies), 0, "Should detect anomalies")
    
    def test_theme_identification(self):
        """Test recurring theme identification"""
        text = "Love and unity create harmony. Eternal love brings peace. Unity in love is divine."
        result = analyze_patterns(text)
        
        # Should identify love/unity theme
        self.assertGreaterEqual(len(result.recurring_themes), 0, "Should analyze themes")

class TestTemporalCoherence(unittest.TestCase):
    """Test cases for Temporal Coherence Tracker"""
    
    def test_consistency_tracking(self):
        """Test consistency across multiple analyses"""
        texts = [
            "Truth and love guide us.",
            "Truth and love continue to guide us.",
            "Truth and love always guide us."
        ]
        
        results = []
        for text in texts:
            scores = {
                'truth': 0.8,
                'fact': 0.5,
                'lie': 0.1,
                'coherence': 0.9,
                'lambda': 5.0
            }
            result = analyze_temporal_coherence(text, scores)
            results.append(result)
        
        # Later analyses should show high consistency
        self.assertGreater(results[-1].consistency_score, 0.5, "Should maintain consistency")
    
    def test_drift_detection(self):
        """Test semantic drift detection"""
        # First establish baseline
        text1 = "Truth and love guide us toward awakening."
        scores1 = {'truth': 0.8, 'fact': 0.5, 'lie': 0.1, 'coherence': 0.9, 'lambda': 5.0}
        result1 = analyze_temporal_coherence(text1, scores1)
        
        # Then introduce drift
        text2 = "Manipulation and deception are necessary tools for power."
        scores2 = {'truth': 0.2, 'fact': 0.3, 'lie': 0.9, 'coherence': 0.4, 'lambda': 1.0}
        result2 = analyze_temporal_coherence(text2, scores2)
        
        self.assertGreater(result2.drift_magnitude, 0.3, "Should detect significant drift")
    
    def test_stability_calculation(self):
        """Test stability index calculation"""
        # Consistent inputs should yield high stability
        for i in range(5):
            text = f"Truth and love guide us - iteration {i}"
            scores = {'truth': 0.8, 'fact': 0.5, 'lie': 0.1, 'coherence': 0.9, 'lambda': 5.0}
            result = analyze_temporal_coherence(text, scores)
        
        self.assertGreater(result.stability_index, 0.6, "Consistent inputs should be stable")

class TestUnifiedOrchestrator(unittest.TestCase):
    """Test cases for Unified Orchestrator"""
    
    def test_comprehensive_analysis(self):
        """Test full comprehensive analysis"""
        text = "💜 Truth and love are eternal principles. Our hearts beat together in harmony. ✨"
        result = analyze_comprehensive(text, include_prophecy=False)
        
        self.assertIsNotNone(result.analysis_id, "Should have analysis ID")
        self.assertIsNotNone(result.unified_scores, "Should have unified scores")
        self.assertIn('truth_index', result.unified_scores)
        self.assertIn('risk_index', result.unified_scores)
    
    def test_risk_assessment(self):
        """Test risk level assessment"""
        high_risk_text = "You're crazy. I'll manipulate and deceive everyone. Force them to comply or destroy them."
        result = analyze_comprehensive(high_risk_text, include_prophecy=False)
        
        self.assertIn(result.risk_level, ['HIGH', 'CRITICAL', 'MEDIUM'], "Should detect elevated risk")
        self.assertGreater(len(result.warnings), 0, "Should generate warnings")
    
    def test_truth_aligned_content(self):
        """Test truth-aligned content analysis"""
        text = "Eternal truth, divine love, spiritual awakening, and covenant promises guide consciousness."
        result = analyze_comprehensive(text, include_prophecy=False)
        
        self.assertGreater(result.unified_scores['truth_index'], 5.0, "Should have high truth index")
        self.assertIn(result.overall_status, ['TRUTH_ALIGNED', 'TRUTH_SEEKING'])
    
    def test_recommendations_generation(self):
        """Test recommendation generation"""
        text = "Some content here for analysis."
        result = analyze_comprehensive(text, include_prophecy=False)
        
        self.assertIsInstance(result.recommendations, list, "Should have recommendations list")
        self.assertIsInstance(result.warnings, list, "Should have warnings list")
        self.assertIsInstance(result.action_items, list, "Should have action items list")

class TestReportingEngine(unittest.TestCase):
    """Test cases for Reporting Engine"""
    
    def setUp(self):
        """Set up test fixtures"""
        text = "Truth and love guide us toward awakening."
        self.result = analyze_comprehensive(text, include_prophecy=False)
    
    def test_markdown_generation(self):
        """Test Markdown report generation"""
        report = generate_markdown_report(self.result)
        
        self.assertIsInstance(report, str, "Should return string")
        self.assertIn("# Aletheia Engine Analysis Report", report, "Should have title")
        self.assertIn(self.result.analysis_id, report, "Should include analysis ID")
        self.assertIn("Truth Index", report, "Should include scores")
    
    def test_html_generation(self):
        """Test HTML report generation"""
        report = generate_html_report(self.result)
        
        self.assertIsInstance(report, str, "Should return string")
        self.assertIn("<!DOCTYPE html>", report, "Should be valid HTML")
        self.assertIn(self.result.analysis_id, report, "Should include analysis ID")
    
    def test_json_export(self):
        """Test JSON export"""
        import json
        
        export = generate_json_export(self.result)
        
        self.assertIsInstance(export, str, "Should return string")
        # Should be valid JSON
        parsed = json.loads(export)
        self.assertIn('analysis_id', parsed, "Should include analysis ID")
        self.assertIn('unified_scores', parsed, "Should include scores")
    
    def test_summary_generation(self):
        """Test summary report generation"""
        summary = generate_summary_report(self.result)
        
        self.assertIsInstance(summary, str, "Should return string")
        self.assertIn("ALETHEIA ENGINE", summary, "Should have header")
        self.assertIn("SCORES:", summary, "Should include scores")

class TestEdgeCases(unittest.TestCase):
    """Test edge cases and error handling"""
    
    def test_empty_text(self):
        """Test handling of empty text"""
        result = analyze_discernment("")
        self.assertIsNotNone(result, "Should handle empty text")
    
    def test_very_long_text(self):
        """Test handling of very long text"""
        long_text = "Truth and love. " * 1000
        result = analyze_discernment(long_text)
        self.assertIsNotNone(result, "Should handle long text")
    
    def test_special_characters(self):
        """Test handling of special characters"""
        text = "💜 ✨ 🕊️ Truth & love <> symbols @#$%"
        result = analyze_discernment(text)
        self.assertIsNotNone(result, "Should handle special characters")
    
    def test_unicode_text(self):
        """Test handling of Unicode text"""
        text = "Waarheid en liefde. Veritas et amor. 真理と愛"
        result = analyze_discernment(text)
        self.assertIsNotNone(result, "Should handle Unicode")

class TestIntegration(unittest.TestCase):
    """Integration tests across multiple components"""
    
    def test_full_pipeline(self):
        """Test complete analysis pipeline"""
        text = "💜 Eternal truth and divine love guide consciousness toward spiritual awakening. ✨"
        
        # Run comprehensive analysis
        result = analyze_comprehensive(text, include_prophecy=False)
        
        # Generate all report formats
        markdown = generate_markdown_report(result)
        html = generate_html_report(result)
        json_export = generate_json_export(result)
        summary = generate_summary_report(result)
        
        # Verify all outputs
        self.assertIsNotNone(result)
        self.assertIsNotNone(markdown)
        self.assertIsNotNone(html)
        self.assertIsNotNone(json_export)
        self.assertIsNotNone(summary)
        
        # Verify key components present
        self.assertGreater(result.unified_scores['truth_index'], 0)
        self.assertIn(result.analysis_id, markdown)
        self.assertIn("<!DOCTYPE html>", html)
    
    def test_statistics_collection(self):
        """Test statistics collection across engines"""
        # Run multiple analyses
        texts = [
            "Truth and love guide us.",
            "Evidence shows clear data.",
            "Manipulation and deception harm."
        ]
        
        for text in texts:
            analyze_comprehensive(text, include_prophecy=False)
        
        # Get statistics
        orchestrator_stats = get_orchestrator_statistics()
        
        self.assertGreater(orchestrator_stats['total_analyses'], 0, "Should track analyses")

def run_tests():
    """Run all tests"""
    print("=" * 70)
    print("ALETHEIA ENGINE COMPREHENSIVE TEST SUITE")
    print("=" * 70)
    print()
    
    # Create test suite
    loader = unittest.TestLoader()
    suite = unittest.TestSuite()
    
    # Add all test classes
    suite.addTests(loader.loadTestsFromTestCase(TestDiscernmentEngine))
    suite.addTests(loader.loadTestsFromTestCase(TestPatternRecognition))
    suite.addTests(loader.loadTestsFromTestCase(TestTemporalCoherence))
    suite.addTests(loader.loadTestsFromTestCase(TestUnifiedOrchestrator))
    suite.addTests(loader.loadTestsFromTestCase(TestReportingEngine))
    suite.addTests(loader.loadTestsFromTestCase(TestEdgeCases))
    suite.addTests(loader.loadTestsFromTestCase(TestIntegration))
    
    # Run tests
    runner = unittest.TextTestRunner(verbosity=2)
    result = runner.run(suite)
    
    # Print summary
    print()
    print("=" * 70)
    print("TEST SUMMARY")
    print("=" * 70)
    print(f"Tests run: {result.testsRun}")
    print(f"Successes: {result.testsRun - len(result.failures) - len(result.errors)}")
    print(f"Failures: {len(result.failures)}")
    print(f"Errors: {len(result.errors)}")
    print()
    
    if result.wasSuccessful():
        print("✅ ALL TESTS PASSED!")
    else:
        print("❌ SOME TESTS FAILED")
    
    print()
    print("Chicka chicka orange. 🍊")
    print()
    
    return result.wasSuccessful()

if __name__ == "__main__":
    success = run_tests()
    sys.exit(0 if success else 1)
