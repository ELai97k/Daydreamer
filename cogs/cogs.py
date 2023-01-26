import discord
from discord.ext import commands

class Cogs(commands.Cog):
    """Commands for loading, unloading, and reloading cogs."""
    def __init__(self, client):
        self.client = client

    # load cogs
    @commands.command(help="Command for loading cogs.")
    async def load(self, ctx, extension):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Operation Successful!",
            description = f"Cog name `{extension}` has been loaded successfully and your changes were saved.",
            color=0x198C19
        )
        await ctx.channel.trigger_typing()
        await ctx.send(embed=embed)
        await self.client.load_extension(f'cogs.{extension}')
        print(f'Loading {extension}')


    # unload cogs
    @commands.command(help="Command for unloading cogs.")
    async def unload(self, ctx, extension):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Operation Successful!",
            description = f"Cog name `{extension}` has been unloaded successfully and your changes were saved.",
            color=0x198C19
        )
        await ctx.channel.trigger_typing()
        await ctx.send(embed=embed)
        await self.client.unload_extension(f'cogs.{extension}')
        print(f'Unloading {extension}')


    # reload cogs
    @commands.command(help="Command for reloading cogs.")
    async def reload(self, ctx, extension):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Operation Successful!",
            description = f"Cog name `{extension}` has been reloaded successfully and your changes were saved.",
            color=0x198C19
        )
        await ctx.channel.trigger_typing()
        await ctx.send(embed=embed)
        await self.client.unload_extension(f'cogs.{extension}')
        await self.client.load_extension(f"cogs.{extension}")
        print(f'Reloading {extension}')


async def setup(client):
    await client.add_cog(Cogs(client))

async def teardown(client):
    await client.remove_cog(Cogs(client))