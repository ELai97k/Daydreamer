import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Echo(commands.Cog):
    """Cog for echo command."""
    def __init__(self, client):
        self.client = client

    # say command for admin only
    @commands.command(help="Control the bot to say anything.")
    @has_permissions(administrator=True)
    async def echo(self, ctx, *, message=None):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        if message is None:
            await ctx.send("What do you want me to say?")

        else:
            await self.client.get_channel(1010841256294875218).send(f"{message}")
            await ctx.message.delete()

    @echo.error
    async def echo_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")


async def setup(client):
    await client.add_cog(Echo(client))