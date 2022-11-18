import discord
import datetime
from discord.ext import commands
from discord.ext.commands import has_permissions, MissingPermissions

import json
with open('reports.json', encoding='utf-8') as f:
  try:
    report = json.load(f)
  except ValueError:
    report = {}
    report['users'] = []


class Warnings(commands.Cog):
    """Warnings for members and warn command"""
    def __init__(self, client):
        self.client = client

    # warn command
    @commands.command(pass_context = True)
    @commands.has_role("Moderators")
    @has_permissions(manage_roles=True, kick_members=True, ban_members=True)
    async def warn(self, ctx, user:discord.Member, *reason:str):
        user = ctx.author
        if not reason:
            await ctx.send("Please provide a reason for warning.")
            return
        reason = ' '.join(reason)
        # embed
        embed = discord.Embed (
            title=f"**⚠ WARNING for {user.name}!**",
            description="You have broken one of Da Rules and your warning has been recorded.",
            color=discord.Color.dark_red()
        )
        embed.set_footer(text="If you think this was a mistake, DM or ping Admin or Mods for further discussion.")
        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)
        print(f"{user.name} has been given a warning!")

        for current_user in report['users']:
            if current_user['name'] == user.name:
                current_user['reasons'].append(reason)
                break
            else:
                report['users'].append({
                    'name':user.name,
                    'reasons': [reason,]
                })
            with open('reports.json','w+') as f:
                json.dump(report,f)

            with open('reports.json','w+') as f:
                json.dump(report,f)
            if len(report['users']) >= 3:
                await user.kick(reason=f'{user.name} has reached 3 warnings.')

    @warn.error
    async def warn_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")


    # warnings command
    @commands.command(pass_context = True)
    @commands.has_role("Moderators")
    @has_permissions(manage_roles=True, kick_members=True, ban_members=True)
    async def warnings(self, ctx, user:discord.Member):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        for current_user in report['users']:
            if user.name == current_user['name']:
                embed = discord.Embed (
                    title=f"Warning Report for {user.name}",
                    description=f"Reported {len(current_user['reasons'])} times : {','.join(current_user['reasons'])}"
                )
                await ctx.send(embed=embed)
                #await ctx.send(f"{user.name} has been reported {len(current_user['reasons'])} times : {','.join(current_user['reasons'])}")
                break
            else:
                await ctx.send(f"{user.name} has never been reported.")

    @warnings.error
    async def warnings_error(self, ctx, error):
        if isinstance(error, MissingPermissions):
            await ctx.send("You do not have permission to use this command!")


async def setup(client):
    client.add_cog(Warnings(client))

async def teardown(client):
    client.remove_cog(Warnings(client))