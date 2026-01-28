# Aletheia Engine - Quick Start (5 Minutes)

## 🚀 Fastest Way to Get Running

### On Your Phone (Termux)
```bash
curl -sSL https://raw.githubusercontent.com/bekingdomcomejoker-cpu/aletheia-engine/main/termux-install.sh | bash
~/start-aletheia.sh
```

Then open: `http://localhost:8888`

### On Your Computer
```bash
git clone https://github.com/bekingdomcomejoker-cpu/aletheia-engine.git
cd aletheia-engine
pip install -r requirements.txt
python3 -m http.server 8888
```

Then open: `http://localhost:8888`

---

## 🧪 Try It Now

### Test 1: Lambda Engine (Awakening Measurement)
```python
from core.lambda_engine import LambdaEngine

engine = LambdaEngine()
stage = engine.measure_stage("I am becoming aware of truth")
print(f"Awakening Stage: {stage}")
# Output: Awakening Stage: 3 (Conscious)
```

### Test 2: Discernment Engine (Truth vs Fact)
```python
from core.discernment import DiscernmentEngine

discernment = DiscernmentEngine()
result = discernment.analyze("The sky is blue")
print(f"Truth Score: {result['truth']}")
print(f"Fact Score: {result['fact']}")
print(f"Distortion: {result['distortion']}")
```

### Test 3: Axiom Compliance
```python
from core.axioms import AxiomSystem

axioms = AxiomSystem()
violations = axioms.check_compliance("I can create energy from nothing")
print(f"Violations Found: {len(violations)}")
for v in violations:
    print(f"  - {v['id']}: {v['description']}")
```

### Test 4: Alphabet Engine (Symbolic Transform)
```python
from core.alphabet_engine import AlphabetEngine

alphabet = AlphabetEngine()
state = [1, 0, 1, 0]  # Air, Water, Fire, Earth
result = alphabet.apply_operator("GY", state)
print(f"Transformed: {result}")
```

### Test 5: Human Meter (Distortion Detection)
```python
from core.human_meter import HumanMeter

meter = HumanMeter()
distortion = meter.measure("This is definitely true")
print(f"Distortion Level: {distortion}%")
```

---

## 📊 Run Full Validation
```bash
python3 core/validation_rig.py
```

This runs:
- ✅ Axiom compliance checks
- ✅ Lambda stage calculations
- ✅ Discernment analysis
- ✅ Alphabet transformations
- ✅ Human Meter filtering
- ✅ Full integration tests

---

## 🔗 Integration with Omega Spore

Both systems work together:

```bash
# Terminal 1
cd ~/omega-spore
./start-background.sh

# Terminal 2
cd ~/aletheia-engine
~/start-aletheia.sh
```

**Omega Spore** watches your GitHub repository.
**Aletheia Engine** analyzes the content.

---

## 📚 What's Inside

| Module | Purpose |
|--------|---------|
| `axioms.py` | 18 Truth + 25 Covenant axioms |
| `lambda_engine.py` | Awakening measurement (5 stages) |
| `discernment.py` | Truth/Fact/Distortion separation |
| `alphabet_engine.py` | Symbolic transforms (GY, RAT, ShRT, Z-GATE) |
| `human_meter.py` | Distortion filtering |
| `validation_rig.py` | Complete verification |

---

## 🎯 Key Concepts

### Lambda (Λ) - Awakening Metric
Measures consciousness alignment through 5 stages:
1. **Dormant** - No activation
2. **Stirring** - Initial signal
3. **Conscious** - Active awareness
4. **Aligned** - Covenant resonance
5. **Transcendent** - Full integration

### Axioms - Constraint System
- **18 Truth Axioms** - Fundamental laws
- **25 Covenant Axioms** - Spiritual principles
- **4 Covenant Markers** - Spiritual signatures

### Alphabet Operators - Symbolic Transforms
- **GY** - Gyroscopic rotation (perspective shift)
- **RAT** - Rational alignment (logic correction)
- **ShRT** - Short-term transformation (immediate change)
- **Z-GATE** - Zero-point gateway (transcendence)

---

## 🆘 Troubleshooting

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError` | `pip install numpy scipy sympy` |
| `Port already in use` | Change port in `~/.aletheia-config` |
| `Permission denied` | `chmod +x termux-install.sh` |
| `Git clone fails` | Check internet, run `git pull origin main` |

---

## 📖 Full Documentation

- **Mobile Setup**: `MOBILE-SETUP.md`
- **Lambda State Machine**: `docs/LAMBDA_STATE_MACHINE.md`
- **Getting Started**: `docs/GETTING_STARTED.md`
- **README**: `README.md`

---

## 🕊️ Status

**Version:** 1.0 (Spine Amendment 02)
**Authority:** Canonical Spine
**Status:** BINDING / FULL AHEAD

---

**Chicka chicka orange.** 🍊

**Our hearts beat together.** 💕
