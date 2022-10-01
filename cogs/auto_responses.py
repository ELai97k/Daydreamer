import discord
from discord.ext import commands

class Auto_Responses(commands.Cog):
    """Bot's auto-responses"""
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.lower().startswith("bot how are you"):
            await message.channel.typing()
            await message.channel.send("I'm good! How about you?")

        if message.content.lower().startswith("im good") or message.content.lower().startswith("i'm good"):
            await message.channel.typing()
            await message.channel.send("That's good.")


async def setup(client):
    await client.add_cog(Auto_Responses(client))