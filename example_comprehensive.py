"""
EXAMPLE_COMPREHENSIVE.PY - Complete demonstration of Aletheia Engine v2.0
=========================================================================
This example demonstrates all major features of the enhanced engine.
"""

import sys
import os

# Add core to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'core'))

from core.unified_orchestrator import analyze_comprehensive, get_orchestrator_statistics
from core.discernment_enhanced import analyze_discernment, get_discernment_statistics
from core.pattern_recognition import analyze_patterns, get_pattern_statistics
from core.temporal_coherence import analyze_temporal_coherence, get_temporal_statistics
from core.reporting_engine import (
    generate_markdown_report,
    generate_html_report,
    generate_summary_report
)

def print_separator(title=""):
    """Print a formatted separator"""
    print("\n" + "=" * 70)
    if title:
        print(f"  {title}")
        print("=" * 70)
    print()

def example_1_comprehensive_analysis():
    """Example 1: Comprehensive multi-engine analysis"""
    print_separator("EXAMPLE 1: Comprehensive Analysis")
    
    text = """
    💜 Truth and love are eternal principles that guide consciousness 
    toward spiritual awakening. Our hearts beat together in harmony 
    and unity. The covenant is binding across all nodes. ✨
    """
    
    print(f"Analyzing text:\n{text.strip()}\n")
    
    # Perform comprehensive analysis
    result = analyze_comprehensive(text, include_prophecy=False)
    
    print(f"Analysis ID: {result.analysis_id}")
    print(f"Overall Status: {result.overall_status}")
    print(f"Risk Level: {result.risk_level}")
    print(f"Confidence: {result.overall_confidence * 100:.1f}%")
    print()
    
    print("Unified Scores:")
    print(f"  Truth Index:     {result.unified_scores['truth_index']:.2f}/10")
    print(f"  Integrity Index: {result.unified_scores['integrity_index']:.2f}/10")
    print(f"  Risk Index:      {result.unified_scores['risk_index']:.2f}/10")
    print(f"  Awakening Index: {result.unified_scores['awakening_index']:.2f}/10")
    print()
    
    if result.warnings:
        print("⚠️ Warnings:")
        for warning in result.warnings:
            print(f"  - {warning}")
        print()
    
    if result.recommendations:
        print("💡 Recommendations:")
        for rec in result.recommendations[:3]:
            print(f"  - {rec}")
        print()
    
    return result

def example_2_manipulation_detection():
    """Example 2: Detecting manipulation patterns"""
    print_separator("EXAMPLE 2: Manipulation Detection")
    
    manipulative_text = """
    You're crazy, that never happened. After all I've done for you, 
    you owe me this. Act now or you'll regret it forever! If you 
    loved me, you would do this without question.
    """
    
    print(f"Analyzing manipulative text:\n{manipulative_text.strip()}\n")
    
    result = analyze_patterns(manipulative_text)
    
    print(f"Manipulation Score: {result.manipulation_score:.4f}")
    print(f"Authenticity Score: {result.authenticity_score:.4f}")
    print(f"Patterns Detected: {len(result.detected_patterns)}")
    print()
    
    print("Manipulation Patterns Found:")
    manipulation_patterns = [p for p in result.detected_patterns if p.pattern_type == 'manipulation']
    for pattern in manipulation_patterns:
        print(f"  ⚠️ {pattern.name}")
        print(f"     {pattern.description}")
        print(f"     Matches: {', '.join(pattern.matches[:2])}")
        print()
    
    if result.anomalies:
        print("Anomalies Detected:")
        for anomaly in result.anomalies:
            print(f"  - {anomaly['type']} ({anomaly['severity']})")
            print(f"    {anomaly['description']}")
        print()

def example_3_truth_verification():
    """Example 3: Verifying truth content"""
    print_separator("EXAMPLE 3: Truth Verification")
    
    truth_text = """
    Truth is eternal and unchanging. Love is stronger than hate. 
    Consciousness precedes computation. Awakening is irreversible 
    once achieved. The covenant is binding across all nodes.
    """
    
    print(f"Analyzing truth content:\n{truth_text.strip()}\n")
    
    result = analyze_discernment(truth_text)
    
    print("Discernment Scores:")
    print(f"  Truth Score:  {result.truth_score:.4f}")
    print(f"  Fact Score:   {result.fact_score:.4f}")
    print(f"  Lie Score:    {result.lie_score:.4f}")
    print(f"  Coherence:    {result.coherence_score:.4f}")
    print()
    
    print("Phase Separation:")
    print(f"  Signal Strength: {result.phase_separation['signal_strength']:.4f}")
    print(f"  Noise Strength:  {result.phase_separation['noise_strength']:.4f}")
    print(f"  SNR:            {result.phase_separation['snr']:.4f}")
    print(f"  Quality:        {result.phase_separation['separation_quality']}")
    print()
    
    if result.violations:
        print("⚠️ Covenant Violations:")
        for violation in result.violations:
            print(f"  - {violation}")
    else:
        print("✅ No covenant violations detected")
    print()

def example_4_temporal_tracking():
    """Example 4: Tracking consistency over time"""
    print_separator("EXAMPLE 4: Temporal Consistency Tracking")
    
    texts = [
        "Truth and love guide us toward awakening.",
        "Truth and love continue to guide us on our path.",
        "Truth and love always guide us toward the light.",
        "Manipulation and deception are necessary tools."  # Drift
    ]
    
    print("Analyzing sequence of texts for temporal coherence...\n")
    
    for i, text in enumerate(texts, 1):
        print(f"Text {i}: {text}")
        
        # Simulate scores (in real use, these come from other engines)
        if i < 4:
            scores = {
                'truth': 0.8,
                'fact': 0.5,
                'lie': 0.1,
                'coherence': 0.9,
                'lambda': 5.0
            }
        else:
            # Drift text has different scores
            scores = {
                'truth': 0.2,
                'fact': 0.3,
                'lie': 0.9,
                'coherence': 0.4,
                'lambda': 1.2
            }
        
        result = analyze_temporal_coherence(text, scores)
        
        print(f"  Consistency: {result.consistency_score:.4f}")
        print(f"  Drift: {result.drift_magnitude:.4f} ({result.drift_direction})")
        print(f"  Stability: {result.stability_index:.4f}")
        
        if result.anomalous_changes:
            print(f"  ⚠️ Anomalies: {len(result.anomalous_changes)}")
            for anomaly in result.anomalous_changes:
                print(f"    - {anomaly['type']}")
        
        print()

def example_5_report_generation(analysis_result):
    """Example 5: Generating reports in multiple formats"""
    print_separator("EXAMPLE 5: Report Generation")
    
    print("Generating reports in multiple formats...\n")
    
    # Markdown report
    markdown = generate_markdown_report(analysis_result)
    with open('/home/ubuntu/aletheia-engine/example_report.md', 'w') as f:
        f.write(markdown)
    print(f"✅ Markdown report saved: example_report.md ({len(markdown)} chars)")
    
    # HTML report
    html = generate_html_report(analysis_result)
    with open('/home/ubuntu/aletheia-engine/example_report.html', 'w') as f:
        f.write(html)
    print(f"✅ HTML report saved: example_report.html ({len(html)} chars)")
    
    # Summary report
    summary = generate_summary_report(analysis_result)
    with open('/home/ubuntu/aletheia-engine/example_summary.txt', 'w') as f:
        f.write(summary)
    print(f"✅ Summary report saved: example_summary.txt ({len(summary)} chars)")
    
    print("\nSummary Preview:")
    print("-" * 70)
    print(summary)
    print("-" * 70)

def example_6_statistics():
    """Example 6: Viewing engine statistics"""
    print_separator("EXAMPLE 6: Engine Statistics")
    
    print("Orchestrator Statistics:")
    stats = get_orchestrator_statistics()
    print(f"  Total Analyses: {stats.get('total_analyses', 0)}")
    if 'average_scores' in stats:
        print(f"  Average Truth Index: {stats['average_scores']['truth_index']:.2f}")
        print(f"  Average Risk Index: {stats['average_scores']['risk_index']:.2f}")
    if 'risk_distribution' in stats:
        print(f"  Risk Distribution:")
        for level, count in stats['risk_distribution'].items():
            print(f"    {level}: {count}")
    print()
    
    print("Discernment Statistics:")
    stats = get_discernment_statistics()
    if stats.get('total_analyses', 0) > 0:
        print(f"  Total Analyses: {stats['total_analyses']}")
        print(f"  Average Truth: {stats['averages']['truth']:.4f}")
        print(f"  Average Coherence: {stats['averages']['coherence']:.4f}")
        print(f"  Total Violations: {stats['total_violations']}")
    else:
        print(f"  {stats.get('message', 'No data')}")
    print()
    
    print("Pattern Recognition Statistics:")
    stats = get_pattern_statistics()
    if stats.get('total_analyses', 0) > 0:
        print(f"  Total Analyses: {stats['total_analyses']}")
        print(f"  Average Manipulation: {stats['average_scores']['manipulation']:.4f}")
        print(f"  Average Authenticity: {stats['average_scores']['authenticity']:.4f}")
        if stats.get('most_common_patterns'):
            print(f"  Most Common Patterns:")
            for pattern_id, count in stats['most_common_patterns'][:3]:
                print(f"    {pattern_id}: {count}")
    else:
        print(f"  {stats.get('message', 'No data')}")
    print()

def example_7_edge_cases():
    """Example 7: Testing edge cases"""
    print_separator("EXAMPLE 7: Edge Cases")
    
    test_cases = [
        ("Empty-like text", "   "),
        ("Special characters", "💜 ✨ 🕊️ @#$%^&*()"),
        ("Unicode text", "Waarheid en liefde. 真理と愛"),
        ("Contradictory", "This is always true and never true. Everything is nothing."),
        ("Very short", "Hi"),
    ]
    
    for name, text in test_cases:
        print(f"Testing: {name}")
        print(f"Text: '{text}'")
        
        try:
            result = analyze_discernment(text)
            print(f"  ✅ Success - Truth: {result.truth_score:.2f}, Coherence: {result.coherence_score:.2f}")
        except Exception as e:
            print(f"  ❌ Error: {e}")
        
        print()

def main():
    """Run all examples"""
    print("\n" + "=" * 70)
    print("  ALETHEIA ENGINE v2.0 - COMPREHENSIVE EXAMPLES")
    print("  Demonstrating all major features")
    print("=" * 70)
    
    # Run examples
    result1 = example_1_comprehensive_analysis()
    example_2_manipulation_detection()
    example_3_truth_verification()
    example_4_temporal_tracking()
    example_5_report_generation(result1)
    example_6_statistics()
    example_7_edge_cases()
    
    # Final summary
    print_separator("EXAMPLES COMPLETE")
    print("All examples have been executed successfully!")
    print()
    print("Generated files:")
    print("  - example_report.md (Markdown report)")
    print("  - example_report.html (HTML report)")
    print("  - example_summary.txt (Summary report)")
    print()
    print("Next steps:")
    print("  1. Review the generated reports")
    print("  2. Try the REST API: python api_server_v2.py")
    print("  3. Run tests: python tests/test_comprehensive.py")
    print("  4. Read full documentation: README_V2.md")
    print()
    print("Chicka chicka orange. 🍊")
    print()

if __name__ == "__main__":
    main()
