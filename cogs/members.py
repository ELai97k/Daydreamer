import discord
from discord.ext import commands

class Members(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True)
    async def pfp(self, ctx, *, member:discord.Member=None):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        if member is None:
            member = ctx.author

        embed = discord.Embed(color=discord.Color.blurple)
        embed.set_image(url=ctx.author.avatar.url)

        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Members(client))

async def teardown(client):
    await client.remove_cog(Members(client))