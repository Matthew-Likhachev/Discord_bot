

# bot.py

import discord
import config
#from dotenv import load_dotenv

#config()
TOKEN = config.TOKEN
GUILD = config.GUILD_ID

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'привет' in message.content.lower():
        await message.channel.send('Fuck You!')

client.run(TOKEN)
