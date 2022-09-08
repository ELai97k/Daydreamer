import discord
from discord.ext import commands

class Info(commands.Cog):
    """Custom help command"""
    def __init__(self, client):
        self.client = client

    # default help command custom mod
    @commands.command()
    async def info(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Bot's List of Commands",
            color=0xffd966
        )
        embed.add_field(name="info", 
        value="Alternate help command that you're looking at right now.",
        inline=False)

        embed.add_field(name="help", 
        value="Displays the bot's default help command.",
        inline=False)

        embed.add_field(name="embed", 
        value="Displays a test embed.",
        inline=False)

        embed.add_field(name="ping", 
        value="This command will show the bot's latency in ms (milliseconds).",
        inline=False)

        embed.add_field(name="test", 
        value="This command is a test command.",
        inline=False)

        embed.add_field(name="responses", 
        value="Displays a list of words / phrases / sentences the bot will auto respond to.",
        inline=False)

        embed.add_field(name="heyprompts",
        value="Command for displaying list of options when you type 'hey daydreamer'.",
        inline=False)

        embed.add_field(name="version / botversion / botver",
        value="Python version for the bot.",
        inline=False)

        embed.set_footer(text="Bot functions listed here will be subject to future changes")

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Info(client))