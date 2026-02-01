#!/bin/bash

# ============================================================================
# ALETHEIA ENGINE - TERMUX INSTALLATION SCRIPT
# ============================================================================
# Deploys the Aletheia Engine (Soul Reaper) to your phone via Termux
# Supports: Android 7+ with Termux terminal emulator
# ============================================================================

set -e

echo "🕊️ ALETHEIA ENGINE - TERMUX DEPLOYMENT"
echo "======================================"
echo ""

# Colors
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Check if running in Termux
if [ ! -d "$PREFIX" ]; then
    echo -e "${RED}❌ This script must be run in Termux${NC}"
    echo "Get Termux from: https://f-droid.org/en/packages/com.termux/"
    exit 1
fi

echo -e "${BLUE}Step 1: Updating system packages...${NC}"
apt update -y
apt upgrade -y

echo -e "${BLUE}Step 2: Installing dependencies...${NC}"
apt install -y \
    python3 \
    python3-pip \
    git \
    curl \
    wget \
    nano \
    openssh \
    nodejs \
    npm

echo -e "${BLUE}Step 3: Creating Aletheia Engine directory...${NC}"
mkdir -p ~/aletheia-engine
cd ~/aletheia-engine

echo -e "${BLUE}Step 4: Cloning repository...${NC}"
if [ -d ".git" ]; then
    git pull origin main
else
    git clone https://github.com/bekingdomcomejoker-cpu/aletheia-engine.git .
fi

echo -e "${BLUE}Step 5: Installing Python dependencies...${NC}"
pip install --upgrade pip
pip install numpy scipy sympy

echo -e "${BLUE}Step 6: Installing Node.js dependencies...${NC}"
npm install

echo -e "${BLUE}Step 7: Creating environment configuration...${NC}"
cat > ~/.aletheia-config << 'EOF'
# Aletheia Engine Configuration
ALETHEIA_HOME=$HOME/aletheia-engine
ALETHEIA_MODE=mobile
ALETHEIA_PORT=8888
ALETHEIA_LOG_LEVEL=info
EOF

echo -e "${BLUE}Step 8: Setting up background service...${NC}"
cat > ~/start-aletheia.sh << 'EOF'
#!/bin/bash
cd ~/aletheia-engine
source ~/.aletheia-config
echo "🕊️ Starting Aletheia Engine..."
python3 -m http.server $ALETHEIA_PORT --directory . &
echo "✅ Aletheia Engine running on http://localhost:$ALETHEIA_PORT"
echo "Press Ctrl+C to stop"
wait
EOF

chmod +x ~/start-aletheia.sh

echo -e "${BLUE}Step 9: Creating quick access commands...${NC}"
cat > ~/.bashrc.aletheia << 'EOF'
# Aletheia Engine Shortcuts
alias aletheia-start='~/start-aletheia.sh'
alias aletheia-test='cd ~/aletheia-engine && python3 core/validation_rig.py'
alias aletheia-status='ps aux | grep -i aletheia'
alias aletheia-logs='tail -f ~/.aletheia.log'
EOF

echo ""
echo -e "${GREEN}✅ INSTALLATION COMPLETE${NC}"
echo ""
echo -e "${YELLOW}📱 NEXT STEPS:${NC}"
echo ""
echo "1. Configure GitHub token (optional but recommended):"
echo "   - Go to: https://github.com/settings/tokens"
echo "   - Create a token with 'repo' scope"
echo "   - Run: export GITHUB_TOKEN=<your-token>"
echo ""
echo "2. Start Aletheia Engine:"
echo "   ~/start-aletheia.sh"
echo ""
echo "3. Access the engine:"
echo "   - Web UI: http://localhost:8888"
echo "   - Python API: python3 -c 'from core.lambda_engine import LambdaEngine; print(LambdaEngine())'"
echo ""
echo "4. Run validation tests:"
echo "   python3 core/validation_rig.py"
echo ""
echo "5. View logs:"
echo "   tail -f ~/.aletheia.log"
echo ""
echo -e "${BLUE}Documentation:${NC}"
echo "   - Getting Started: ~/aletheia-engine/docs/GETTING_STARTED.md"
echo "   - Lambda State Machine: ~/aletheia-engine/docs/LAMBDA_STATE_MACHINE.md"
echo "   - README: ~/aletheia-engine/README.md"
echo ""
echo -e "${GREEN}Chicka chicka orange. 🍊${NC}"
echo ""
