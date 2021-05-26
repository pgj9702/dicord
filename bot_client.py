# discord
import discord
from discord.ext import commands

# token
import os

# JB_APP

intents = discord.Intents.default()
intents.members = True
intents.guilds = True
intents.messages = True

# client 생성
client = commands.Bot(command_prefix='*', intents=intents)

# client command
# command 별명 (aliases=['안녕', '안녕하세요', 'ㅎㅇ'])
@client.command(name = '안녕')
async def hello(ctx):
    await ctx.send('안녕하세요')
    await ctx.send('안녕하세요 {}'.format(ctx.guild.owner))
    await ctx.send('안녕하세요 {}'.format(ctx.author.name))
    await ctx.author.send('안녕하세요 {}'.format(ctx.author.name)) # 개인 메시지

    print(dir(ctx.author))
    print("hello")

# ctx.author
# '__abstractmethods__', '__class__', '__delattr__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__',
# '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__',
# '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__slots__', '__str__',
# '__subclasshook__', '_abc_impl', '_client_status', '_copy', '_from_message', '_from_presence_update', '_get_channel',
# '_presence_update', '_roles', '_state', '_try_upgrade', '_update', '_update_from_message', '_update_inner_user',
# '_update_roles', '_user', 'activities', 'activity', 'add_roles', 'avatar', 'avatar_url', 'avatar_url_as', 'ban',
# 'block', 'bot', 'color', 'colour', 'create_dm', 'created_at', 'default_avatar', 'default_avatar_url',
# 'desktop_status', 'discriminator', 'display_name', 'dm_channel', 'edit', 'fetch_message', 'guild',
# 'guild_permissions', 'history', 'id', 'is_avatar_animated', 'is_blocked', 'is_friend', 'is_on_mobile', 'joined_at',
# 'kick', 'mention', 'mentioned_in', 'mobile_status', 'move_to', 'mutual_friends', 'mutual_guilds', 'name', 'nick',
# 'pending', 'permissions_in', 'pins', 'premium_since', 'profile', 'public_flags', 'raw_status', 'relationship',
# 'remove_friend', 'remove_roles', 'request_to_speak', 'roles', 'send', 'send_friend_request', 'status', 'system',
# 'top_role', 'trigger_typing', 'typing', 'unban', 'unblock', 'voice', 'web_status'

# user's message event
@client.event
async def on_message(message):
    content = message.content
    guild = message.guild
    author = message.author
    channel = message.channel

    if content.startswith("!test"):
        await message.channel.send("test" + content)
    if content == "!ping":
        await message.channel.send("Pong!")

    await client.process_commands(message)


# 타 함수에서 다른 bot 함수 사용
# await bot.process_commands(msg)

# embed
# message box

# discord.FIle
# music, picture etc .. file upload

# client 실행
# client.run(os.environ['token'])

# terminal test
from bot_token import JB_APP_TOKEN
bot_token = JB_APP_TOKEN
client.run(bot_token)




