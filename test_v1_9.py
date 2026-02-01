import sys
import os

# Add core directory to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'core'))

from unified_api import perform_unified_analysis

test_text = "💜 Violet light tears - Our hearts beat together asseblief my lief ✨ 🕊️"
res = perform_unified_analysis(test_text)

print("\n--- V1.9 ENGINE TEST ---")
print(f"Status: {res['assessment']['status']} {res['assessment']['emoji']}")
print(f"Lambda: {res['assessment']['metrics']['composite_resonance']}")
print(f"Threshold Passed: {res['assessment']['threshold_passed']}")
print(f"Throne Access: {res['throne_room']['success']}")
if res['prophecy']:
    print(f"Prophecy: {res['prophecy']['prophecy']}")
    print(f"Experts: {res['prophecy']['experts_consulted']}")
print(f"Echoes: {res['assessment']['echoes']}")
print("------------------------")
