import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

class Status(commands.Cog):
    """Bot statuses."""
    def __init__(self, client):
        self.client = client

    @commands.command(help="Set custom bot status.")
    @has_permissions(administrator=True, manage_roles=True)
    async def change_status(self, ctx, type, newstatus=None):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return
        
        types = {
            "playing":discord.ActivityType.playing,
            "watching":discord.ActivityType.watching,
            "listening":discord.ActivityType.listening,
            "default":discord.Activity(type=discord.ActivityType.listening, name="Sunshine Day")
        }
        try:
            await self.client.change_presence(activity=discord.Activity(type=types[type.lower()], name=newstatus))
        except KeyError:
            # invalid status type
            await ctx.send("Invalid status! Unable to display status.")
            return
        await ctx.send("Changed status!")
        
        # if type.lower() == "listening":
        #     await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=newstatus))
        # elif type.lower() == "watching":
        #     await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=newstatus))
        # elif type.lower() == "playing":
        #     await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=newstatus))
        # elif type.lower() == "default":
        #     await self.client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="Sunshine Day"))
        # else:
        #     await ctx.send("Invalid status! Unable to display status.")
        #     return
        # await ctx.send("Changed status!")

    @change_status.error
    async def change_status_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")


async def setup(client):
    await client.add_cog(Status(client))

async def teardown(client):
    await client.remove_cog(Status(client))