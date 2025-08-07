import discord
import os
import requests
#moikaikille

DISCORD_TOKEN = os.environ['DISCORD_TOKEN']
TOGETHER_API_KEY = os.environ['TOGETHER_API_KEY']

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
        await message.channel.send("💭 Hetki pieni Matti miettii...")

        vastaus = kysytekoalylta(kysymys)
        await message.channel.send(vastaus[:2000])

client.run(DISCORD_TOKEN)
