import discord
import os
import asyncio
import json
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions
from datetime import datetime

intents = discord.Intents.default().all()
intents.members = True

# for bot warnings
# save warnings
def save_warn(self, ctx, member: discord.Member):
    with open('warns.json', 'r') as f:
        warns = json.load(f)
        warns[str(member.id)] += 1

        with open('warns.json', 'w') as f:
            json.dump(warns, f)

# remove warnings
def remove_warn(ctx, member: discord.Member, amount: int):
    with open('warns.json', 'r') as f:
        warns = json.load(f)
        warns[str(member.id)] -= amount

    with open('warns.json', 'w') as f:
        json.dump(warns, f)

# warning checks
def warns_check(member: discord.Member):
    with open('warns.json', 'r') as f:
        warns = json.load(f)
        warns[str(member.id)]

    return warns

# custom help command
class CustomHelpCommand(commands.HelpCommand):
    # cogs and commands
    async def send_bot_help(self, mapping):
        command_prefix="?"
        embed = discord.Embed(title=f"{client.user.name}'s Cogs & Commands", color=0xffd966)
        description = self.context.bot.description
        if description:
            embed.description = description

        for cog, commands in mapping.items():
            if cog is not None:
                name = cog.qualified_name
                filtered = await self.filter_commands(commands, sort=True)

                if filtered:
                    value = '\u2002 '.join('`' + c.name + '`' for c in commands if not c.hidden)

                    if cog and cog.description:
                        value = '{0}\n{1}'.format(cog.description, value)

                    embed.add_field(name=name, value=value, inline=True)
                    embed.set_footer(text=f"Use {command_prefix}help [cog] or {command_prefix}help [command] for more info.")

        await self.get_destination().send(embed=embed)

    # cog info
    async def send_cog_help(self, cog):
        command_prefix="?"
        embed = discord.Embed (
            title = f"{cog.qualified_name} Commands",
            description = f"{cog.description}\n```{[command.name for command in cog.get_commands()]}```",
            color=0xffd966
        )
        embed.set_footer(text=f"Use {command_prefix}help [command] for more info on a command.")
        await self.get_destination().send(embed=embed)

    # command info
    async def send_command_help(self, command):
        embed = discord.Embed (
            color=0xffd966
        )
        embed.add_field (
            name=f"{command.name}",
            value=command.help,
            inline=False
        )
        await self.get_destination().send(embed=embed)

client = commands.Bot(command_prefix="?", 
help_command=CustomHelpCommand(), 
case_insensitive=True, 
intents=intents)

# cogs
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f'cogs.{filename [:-3]}')

async def main():
    await load_extensions()
asyncio.run(main())

# on ready event
@client.event
async def on_ready():
    # bot login
    print(f"{client.user} logged in successfully!")

    # bot status
    await client.change_presence (
        activity = discord.Activity (
            type = discord.ActivityType.listening, name = "Sunshine Day"
        )
    )

# warn command
@client.command(help="Warn command for Admin and Mods.")
@commands.has_role("Moderators")
@has_permissions(manage_roles=True)
async def warn(ctx, member:discord.Member, *, reason=None):
    if ctx.author == client.user:
        return
    if ctx.author.bot:
        return

    if reason is None:
        return await ctx.send("Pls provide a reason for warning.")

    save_warn(ctx, member)
    embed = discord.Embed (
        title=f"**⚠ WARNING for {member.name}!**",
        description=f"You have been given a warning for ```{reason}```",
        color=discord.Color.dark_red()
    )
    embed.set_footer(text="If you think this was a mistake, DM or ping Admin or Mods for further discussion.")
    embed.timestamp = datetime.datetime.utcnow()
    await ctx.send(embed=embed)
    print(f"{member.name} has been given a warning!")

# warn command error
@warn.error
async def warn_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("You do not have permission to use this command!")

# warnings command
@client.command(help="Number of warnings for users in the server.")
@commands.has_role("Moderators")
@has_permissions(manage_roles=True)
async def warnings(ctx, *, member:discord.Member):
    if ctx.author == client.user:
        return
    if ctx.author.bot:
        return

    warns = warns_check(member)
    await ctx.send(f"{member.name} has {warns} warnings.")

# warnings command error
@warnings.error
async def warnings_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("You do not have permission to use this command!")

# remove warnings from user
@client.command(help="Remove warnings from a user.")
@commands.has_role("Moderators")
@has_permissions(manage_roles=True)
async def removewarn(ctx, *, member:discord.Member, amount: int):
    if ctx.author == client.user:
        return
    if ctx.author.bot:
        return

    if amount is None:
        await ctx.send("Pls specify the number of warnings for me to remove.")

    remove_warn(ctx, member, amount)
    await ctx.send(f"Removed {amount} warnings from {member.name}.")

# remove warn error
@removewarn.error
async def removewarn_error(ctx, error):
    if isinstance(error, MissingPermissions):
        await ctx.send("You do not have permission to use this command!")

client.run(os.getenv("TOKEN"))