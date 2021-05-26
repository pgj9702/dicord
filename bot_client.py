# discord
import discord
from discord.ext import commands

# token
import os

# JB_APP

intents = discord.Intents.default()
intents.members = True

# client 생성
client = commands.Bot(command_prefix='*', intents=intents)

# client command
# command 별명 (aliases=['안녕', '안녕하세요', 'ㅎㅇ'])
@client.command(name = '안녕')
async def hello(ctx):
    await ctx.send('안녕하세요')
    await ctx.send('안녕하세요 {}'.format(ctx.guild.owner))

# user's message event
@client.event()
async def on_message(message):
    content = message.content
    guild = message.guild
    author = message.author
    channel = message.channel

    if content.startswith("!test"):
        await message.channel.send("test" + content)
    if content == "!ping":
        await message.channel.send("Pong!")

# embed
# message box

# discord.FIle
# music, picture etc .. file upload

# client 실행
client.run(os.environ['token'])

