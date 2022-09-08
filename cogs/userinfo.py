import discord
from discord.ext import commands
from datetime import datetime

class UserInfo(commands.Cog):
    """Command to fetch user info"""
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def userinfo(self, ctx, *, user: discord.Member = None):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return
        
        if user is None:
            user = ctx.author

        date_format = "%a, %d %b, %Y"
        status = user.status[0]
        statusnames = {"online" : "Online", "dnd" : "Do Not Disturb", "idle" : "Idle", "offline" : "Invisible/Offline"}
        statusemojis = {"online" : "<:online:767294866488295475>", "dnd": "<:dnd:767510004135493662>", "idle" : "<:idle:767510329139396610>", "offline" : "<:invisible:767510747466170378>"}

        embed = discord.Embed (
            title = f"{user} Info",
            color=0xffd966
        )
        embed.set_author(name=str(user), icon_url=user.avatar_url)
        embed.set_thumbnail(url=user.avatar_url)
        embed.add_field(name="Joined", value=user.joined_at.strftime(date_format))

        members = sorted(ctx.guild.members, key=lambda m: m.joined_at)

        embed.add_field(name="Join position", value=str(members.index(user)+1), inline=False)
        embed.add_field(name="Registered", value=user.created_at.strftime(date_format), inline=False)

        if len(user.roles) > 1:
            role_string = ' '.join([r.mention for r in user.roles][1:])
            embed.add_field(name="Roles [{}]".format(len(user.roles)-1), value=role_string, inline=False)

        perm_string = ', '.join([str(p[0]).replace("_", " ").title() for p in user.guild_permissions if p[1]])

        embed.add_field(name="Guild permissions", value=perm_string, inline=False)
        embed.add_field(name="Status:", value=f"{statusemojis[status]} {statusnames[status]}", inline=False)

        embed.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(UserInfo(client))