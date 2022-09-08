import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Clearchats(commands.Cog):
    """Command for clearing messages in text channel"""
    def __init__(self, client):
        self.client = client

    # clear chat in text channel
    @commands.command(pass_context=True, aliases=["deletechats"])
    @has_permissions(manage_messages=True)
    async def clearchats(self, ctx, amount=100):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        channel = ctx.message.channel
        messages = []
        async for message in self.client.logs_from(channel, limit=int(amount) + 1):
            messages.append(message)
            await self.client.delete_messages(messages)
            print(f"Deleting messages in {channel} . . .")

    @clearchats.error
    async def clearchats_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")


def setup(client):
    client.add_cog(Clearchats(client))