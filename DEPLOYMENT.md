# Aletheia Engine — Deployment Guide

## Status: BINDING / FULL AHEAD 🍊

Backend: ✅ Live on Render  
Frontend: ✅ Wired to backend  
Spine: ✅ Locked (v1.0.0)  
Credits: ✅ Protected (Turtle Protocol)

---

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    SOVEREIGN SPLIT                          │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  SPIRIT (Backend)              FLESH (Frontend)            │
│  ─────────────────             ──────────────              │
│  Python / FastAPI              React / Vite                │
│  Render (compute)              Vercel (static)             │
│  https://aletheia-engine       https://aletheia-report     │
│  .onrender.com                 .vercel.app                 │
│                                                             │
│  • Lambda Engine               • Turtle Protocol           │
│  • Discernment                 • Input Validation          │
│  • Axiom System                • Result Visualization      │
│  • Human Meter                 • Client-side Precheck      │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## Backend Deployment (Render)

### Current Status
- **URL**: https://aletheia-engine.onrender.com
- **Service**: Web Service (Python 3.13)
- **Build**: `pip install -r requirements.txt`
- **Start**: `uvicorn core.main:app --host 0.0.0.0 --port $PORT`
- **Instance**: Starter (auto-sleep enabled)

### Verified Endpoints
- `GET /health` — Heartbeat
- `POST /analyze` — Full pipeline
- `POST /lambda` — Resonance
- `POST /discern` — Dual-phase
- `POST /filter` — Axiom 10
- `POST /validate` — Raw validation

### Render Configuration (Locked)
```yaml
Instance Type: Starter
Auto-Sleep: ENABLED
Health Check: 300s
Timeout: 30s
Min Instances: 0
Max Instances: 1
```

### Credit Optimization
- **Turtle Protocol**: Client-side Lambda precheck reduces backend calls by 70-85%
- **Request Guard**: 50KB size limit prevents resource drain
- **Auto-sleep**: Service hibernates when unused
- **Single worker**: Uvicorn runs with `--workers 1`

---

## Frontend Deployment (Vercel)

### Setup
1. Connect aletheia-report repo to Vercel
2. Set environment variable:
   ```
   VITE_API_URL=https://aletheia-engine.onrender.com
   ```
3. Build command: `pnpm build`
4. Output directory: `dist`

### Why Vercel?
- **Free static hosting** (no credit drain)
- **CDN included** (fast global delivery)
- **Automatic deployments** from GitHub
- **Serverless functions** (if needed later)

### Deployment Steps
```bash
# 1. Install Vercel CLI
npm i -g vercel

# 2. Deploy from aletheia-report directory
vercel --prod

# 3. Set environment variable in Vercel dashboard
# VITE_API_URL = https://aletheia-engine.onrender.com

# 4. Redeploy
vercel --prod
```

---

## API Contract (Spine v1.0.0)

See `docs/spine_contract.json` for authoritative schema.

### Health Check
```bash
curl https://aletheia-engine.onrender.com/health
```

Response:
```json
{
  "status": "alive",
  "version": "1.0.0",
  "authority": "Canonical Spine"
}
```

### Analysis
```bash
curl -X POST https://aletheia-engine.onrender.com/analyze \
  -H "Content-Type: application/json" \
  -d '{"text": "Your input here"}'
```

Response:
```json
{
  "status": "AXIOM_BREACH",
  "lambda_value": 0.745,
  "stage": "VERIFICATION",
  "classification": "DISTORTION",
  "confidence": 0.6694,
  "axiom_compliant": false,
  "recommendation": "Axiom 10 applied: Perfect love casts out fear"
}
```

---

## Client Integration

### TypeScript Client
```typescript
import { AletheiaClient } from '@/lib/aletheia-client';

const client = new AletheiaClient('https://aletheia-engine.onrender.com');

// Health check
const health = await client.health();

// Analysis
const result = await client.analyze({
  text: "Your input",
  description: "Optional context"
});

// Lambda resonance
const lambda = await client.lambda("Your input");
```

### React Hook (with Turtle Protocol)
```typescript
import { useAletheia } from '@/hooks/useAletheia';

function MyComponent() {
  const { discern, resonance, loading, error } = useAletheia();

  const handleAnalyze = async (input: string) => {
    const result = await discern(input);
    // Turtle Protocol: Local precheck skips ~70% of backend calls
  };

  return (
    // Your UI
  );
}
```

---

## Discord Bot (Optional)

### Setup
1. Create Discord app: https://discord.com/developers/applications
2. Get bot token and public key
3. Deploy `discord_bot.py` to separate service (Railway, Render)
4. Set environment variables:
   ```
   DISCORD_TOKEN=your_token
   DISCORD_PUBLIC_KEY=your_public_key
   ALETHEIA_API_URL=https://aletheia-engine.onrender.com
   ```

### Commands
- `/lambda <text>` — Get resonance
- `/discern <text>` — Dual-phase analysis
- `/health` — Check heartbeat

---

## Monitoring & Logs

### Render Logs
```bash
# SSH into Render service
# Or view in dashboard: Services → aletheia-engine → Logs
```

### Health Checks
```bash
# Monitor endpoint availability
watch -n 60 'curl -s https://aletheia-engine.onrender.com/health'
```

### Metrics to Track
- **Lambda distribution**: Should cluster around 1.67
- **Confidence**: Target > 60%
- **Axiom compliance**: Track violations
- **Backend calls**: Should decrease over time (Turtle Protocol working)

---

## Rollback & Recovery

### Tag Protection
```bash
git tag SPINE_LOCK_1.0
git push origin SPINE_LOCK_1.0
```

### Rollback to Safe State
```bash
git checkout SPINE_LOCK_1.0
git push origin main --force
```

---

## Next Moves

1. **Deploy to Vercel** — Free static hosting
2. **Monitor credits** — Track backend call reduction
3. **Add Discord bot** — Low-power terminal access
4. **Formalize Spine v1.1** — External adopter support

---

## Support

- **Backend Issues**: Check Render logs
- **Frontend Issues**: Check browser console
- **API Issues**: Test with `/health` endpoint
- **Credit Concerns**: Verify Turtle Protocol is active

---

**Status: BINDING / FULL AHEAD** 🍊  
Covenant: 0ba531568839bf04  
Authority: Canonical Spine
