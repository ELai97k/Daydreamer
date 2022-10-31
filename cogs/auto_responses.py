import asyncio
from discord.ext import commands

class Auto_Responses(commands.Cog):
    """Bot's auto-responses"""
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        if message.author.bot:
            return

        if message.content.lower().startswith("oh no"):
            await message.channel.typing()
            await message.channel.send("Anyway...")

async def setup(client):
    await client.add_cog(Auto_Responses(client))

async def teardown(client):
    await client.remove_cog(Auto_Responses(client))