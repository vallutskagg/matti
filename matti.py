import discord
import os
import requests

DISCORD_TOKEN = os.environ['MTQwMzA0MjMxNTY2NDM2Mzc2Mw.GFz1NY.EqnBQE0AwFS8uSaDdtPJzpSrL0Z-2Okpf0Gnic']
TOGETHER_API_KEY = os.environ['64ea227142d38c6889f842e0e85654ba844ba4b216042634256ce60ae5ed74c2']

client = discord.Client(intents=discord.Intents.all())

def kysytekoalylta(prompt):
    resp = requests.post(
        "https://api.together.xyz/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {TOGETHER_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            # 🔽 Tässä kohtaa vaihdetaan mallin nimi:
            "model": "meta-llama/Llama-3.3-70B-Instruct-Turbo-Free",
            "messages": [{"role": "user", "content": prompt}]
        }
    )
    return resp.json()["choices"][0]["message"]["content"]

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!kysy "):
        kysymys = message.content[len("!kysy "):]
        await message.channel.send("💭 Hetki...")

        vastaus = kysytekoalylta(kysymys)
        await message.channel.send(vastaus[:2000])

client.run(DISCORD_TOKEN)
