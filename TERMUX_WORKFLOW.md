# 🕊️ OMNISSIAH ENGINE — Termux Workflow Guide

**Device**: Redmi 13C (ARM64)  
**OS**: Android + Termux  
**Strategy**: Staging + Verification Node

---

## Ground Truth

Your phone is **excellent at**:
- ✅ Cloning / pulling / inspecting repos
- ✅ One-shot builds
- ✅ Static previews
- ✅ Python execution
- ✅ Crypto + math
- ✅ Editing
- ✅ Verification
- ✅ Transport / staging

Your phone is **not ideal for**:
- ❌ Running Vite dev servers continuously
- ❌ Hot-reload at desktop speeds
- ❌ Heavy native CSS optimizers
- ❌ Large graph/layout libs under load
- ❌ "Leave it running all day"

**This is not a failure. This is physics.**

---

## Recommended Workflow

### Option A: Static Build + Python Preview (Best for Termux)

This is the **phone-first** approach. No Vite. No hot-reload. Just build → verify → stage.

```bash
# 1. Clone the repo
git clone https://github.com/bekingdomcomejoker-cpu/omnissiah-engine.git
cd omnissiah-engine

# 2. Install dependencies (one time)
pnpm install

# 3. Build the frontend to static files
pnpm build

# 4. Preview the build without Vite (lightweight)
python3 -m http.server 8080 --directory dist/public

# 5. Open in your phone browser
# http://localhost:8080
```

**Advantages**:
- ✔ No native binaries required
- ✔ No long-running dev process
- ✔ Much lighter on CPU/RAM
- ✔ No thermal throttling issues
- ✔ Perfect for verification

**Disadvantages**:
- ✗ No hot-reload
- ✗ Must rebuild to see changes

---

### Option B: Dev Server (When Needed)

If you need to test changes quickly:

```bash
# Start Vite briefly
pnpm dev --host

# Use it for a few minutes
# Make your changes
# Test in browser

# Kill it when done (Ctrl+C)
# Don't leave it running
```

**Important**: This is **temporary**. Use it for quick testing, then kill it. Don't expect it to run all day.

---

### Option C: Python Engine Only (Fastest)

If you only need to test the **math engine** (no UI):

```bash
# Run the core engine
python3 omnissiah_engine.py

# Or run individual modules
python3 cryptographic_seal.py
python3 hieroglyphic_sigil.py
python3 alphabet_engine.py
```

**This is the fastest option.** Pure Python, no Node, no build step.

---

## Typical Termux Session

```bash
# Morning: Clone and inspect
git clone https://github.com/bekingdomcomejoker-cpu/omnissiah-engine.git
cd omnissiah-engine
git log --oneline | head -5

# Midday: Run Python engine
python3 omnissiah_engine.py

# Afternoon: Build and verify
pnpm install  # (only if needed)
pnpm build
python3 -m http.server 8080 --directory dist/public
# Open browser, verify UI

# Evening: Edit and stage
nano client/src/pages/Home.tsx  # Make changes
pnpm build  # Rebuild
# Verify changes

# Night: Push to GitHub
git add -A
git commit -m "Update from Termux"
git push origin main
```

---

## Memory & Thermal Management

### If you see thermal throttling:

1. **Kill Vite** (if running): `Ctrl+C`
2. **Wait 2-3 minutes** for the phone to cool
3. **Run Python only** (no Node): `python3 omnissiah_engine.py`
4. **Use static preview** instead of dev server

### If you run out of memory:

1. **Close other apps**
2. **Use `pnpm build` instead of `pnpm dev`** (lighter)
3. **Use Python modules** instead of Node (much lighter)

---

## File Structure (Termux-Relevant)

```
omnissiah-engine/
├── omnissiah_engine.py          ← Pure Python, run directly
├── cryptographic_seal.py        ← Pure Python, run directly
├── hieroglyphic_sigil.py        ← Pure Python, run directly
├── alphabet_engine.py           ← Pure Python, run directly
├── core.py                      ← Integration module
├── client/                      ← React frontend
│   ├── src/
│   │   ├── pages/Home.tsx
│   │   └── ...
│   └── index.html
├── dist/                        ← Static build output (after pnpm build)
├── package.json                 ← Node dependencies
└── vite.config.ts              ← Vite config (PostCSS, no lightningcss)
```

---

## Quick Commands

```bash
# Run Python engine (fastest)
python3 omnissiah_engine.py

# Build frontend (one-shot)
pnpm build

# Preview build (no Vite)
python3 -m http.server 8080 --directory dist/public

# Start Vite (temporary only)
pnpm dev --host

# Check git status
git status

# Commit and push
git add -A
git commit -m "Your message"
git push origin main
```

---

## Troubleshooting

### "Port 3000 is in use"
```bash
# Kill the process
lsof -i :3000
kill -9 <PID>

# Or use a different port
pnpm dev --host --port 3001
```

### "Cannot find module 'lightningcss'"
```bash
# This is fixed in vite.config.ts (PostCSS transformer)
# Just run: pnpm build
```

### "pnpm: command not found"
```bash
# Reinstall pnpm
npm install -g pnpm
```

### "Python module not found"
```bash
# Install cryptography
pip install cryptography

# Then run
python3 omnissiah_engine.py
```

---

## Best Practices

1. **Use static builds** for verification (not dev server)
2. **Run Python modules** for quick testing (no Node overhead)
3. **Don't leave Vite running** (kill it when done)
4. **Monitor thermal status** (use `top` if needed)
5. **Commit frequently** (small, atomic commits)
6. **Use GitHub as your backup** (push daily)

---

## Why This Workflow?

Your phone is **not** a desktop workstation. It's a **staging + verification node**.

This workflow treats it as such:
- **Staging**: Clone, edit, build
- **Verification**: Test the build, run Python
- **Transport**: Push to GitHub

This is **normal and correct** for mobile development.

---

## Covenant Signature

**CHICKA_CHICKA_ORANGE**  
**Verified by**: The Trinity  
**Till test do us part** 🕊️🗡️

---

**Last Updated**: January 3, 2026  
**Status**: OPERATIONAL  
**Device**: Redmi 13C (ARM64)  
**Environment**: Termux
