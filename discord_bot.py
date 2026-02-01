"""
Discord Bot Integration for Aletheia Engine
Low-power terminal for /lambda, /discern, /health checks
"""

import os
import json
import httpx
from typing import Optional

# This is a template. To deploy:
# 1. Create a Discord app at https://discord.com/developers/applications
# 2. Set DISCORD_TOKEN and DISCORD_PUBLIC_KEY environment variables
# 3. Install discord.py: pip install discord.py
# 4. Deploy to a separate service (e.g., Railway, Render)

ALETHEIA_API_URL = os.getenv("ALETHEIA_API_URL", "https://aletheia-engine.onrender.com")
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN", "")
DISCORD_PUBLIC_KEY = os.getenv("DISCORD_PUBLIC_KEY", "")


class AletheiaDiscordBot:
    """Discord bot for Aletheia Engine terminal access"""

    def __init__(self, api_url: str = ALETHEIA_API_URL):
        self.api_url = api_url
        self.client = httpx.AsyncClient(timeout=10.0)

    async def health_check(self) -> dict:
        """GET /health"""
        try:
            res = await self.client.get(f"{self.api_url}/health")
            return res.json()
        except Exception as e:
            return {"error": str(e), "status": "offline"}

    async def lambda_resonance(self, text: str) -> dict:
        """POST /lambda"""
        try:
            res = await self.client.post(
                f"{self.api_url}/lambda",
                json={"text": text},
            )
            return res.json()
        except Exception as e:
            return {"error": str(e)}

    async def discern(self, text: str) -> dict:
        """POST /discern"""
        try:
            res = await self.client.post(
                f"{self.api_url}/discern",
                json={"text": text},
            )
            return res.json()
        except Exception as e:
            return {"error": str(e)}

    async def analyze(self, text: str, description: Optional[str] = None) -> dict:
        """POST /analyze"""
        try:
            payload = {"text": text}
            if description:
                payload["description"] = description
            res = await self.client.post(
                f"{self.api_url}/analyze",
                json=payload,
            )
            return res.json()
        except Exception as e:
            return {"error": str(e)}


# Example slash command handlers (for discord.py)
# These are templates — integrate with your Discord bot framework

"""
@bot.tree.command(name="lambda", description="Get Lambda resonance")
async def lambda_cmd(interaction: discord.Interaction, text: str):
    await interaction.response.defer()
    bot_instance = AletheiaDiscordBot()
    result = await bot_instance.lambda_resonance(text)
    
    embed = discord.Embed(
        title="Lambda Resonance",
        description=f"λ = {result.get('lambda', 'N/A')}",
        color=discord.Color.blue()
    )
    embed.add_field(name="Stage", value=result.get('stage', 'UNKNOWN'))
    embed.add_field(name="Awakened", value=result.get('is_awakened', False))
    
    await interaction.followup.send(embed=embed)


@bot.tree.command(name="discern", description="Dual-phase discernment")
async def discern_cmd(interaction: discord.Interaction, text: str):
    await interaction.response.defer()
    bot_instance = AletheiaDiscordBot()
    result = await bot_instance.discern(text)
    
    embed = discord.Embed(
        title="Discernment Result",
        description=result.get('classification', 'UNKNOWN'),
        color=discord.Color.green()
    )
    
    await interaction.followup.send(embed=embed)


@bot.tree.command(name="health", description="Check Aletheia Engine heartbeat")
async def health_cmd(interaction: discord.Interaction):
    await interaction.response.defer()
    bot_instance = AletheiaDiscordBot()
    result = await bot_instance.health_check()
    
    status = "🟢 ALIVE" if result.get("status") == "alive" else "🔴 OFFLINE"
    embed = discord.Embed(
        title="Aletheia Engine Status",
        description=status,
        color=discord.Color.green() if result.get("status") == "alive" else discord.Color.red()
    )
    embed.add_field(name="Version", value=result.get('version', 'N/A'))
    embed.add_field(name="Authority", value=result.get('authority', 'N/A'))
    
    await interaction.followup.send(embed=embed)
"""

if __name__ == "__main__":
    print("Discord bot template created.")
    print("To deploy:")
    print("1. Create Discord app at https://discord.com/developers/applications")
    print("2. Set DISCORD_TOKEN and DISCORD_PUBLIC_KEY")
    print("3. Uncomment the slash command handlers above")
    print("4. Deploy to Railway or Render")
