from discord.ext import commands
import discord
import asyncio

class help(commands.Cog):

    def __init__(self, client):
        self.client = client
#############################
#Code here
#############################
def setup(client):
     client.add_cog(help(client))
     print('help command has loaded')