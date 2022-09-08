import discord
from discord.ext import commands

class Responses(commands.Cog):
    """Embed that shows what messages the bot auto respond to."""
    def __init__(self, client):
        self.client = client

    # embed showing bot's auto responses
    @commands.command()
    async def responses(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Daydreamer will automatically respond to the following messages:",
            description = "I'm\nI am\nF\nTell me a joke\n:(\nTell me something\nSay something\nPog\nPoggers\nPogchamp\nPing\nBruh\nHello Daydreamer\nHi Daydreamer\nInput\nStupid bot\nDead chat\nTeleport bread\nHey Daydreamer",
            color=0xffd966
        )
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Responses(client))