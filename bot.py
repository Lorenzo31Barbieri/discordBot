import discord
from bot_logic import gen_pass

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Hai fatto l\\'accesso come {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$ciao'):
        await message.channel.send(f'Ciao! Io sono un bot{client.user}!')
    elif  message.content.startswith('$heh'):
        if len(message.content) > 4:
            count_heh = int(message.content[4:])
        else:
            count_heh = 10
        await message.channel.send("he" * count_heh)
    elif message.content.startswith("$password"):
        n = message.content[9:]
        await message.channel.send(gen_pass(n))
        
client.run("IL TOKEN SEGRETO VA QUI")
