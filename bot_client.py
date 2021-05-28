# discord
import discord
from discord.ext import commands
import os

# 반복 작업을 위한 패키지
from discord.ext import tasks
# 현재 시간을 받아와 구조체에 넣어주는 용도로 사용할 패키지
import datetime
# 중복 전송을 방지하기 위해 사용할 패키지
import time

# loa_auction
# 경매장에 원하는 필터로 1분 간격 검색
# 개인당 3개 이하까지 등록 가능
# 새로 등록된 물품 발견시 알림

# 최초 등록 시 현재 경매장에 등록된 물품 정보 출력 (max 5, 입찰 시간 적은 순)
# 이후 새로운 물품 등록 시 알람

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
    await ctx.author.send('안녕하세요 {}'.format(ctx.author.profile)) # 개인 메시지
    await ctx.author.send('안녕하세요 {}'.format(ctx.author.id)) # 개인 메시지
    await ctx.author.send('안녕하세요 {}'.format(type(ctx))) # 개인 메시지

    print(type(ctx))
    print(dir(ctx.author))
    print("hello")

# ctx.author 명령어를 보낸 사람
# ctx.bot 명령어를 포함하는 봇에 대한 정보
# ctx.channel 명령어를 보낸 textchannel
# ctx.command 현재 명령어
# ctx.command_failed 실패 시 True 반환
# ctx.guild 디스코드 서버 정보
# ctx.message 채팅 정보
# ctx.me 봇의 이름과 번호

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
client.run(os.environ['token'])

# terminal test
# from bot_token import JB_APP_TOKEN
# bot_token = JB_APP_TOKEN
# client.run(bot_token)




