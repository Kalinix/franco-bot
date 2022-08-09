from ast import Delete
import asyncio
from distutils import command
from email import message
from typing import AsyncIterable
import os, random, discord, time
from dotenv import load_dotenv
from discord.ext import commands
from abc import ABCMeta

comandos = '''
-ping
-limpia Borra un número de mensajes.
-fusila Banea a un miembro
-warn Manda a un aviso a un miembro.
-warnafk Manda un aviso predefinido a un miembro por inactividad.
-warnafkog Manda un aviso predefinido a un miembro por inactividad (usar solo en miembros originales).
-com Manda un mensaje personalizado a los DM de un miembro.
-inv Manda una invitación temporal al canal en el que se manda el comando.
-pfp Muestra la foto de perfil de un miembro.
-pfppriv Muestra la foto de perfil de un miembro al DM de quien haya usado el comando (el comando se borra automáticamente).
'''

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
    
    if message.channel.type is discord.ChannelType.private:
        if message.author.id != 853660999558889492:
            user = str(message.author).split('#')[0]
            user_msg = str(message.content)
            log = (f'**{user}:** {user_msg}')
            embed = discord.Embed(title = '', description = log)
            channel = client.get_channel(967781655324549210)
            await channel.send(embed = embed)
    
    else:    
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

@client.command()
async def ping(ctx):
    await ctx.send(f'Aquí estoy, mi tiempo de respuesta es de {round(client.latency * 1000)}ms')

@client.command()
async def limpia(ctx, amount):
    if ctx.author.id == 493802014942429194:
        await ctx.send ('Silencio')
    else:
        await ctx.channel.purge(limit=int(amount))

@client.command()
@commands.has_guild_permissions(kick_members = True)
async def fusila(ctx, member : discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} ha sido fusilado con éxito')

@client.command()
@commands.has_guild_permissions(manage_messages = True)
async def warn(ctx, member :discord.Member, *, reason=None):
    await member.send(f'Has recibido un aviso por la siguiente razón: {reason}. Compórtate para la próxima vez.')
    await ctx.send(f'{member.mention} ha sido advertido por {reason} con éxito', delete_after=4)
    await ctx.message.delete()

@client.command()
async def com(ctx, member:discord.Member, *, mensaje):
    await member.send(f'{mensaje}')
    await ctx.send(f'"{mensaje}" enviado con éxito a {member.mention}', delete_after = 2)
    await ctx.message.delete()

@client.command()
async def anuncia(ctx, channel:discord.TextChannel, *, mensaje):
    await channel.send(f'{mensaje}')
    await ctx.send(f'"{mensaje}" enviado con éxito a en {channel}', delete_after = 2)
    await ctx.message.delete()

@client.command()
@commands.has_guild_permissions(administrator = True)
async def inv(ctx):
    inv = await ctx.channel.create_invite(max_age = 300)
    await ctx.send('Aquí tienes una invitación ' + str(inv))

@client.command()
@commands.has_guild_permissions(manage_messages=True)
async def warnafk(ctx, member1: discord.Member = None, member2: discord.Member = None, member3: discord.Member = None, member4: discord.Member = None, member5: discord.Member = None):
    enviados = ['']

    await member1.send(f'Has recibido un aviso debido a tu reciente inactividad, esto podría conllevar una expulsión a futuro.')
    enviados.append(member1.mention)
    if member2 != None:
        await member2.send(f'Has recibido un aviso debido a tu reciente inactividad, esto podría conllevar una expulsión a futuro.')
        enviados.append(member2.mention)
        
    if member3 != None:
        await member3.send(f'Has recibido un aviso debido a tu reciente inactividad, esto podría conllevar una expulsión a futuro.')
        enviados.append(member3.mention)

    if member4 != None:
        await member4.send(f'Has recibido un aviso debido a tu reciente inactividad, esto podría conllevar una expulsión a futuro.')
        enviados.append(member4.mention)

    if member5 != None:
        await member5.send(f'Has recibido un aviso debido a tu reciente inactividad, esto podría conllevar una expulsión a futuro.')
        enviados.append(member5.mention)

    await ctx.send('Advertencia enviada a' + ' '.join(enviados), delete_after = 2)

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
    await ctx.message.delete()
    
@client.command()
async def info(ctx):
    embed = discord.Embed(title = 'Lista de comandos', description = comandos)
    await ctx.author.send(embed = embed)

@client.command()
async def dm(ctx):
    dm_message = "prueba"
    await ctx.message.delete()
    for member in ctx.guild.members:
        try:
            print (member.id)
            if member.id == 8979879879:
                pass
            else:
                await member.send(dm_message)
                print(f"Sent to {member}")
                # To not be rate limited
                await asyncio.sleep(1)
        except:
            print(f"Couldn't send to {member}")

@client.command()
async def nuke(ctx, channel_name):
    guild = ctx.guild
    existing_channel = discord.utils.get(guild.channels, name=channel_name)
    if existing_channel is not None:
        await existing_channel.clone(reason="Has been nuked")
        await existing_channel.delete()
        await ctx.send(f'Hecho pa')

@client.command()
async def copych(ctx, channel: discord.TextChannel=None):
    if channel is None:
        channel = ctx.channel
    await channel.clone()
    await channel.delete()

    
client.run(TOKEN)