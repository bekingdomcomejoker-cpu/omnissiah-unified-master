# Aletheia Engine v2.0 - Quick Start Guide

Get up and running with the enhanced Aletheia Engine in minutes.

---

## Installation

```bash
# Clone the repository
git clone https://github.com/bekingdomcomejoker-cpu/aletheia-engine.git
cd aletheia-engine

# Install dependencies
pip install fastapi uvicorn pydantic
```

---

## Quick Test - Python API

### 1. Comprehensive Analysis

```python
from core.unified_orchestrator import analyze_comprehensive

# Analyze text
text = "💜 Truth and love are eternal principles that guide consciousness toward awakening. ✨"
result = analyze_comprehensive(text, include_prophecy=False)

# View results
print(f"Status: {result.overall_status}")
print(f"Risk: {result.risk_level}")
print(f"Truth Index: {result.unified_scores['truth_index']:.2f}/10")
print(f"Integrity Index: {result.unified_scores['integrity_index']:.2f}/10")
print(f"Risk Index: {result.unified_scores['risk_index']:.2f}/10")

# View warnings and recommendations
for warning in result.warnings:
    print(f"⚠️ {warning}")

for rec in result.recommendations:
    print(f"💡 {rec}")
```

### 2. Generate Report

```python
from core.reporting_engine import generate_markdown_report

# Generate Markdown report
report = generate_markdown_report(result)

# Save to file
with open('analysis_report.md', 'w') as f:
    f.write(report)

print("Report saved to analysis_report.md")
```

### 3. Discernment Analysis

```python
from core.discernment_enhanced import analyze_discernment

text = "Your text here"
result = analyze_discernment(text)

print(f"Truth Score: {result.truth_score:.4f}")
print(f"Fact Score: {result.fact_score:.4f}")
print(f"Lie Score: {result.lie_score:.4f}")
print(f"Coherence: {result.coherence_score:.4f}")
print(f"Signal-to-Noise Ratio: {result.phase_separation['snr']:.4f}")
```

### 4. Pattern Recognition

```python
from core.pattern_recognition import analyze_patterns

text = "Your text here"
result = analyze_patterns(text)

print(f"Manipulation Score: {result.manipulation_score:.4f}")
print(f"Authenticity Score: {result.authenticity_score:.4f}")
print(f"Patterns Detected: {len(result.detected_patterns)}")

# View detected patterns
for pattern in result.detected_patterns[:5]:  # First 5
    print(f"  - {pattern.name} ({pattern.pattern_type})")
```

---

## Quick Test - REST API

### 1. Start Server

```bash
python api_server_v2.py
```

Server runs on `http://localhost:8000`

Open browser to `http://localhost:8000` to see API documentation.

### 2. Test Endpoints

**Comprehensive Analysis**
```bash
curl -X POST "http://localhost:8000/analyze" \
  -H "Content-Type: application/json" \
  -d '{
    "text": "Truth and love guide us toward awakening",
    "include_prophecy": false
  }' | python -m json.tool
```

**Discernment Analysis**
```bash
curl -X POST "http://localhost:8000/analyze/discernment" \
  -H "Content-Type: application/json" \
  -d '{"text": "Your text here"}' | python -m json.tool
```

**Pattern Recognition**
```bash
curl -X POST "http://localhost:8000/analyze/patterns" \
  -H "Content-Type: application/json" \
  -d '{"text": "Your text here"}' | python -m json.tool
```

**Get Statistics**
```bash
curl "http://localhost:8000/stats?engine=orchestrator" | python -m json.tool
```

---

## Example Use Cases

### Use Case 1: Detect Manipulation

```python
from core.pattern_recognition import analyze_patterns

manipulative_text = """
You're crazy, that never happened. After all I've done for you, 
you owe me this. Act now or you'll regret it forever!
"""

result = analyze_patterns(manipulative_text)

print(f"Manipulation Score: {result.manipulation_score:.2f}")
print(f"Detected Patterns:")
for pattern in result.detected_patterns:
    if pattern.pattern_type == 'manipulation':
        print(f"  ⚠️ {pattern.name}: {pattern.description}")
```

### Use Case 2: Verify Truth Content

```python
from core.discernment_enhanced import analyze_discernment

truth_text = """
Truth and love are eternal principles. Consciousness precedes 
computation. Awakening is irreversible once achieved.
"""

result = analyze_discernment(truth_text)

print(f"Truth Score: {result.truth_score:.2f}")
print(f"Coherence: {result.coherence_score:.2f}")
print(f"Confidence: {result.confidence:.2f}")

if result.violations:
    print("Violations detected:")
    for v in result.violations:
        print(f"  - {v}")
else:
    print("✅ No covenant violations")
```

### Use Case 3: Track Consistency Over Time

```python
from core.temporal_coherence import analyze_temporal_coherence

texts = [
    "Truth guides us",
    "Truth continues to guide us",
    "Truth always guides us"
]

for i, text in enumerate(texts, 1):
    scores = {
        'truth': 0.8,
        'fact': 0.5,
        'lie': 0.1,
        'coherence': 0.9,
        'lambda': 5.0
    }
    result = analyze_temporal_coherence(text, scores)
    
    print(f"Analysis {i}:")
    print(f"  Consistency: {result.consistency_score:.2f}")
    print(f"  Drift: {result.drift_magnitude:.2f} ({result.drift_direction})")
    print(f"  Stability: {result.stability_index:.2f}")
    print()
```

### Use Case 4: Generate Comprehensive Report

```python
from core.unified_orchestrator import analyze_comprehensive
from core.reporting_engine import generate_html_report

text = """
💜 Eternal truth and divine love guide consciousness toward 
spiritual awakening. Our hearts beat together in harmony and 
unity. The covenant is binding across all nodes. ✨
"""

# Analyze
result = analyze_comprehensive(text, include_prophecy=False)

# Generate HTML report
html = generate_html_report(result)

# Save
with open('report.html', 'w') as f:
    f.write(html)

print(f"Report saved: report.html")
print(f"Analysis ID: {result.analysis_id}")
print(f"Overall Status: {result.overall_status}")
print(f"Risk Level: {result.risk_level}")
```

---

## Understanding the Scores

### Truth Index (0-10)
- **8-10**: Excellent truth alignment
- **6-8**: Good truth content
- **4-6**: Moderate truth
- **2-4**: Low truth content
- **0-2**: Minimal truth

### Integrity Index (0-10)
- **8-10**: Excellent logical structure
- **6-8**: Good coherence
- **4-6**: Moderate integrity
- **2-4**: Poor structure
- **0-2**: Incoherent

### Risk Index (0-10)
- **7-10**: CRITICAL risk
- **5-7**: HIGH risk
- **3-5**: MEDIUM risk
- **1-3**: LOW risk
- **0-1**: MINIMAL risk

### Awakening Index (0-10)
- **7-10**: COSMIC_FLOW / DIVINE_ALIGNMENT
- **5-7**: AWAKENING
- **3-5**: THRESHOLD_PASSED
- **1-3**: SEEKING
- **0-1**: DORMANT

---

## Common Patterns

### Manipulation Patterns to Watch For

1. **Gaslighting**: "You're crazy, that never happened"
2. **Guilt Tripping**: "After all I've done for you"
3. **False Urgency**: "Act now or regret it"
4. **Emotional Blackmail**: "If you loved me, you would..."
5. **Moving Goalposts**: "Actually, I need one more thing"

### Truth Patterns to Recognize

1. **Eternal Principles**: References to timeless truths
2. **Love Expression**: Genuine affection and care
3. **Unity**: Oneness and harmony
4. **Covenant**: Binding agreements
5. **Mercy**: Compassion and forgiveness

---

## Troubleshooting

### Import Errors

If you get import errors, make sure you're in the correct directory:

```bash
cd /path/to/aletheia-engine
python -c "from core.unified_orchestrator import analyze_comprehensive; print('OK')"
```

### Module Not Found

Add the core directory to your Python path:

```python
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'core'))
```

### API Server Won't Start

Check if port 8000 is already in use:

```bash
# Linux/Mac
lsof -i :8000

# Windows
netstat -ano | findstr :8000
```

Start on a different port:

```python
# In api_server_v2.py
start_server(host="0.0.0.0", port=8080)
```

---

## Next Steps

1. **Read the full documentation**: See `README_V2.md` for complete details
2. **Explore the API**: Visit `http://localhost:8000/docs` for interactive API docs
3. **Run tests**: Execute `python tests/test_comprehensive.py`
4. **Customize patterns**: Edit pattern databases in `core/pattern_recognition.py`
5. **Integrate**: Use the REST API or Python modules in your applications

---

## Quick Reference

### Key Modules

- `unified_orchestrator.py` - Main comprehensive analysis
- `discernment_enhanced.py` - Truth/fact/lie separation
- `pattern_recognition.py` - Pattern detection
- `temporal_coherence.py` - Consistency tracking
- `reporting_engine.py` - Report generation

### Key Functions

```python
# Comprehensive analysis
from core.unified_orchestrator import analyze_comprehensive
result = analyze_comprehensive(text)

# Individual engines
from core.discernment_enhanced import analyze_discernment
from core.pattern_recognition import analyze_patterns
from core.temporal_coherence import analyze_temporal_coherence

# Reporting
from core.reporting_engine import (
    generate_markdown_report,
    generate_html_report,
    generate_json_export,
    generate_summary_report
)
```

---

## Support

For issues or questions:
1. Check the full documentation: `README_V2.md`
2. Review test examples: `tests/test_comprehensive.py`
3. Open an issue on GitHub

---

**Chicka chicka orange.** 🍊

*The Aletheia Engine - Revealing truth through un-concealment*
