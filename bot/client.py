# discord
from discord.ext import commands

# token
import bot_token
jb_app_token = bot_token.JB_APP_TOKEN

# JB_APP

# client 생성
client = commands.Bot(command_prefix='*')

# client command
@client.command()
async def hello(ctx):
    await ctx.send('안녕하세요')

# client 실행
client.run(jb_app_token)


