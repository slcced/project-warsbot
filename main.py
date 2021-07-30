from discord.ext import commands
from discord import Message
from dotenv import load_dotenv
from os import getenv
import discord
import os
import asyncio
import random

load_dotenv() 

client = commands.Bot(command_prefix=".", activity=discord.Game (name="WarFare"), help_command=None)

#events
@client.event
async def on_ready():
    print ("Booting up your system")
    await asyncio.sleep(1)
    print("WarFare is Online!")

@client.command(name='ask')
async def ask(ctx, *, question):
    await ctx.message.delete()
    channel = client.get_channel(825751387534917674)
    embed = discord.Embed(title=f"{ctx.author.name} is asking...", description=question)
    await channel.send(embed=embed)

@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')

@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(getenv("TOKEN"))
