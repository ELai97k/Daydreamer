import discord
from discord.ext import commands

class Audio(commands.Cog):
    def __init__(self, client):
        self.client = client

    #@commands.command(help="")


async def setup(client):
    await client.add_cog(Audio(client))

async def teardown(client):
    await client.remove_cog(Audio(client))