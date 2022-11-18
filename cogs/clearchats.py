import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class ClearChats(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    @commands.has_role("Moderators")
    @has_permissions(manage_messages=True)
    async def clearchat(self, ctx, amount=None):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        if amount is None:
            await ctx.send("Pls enter amount of messages for me to clear.")

        else:
            await ctx.channel.purge(limit=amount)
            #await self.client.get_channel(961934795460444231).send(f"Clearing messages in {ctx.channel.name}.")
            embed = discord.Embed(title="Operation Successful!", description=f"Clearing messages in {ctx.channel.name}.", color=0x198C19)
            await ctx.send(embed=embed)

    @clearchat.error
    async def clearchat_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")


async def setup(client):
    await client.add_cog(ClearChats(client))

async def teardown(client):
    await client.remove_cog(ClearChats(client))