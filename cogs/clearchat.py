import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Clearchat(commands.Cog):
    """Clear chat function."""
    def __init__(self, client):
        self.client = client

    @commands.command(pass_context=True, help="Delete messages in a text channel.")
    @has_permissions(administrator=True)
    async def clearchat(self, ctx, amount):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        if amount is None:
            await ctx.get_channel(961934795460444231).send("Deleting messages.")
            await ctx.channel.purge(limit=5)

        elif amount == "all":
            await ctx.get_channel(961934795460444231).send("Deleting all messages.")
            await ctx.channel.purge()

        else:
            await ctx.get_channel(961934795460444231).send(f"Deleting {amount} messages.")
            await ctx.channel.purge(limit=int(amount))

    @clearchat.error
    async def clearchat_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")


async def setup(client):
    await client.add_cog(Clearchat(client))