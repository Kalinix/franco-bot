from email import message
from typing import AsyncIterable
import discord
import os
from dotenv import load_dotenv
from discord.ext import commands
import random

client = discord.Client()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix='-')

@client.event
async def on_ready():
    print('Conectado como {0.user}'.format(client))

@client.event
async def on_message(message):
    await client.process_commands(message)
    user = str(message.author).split('#')[0]
    user_msg = str(message.content)
    channel = str(message.channel.name)
    print(f'{user}: {user_msg} ({channel})')

    if message.content.startswith('') and message.author.id == 715498111325306900:
        res = random.randint(1 , 4)
        mr=message.reply
        if res == 1:
            await mr('Cállate Aitor')
        elif res == 2:
            await mr('Que te calles')
        elif res == 3:
            await mr('¿Te quieres callar?')
        elif res == 4:
            await mr('Silencio rojo asqueroso')
    
    elif message.content.startswith('') and message.author.id == 720270681589153847:
        res = random.randint(1 , 20)
        mr=message.reply
        if res == 1:
            await mr('Cállate roja')
        elif res == 2:
            await mr('Roja muerta abono pa la huerta')
        elif res == 3:
            await mr('¿No tienes que chupársela a Aitor o algo?')
        elif res == 4:
            await mr('A la cocina')
        elif res == 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20:
            return

@client.command()
@commands.has_guild_permissions(kick_members = True)
async def ping(ctx):
    await ctx.send(f'Pong')

@client.command()
async def limpia(ctx, amount):
    await ctx.channel.purge(limit=int(amount))

@client.command()
@commands.has_permissions(kick_members = True)
async def fusila(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

client.run(TOKEN)