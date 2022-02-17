from ast import Delete
from distutils import command
from email import message
from typing import AsyncIterable
import os, random, discord, time
from dotenv import load_dotenv
from discord.ext import commands



client = discord.Client()

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
client = commands.Bot(command_prefix='-')

@client.event
async def on_ready():
    activity = discord.Game(name='MataRojos Simulator')
    await client.change_presence(status = discord.Status.online, activity = activity)
    print('Conectado como {0.user}'.format(client))

@client.event
async def on_message(message):
    await client.process_commands(message)
    user = str(message.author).split('#')[0]
    user_msg = str(message.content)
    channel = str(message.channel.name)
    print(f'{user}: {user_msg} ({channel})')

    if message.content.startswith('') and message.author.id == 715498111325306900:
        res = random.randint(1 , 20)
        mr=message.reply
        if res == 1:
            await mr('Cállate Aitor')
        elif res == 2:
            await mr('Que te calles')
        elif res == 3:
            await mr('¿Te quieres callar?')
        elif res == 4:
            await mr('Silencio rojo asqueroso')
        elif res == 5 or 6 or 7 or 8 or 9 or 10 or 11 or 12 or 13 or 14 or 15 or 16 or 17 or 18 or 19 or 20:
            return
    
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
async def ping(ctx):
    await ctx.send(f'Aquí estoy, mi tiempo de respuesta es de {round(client.latency * 1000)}ms')

@client.command()
@commands.has_guild_permissions(manage_messages = True)
async def limpia(ctx, amount):
    await ctx.channel.purge(limit=int(amount))

@client.command()
@commands.has_guild_permissions(kick_members = True)
async def fusila(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)

@client.command()
@commands.has_guild_permissions(manage_messages = True)
async def warn(ctx, member :discord.Member, *, reason=None):
    await member.send(f'Has recibido un aviso por la siguiente razón: {reason}. Compórtate para la próxima vez.')
    await ctx.send(f'{member.mention} ha sido advertido por {reason} con éxito', delete_after=4)
    await ctx.message.delete()

@client.command()
async def com(ctx, member:discord.Member, *, mensaje):
    await member.send(f'{mensaje}')
    await ctx.send(f'"{mensaje}" enviado con éxito a {member.mention}', delete_after = 4)
    await ctx.message.delete()

@client.command()
@commands.has_guild_permissions(administrator = True)
async def inv(ctx):
    inv = await ctx.channel.create_invite(max_age = 300)
    await ctx.send('Aquí tienes una invitación ' + str(inv))

@client.command()
@commands.has_guild_permissions(manage_messages=True)
async def warnafk(ctx, member:discord.Member):
    await member.send(f'Has recibido un aviso debido a tu reciente inactividad, esto podría conllevar una expulsión a futuro.')
    await ctx.send(f'Advertencia enviada a {member.mention}.', delete_after = 4)
    await ctx.message.delete()

@client.command()
@commands.has_guild_permissions(manage_messages=True)
async def warnafkog(ctx, member:discord.Member):
    await member.send(f'Has recibido un aviso debido a tu reciente inactividad, debido a tu condición de miembro originario, no será tomada en cuenta, pero estaría bien que te metieras algo más.')
    await ctx.send(f'Advertencia enviada a {member.mention}.', delete_after = 4)
    await ctx.message.delete()

@client.command()
async def pab(ctx, member : discord.Member, mensaje):
    if ctx.author.id == 478617818816839689:
        ctx.send(f'Cállate Pablo')
    else:
        for i in range (0, 9):
            await member.send(f'{mensaje}')
            await ctx.send(str(i + 1 ) + ' mensajes enviados', delete_after = 4)
        await ctx.message.delete()

@client.command()
async def pfp(ctx, member : discord.Member):
    author = member
    pfp = author.avatar_url
    await ctx.send(pfp)
    
@client.command()
async def pfppriv(ctx, member : discord.Member):
    author = member
    pfp = author.avatar_url
    user = ctx.author
    await user.send(pfp)
    
client.run(TOKEN)