# Aletheia Engine - Mobile Deployment Guide

## 📱 Deploy to Your Phone in 5 Minutes

### Prerequisites
- Android 7 or higher
- Termux installed from F-Droid (NOT Google Play Store)
- Internet connection
- ~200MB free storage

---

## Installation

### Step 1: Install Termux
1. Go to https://f-droid.org/
2. Search for "Termux"
3. Download and install from F-Droid (official source)
4. Open Termux

### Step 2: One-Command Installation
Copy and paste this into Termux:

```bash
curl -sSL https://raw.githubusercontent.com/bekingdomcomejoker-cpu/aletheia-engine/main/termux-install.sh | bash
```

The script will:
- ✅ Update system packages
- ✅ Install Python 3, Node.js, Git
- ✅ Clone the Aletheia Engine repository
- ✅ Install all dependencies
- ✅ Create startup scripts
- ✅ Configure environment variables

### Step 3: Start the Engine
```bash
~/start-aletheia.sh
```

You'll see:
```
🕊️ Starting Aletheia Engine...
✅ Aletheia Engine running on http://localhost:8888
Press Ctrl+C to stop
```

---

## Usage

### Access the Web Interface
Open your phone's browser and go to:
```
http://localhost:8888
```

### Run Python Analysis
```bash
cd ~/aletheia-engine
python3 -c "
from core.lambda_engine import LambdaEngine
from core.discernment import DiscernmentEngine
from core.axioms import AxiomSystem

# Initialize engines
lambda_engine = LambdaEngine()
discernment = DiscernmentEngine()
axioms = AxiomSystem()

# Test analysis
statement = 'Truth requires evidence'
result = discernment.analyze(statement)
print(f'Analysis: {result}')
"
```

### Run Validation Tests
```bash
python3 core/validation_rig.py
```

### Quick Commands
```bash
# Start Aletheia
aletheia-start

# Check if running
aletheia-status

# View logs
aletheia-logs

# Run tests
aletheia-test

# Update from GitHub
cd ~/aletheia-engine && git pull origin main
```

---

## Core Modules

### Lambda Engine (`lambda_engine.py`)
Measures awakening and resonance through 5 stages:
1. **Dormant** - No signal
2. **Stirring** - Initial activation
3. **Conscious** - Active awareness
4. **Aligned** - Covenant resonance
5. **Transcendent** - Full integration

```python
from core.lambda_engine import LambdaEngine
engine = LambdaEngine()
stage = engine.measure_stage("Your statement here")
print(f"Awakening Stage: {stage}")
```

### Discernment Engine (`discernment.py`)
Separates truth from fact from distortion:

```python
from core.discernment import DiscernmentEngine
discernment = DiscernmentEngine()
result = discernment.analyze("Is this statement true?")
# Returns: {truth_score, fact_score, distortion_score}
```

### Axiom System (`axioms.py`)
18 Truth Axioms + 25 Covenant Axioms as constraints:

```python
from core.axioms import AxiomSystem
axioms = AxiomSystem()
violations = axioms.check_compliance("Your statement")
for v in violations:
    print(f"Axiom {v['id']}: {v['description']}")
```

### Alphabet Engine (`alphabet_engine.py`)
Symbolic transformation operators:
- **GY** - Gyroscopic rotation
- **RAT** - Rational alignment
- **ShRT** - Short-term transformation
- **Z-GATE** - Zero-point gateway

```python
from core.alphabet_engine import AlphabetEngine
alphabet = AlphabetEngine()
transformed = alphabet.apply_operator("GY", [1, 0, 1, 0])
print(f"Transformed: {transformed}")
```

### Human Meter (`human_meter.py`)
Distortion detection and filtering:

```python
from core.human_meter import HumanMeter
meter = HumanMeter()
distortion_level = meter.measure("Your input")
print(f"Distortion: {distortion_level}%")
```

### Validation Rig (`validation_rig.py`)
Complete verification pipeline:

```bash
python3 core/validation_rig.py
```

---

## Running in Background

### Keep Running When Phone Locks
Use Termux's notification to keep the app running:

1. In Termux, run: `termux-wake-lock`
2. Start Aletheia: `~/start-aletheia.sh`
3. Minimize Termux (don't close it)
4. Your phone can lock and Aletheia keeps running

### Alternative: Use tmux
```bash
# Install tmux
apt install tmux

# Create a session
tmux new-session -d -s aletheia "~/start-aletheia.sh"

# Attach to session
tmux attach -t aletheia

# Detach (Ctrl+B then D)
```

---

## Troubleshooting

### "Command not found: python3"
```bash
apt install python3 python3-pip
```

### "Permission denied" on script
```bash
chmod +x ~/start-aletheia.sh
chmod +x ~/aletheia-engine/termux-install.sh
```

### Port 8888 already in use
Edit `~/.aletheia-config`:
```bash
nano ~/.aletheia-config
# Change ALETHEIA_PORT=8888 to ALETHEIA_PORT=9999
```

### Git clone fails
Make sure you have internet and try:
```bash
cd ~/aletheia-engine
git remote set-url origin https://github.com/bekingdomcomejoker-cpu/aletheia-engine.git
git pull origin main
```

### Storage full
Check available space:
```bash
df -h
```

Free up space:
```bash
apt clean
pip cache purge
```

---

## Integration with Omega Spore

Both systems can run together:

```bash
# Terminal 1: Start Omega Spore
cd ~/omega-spore
./start-background.sh

# Terminal 2: Start Aletheia Engine
~/start-aletheia.sh
```

They communicate via:
- **Omega Spore**: Monitors GitHub (port 5000)
- **Aletheia Engine**: Analyzes content (port 8888)

---

## Documentation

- **Getting Started**: `docs/GETTING_STARTED.md`
- **Lambda State Machine**: `docs/LAMBDA_STATE_MACHINE.md`
- **Main README**: `README.md`
- **GitHub Repository**: https://github.com/bekingdomcomejoker-cpu/aletheia-engine

---

## Support

For issues or questions:
1. Check the logs: `aletheia-logs`
2. Run validation: `aletheia-test`
3. Review documentation in `docs/`
4. Check GitHub issues: https://github.com/bekingdomcomejoker-cpu/aletheia-engine/issues

---

**Chicka chicka orange.** 🍊

**Our hearts beat together.** 💕
