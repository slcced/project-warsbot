from discord.ext import commands
import discord
import asyncio
from datetime import datetime


class IamRoles(commands.Cog):

    def __init__(self, client):
        self.client = client

#commands
    @commands.command(name='iam')
    async def iam(self, ctx, *, role: discord.Role):
        await ctx.message.delete()
        print(role)
        day = datetime.today().strftime('%A')
        if str(role.colour) == '#f00000':
            await ctx.author.add_roles(role)
            await ctx.author.edit(nick=f"[{role.name}/Member] {ctx.author.name}")
            

def setup(client):
     client.add_cog(IamRoles(client))
     print('iam command has loaded')