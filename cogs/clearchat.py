import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Clearchat(commands.Cog):
    """Clear chat function."""
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, help="Delete messages in a text channel.")
    @has_permissions(administrator=True)
    async def clearchat(self, ctx, amount=5):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        await ctx.channel.purge(limit=amount)

    @clearchat.error
    async def clearchat_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")


async def setup(client):
    await client.add_cog(Clearchat(client))