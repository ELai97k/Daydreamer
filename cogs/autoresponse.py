import discord
from discord.ext import commands

class Autoresponse(commands.Cog):
    """Cog for the bot's auto-responses."""
    def __init__(self, client):
        self.client = client

    # auto responses off
    @commands.command(pass_context=True, help="Turn off bot's auto-responses.")
    async def autoresponse_off(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Operation Successful!",
            description = "`Auto-Responses` has been turned **OFF** and your changes were saved.",
            color=0x198C19
        )
        await ctx.send(embed=embed)
        await self.client.unload_extension("cogs.auto_responses")
        print("Auto responses has been turned off")


    # auto responses on
    @commands.command(pass_context=True, help="Turn on bot's auto-responses.")
    async def autoresponse_on(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Operation Successful!",
            description = "`Auto-Responses` has been turned **ON** and your changes were saved.",
            color=0x198C19
        )
        await ctx.send(embed=embed)
        await self.client.load_extension("cogs.auto_responses")
        print("Auto responses has been turned on")


    # embed showing bot's auto responses
    @commands.command(help="Embed that shows what messages the bot will auto-respond to.")
    async def responses(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "Daydreamer will automatically respond to the following messages:",
            description = "I'm\nI am\nF\nTell me a joke\n:(\nTell me something\nSay something\nPog\nPoggers\nPogchamp\nPing\nBruh\nHello Daydreamer\nHi Daydreamer\nInput\nStupid bot\nDead chat\nTeleport bread\nHey Daydreamer",
            color=0xffd966
        )
        await ctx.send(embed=embed)


    # hey daydreamer prompts and responses
    @commands.command(help="Command embed to find out what you can input when you trigger 'hey daydreamer' in message.")
    async def heyprompts(self, ctx):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return

        embed = discord.Embed (
            title = "List of available options when typing 'hey daydreamer'",
            color=0xffd966
        )
        # how are you
        embed.add_field(name="Ask how is Daydreamer", 
        value="**Prompts:** 'how are you', 'how are you doing'",
        inline=False)

        # features
        embed.add_field(name="Ask about Daydreamer's functions / features", 
        value="**Prompts:** 'what can you do', 'what are your features', 'what are your functions'",
        inline=False)

        # tell me about yourself
        embed.add_field(name="Ask Daydreamer to introduce himself", 
        value="**Prompts:** 'tell me about yourself', 'who are you', 'what are you'",
        inline=False)

        # what are you doing right now
        embed.add_field(name="Ask Daydreamer what he's doing", 
        value="**Prompts:** 'what are you doing right now', 'what are you doing now', 'what are you doing', 'what you doing', 'whatcha doin', 'whatcha doing', 'what'cha doin', 'what'cha doing', 'what are you doing currently', 'what are you currently doing'",
        inline=False)

        # talk to me
        embed.add_field(name="Make Daydreamer talk to you", 
        value="**Prompts:** 'talk to me', 'talk to me pls', 'pls talk to me', 'can you talk to me', 'can you pls talk to me', 'can ypu talk to me pls'",
        inline=False)
        
        # time
        embed.add_field(name="Ask Daydreamer about the time. (in GMT+8)",
        value="**Prompts:** 'whats the time', 'whats the time now', 'what's the time', 'what's the time now', 'what is the time', 'what is the time now', 'what time is it'",
        inline=False)

        # Isaac Asimov's Laws of Robotics
        embed.add_field(name="Ask Daydreamer about the Laws of Robotics",
        value="**Prompts:** 'tell me about robot laws', 'tell me about the robot laws', 'what are the robot laws', 'what are the laws of robotics'",
        inline=False)

        # you're / ur responses
        embed.add_field(name="hey daydreamer + you're / ur",
        value="stupid, dumb, dum, a dumbass, useless, not helpful, not helping, a good bot, a clever bot, a cleverbot, a smart bot",
        inline=False)

        await ctx.send(embed=embed)


async def setup(client):
    await client.add_cog(Autoresponse(client))