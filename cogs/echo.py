import discord
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions, CommandError

class Echo(commands.Cog):
    """Control the bot to say anything."""
    def __init__(self, client):
        self.client = client

    # echo
    @commands.command(help="Echo command.")
    @has_permissions(manage_roles=True)
    async def echo(self, ctx, *, channel=None, message=None):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return
        
        if message is None and channel is None:
            await ctx.send("Pls specify a channel and message to type.")

        else:
            await ctx.message.delete()
            await self.client.get_channel(f"{ctx.guild.text_channels}").send(f"{message}")

    @echo.error
    async def echo_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")

        if isinstance(error, CommandError):
            embed = discord.Embed (
                title = "Command Error",
                description = "Pls try again!\n```Could not complete your request!```",
                color = discord.Color.dark_red()
            )
            await ctx.send(embed=embed)
            print(f"{self.client.user} Error 404: Command Error")


async def setup(client):
    await client.add_cog(Echo(client))

async def teardown(client):
    await client.remove_cog(Echo(client))