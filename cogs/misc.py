import discord
from discord.ext import commands

class Misc(commands.Cog):
    """Cog for basic and misc commands."""
    def __init__(self, client):
        self.client = client

    # test command
    @commands.command(help="This is a test command.")
    async def test(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        await ctx.send("This is a test command.")


    # ping command
    @commands.command(help="Command that shows the bot's latency.")
    async def ping(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        await ctx.send(f"🏓pong! Latency is {round (self.client.latency * 1000)} ms.")


    # test embed
    @commands.command(help="Command for a test embed.")
    async def embed(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Hello world",
            description = "This is a test embed",
            color=0xffc90d
        )
        await ctx.send(embed=embed)


    # user profile pics
    @commands.command(pass_context=True, aliases=["profile", "userprofile", "userpfp", "avatar"], help="Command to show user's profile picture (pfp)")
    async def pfp(self, ctx, *, user:discord.Member=None):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        if user is None:
            user = ctx.author

        embed = discord.Embed(color=discord.Color.blurple())
        try:
            embed.set_image(url=user.avatar.url)
        except:
            embed.set_image(url=str(user.display_avatar.url))
        await ctx.send(embed=embed)
    

    @commands.command(name="version", aliases=["ver"], help="Bot's discord.py version")
    async def _version(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return
        
        await ctx.send(f"My discord.py version is {discord.__version__}")
        print(f"discord.py v{discord.__version__}")

        
    @commands.command(help="Shows the bot's GitHub page.")
    async def github(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return
        github = "https://github.com/ELai97k/Daydreamer"
        await ctx.send(github)


async def setup(client):
    await client.add_cog(Misc(client))

async def teardown(client):
    await client.remove_cog(Misc(client))