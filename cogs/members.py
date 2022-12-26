import discord
from discord.ext import commands

class Members(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, help="Command to show user's profile picture (pfp)")
    async def pfp(self, ctx, *, user:discord.Member=None):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        if user is None:
            user = ctx.author

        embed = discord.Embed(color=discord.Color.blurple())
        embed.set_image(url=user.avatar.url)

        await ctx.send(embed=embed)


    @commands.command(help="Command to fetch number of members in server.")
    async def server_members(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = f"{ctx.guild.name} Members",
            description = f"👥 {ctx.guild.member_count}",
            color=discord.Color.blurple()
        )

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Members(client))

def teardown(client):
    client.remove_cog(Members(client))