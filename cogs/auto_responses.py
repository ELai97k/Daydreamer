import discord
from discord.ext import commands

class Auto_Responses(commands.Cog):
    """Bot's auto-responses"""
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        if message.content.lower().startswith("heya"):
            await message.channel.typing()
            await message.channel.send("How are you?")

        if message.content.lower().startswith("im okay") or message.content.lower().startswith("i'm okay"):
            await message.channel.typing()
            await message.channel.send("That's good.")


async def setup(client):
    await client.add_cog(Auto_Responses(client))