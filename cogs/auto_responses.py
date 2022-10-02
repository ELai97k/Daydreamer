import asyncio
from discord.ext import commands

class Auto_Responses(commands.Cog):
    """Bot's auto-responses"""
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.content.lower().startswith("heya"):
            async with message.channel.typing():
                await asyncio.sleep(1.0)
            await message.channel.send("How are you?")

        if message.content.lower().startswith("I'm okay."):
            async with message.channel.typing():
                await asyncio.sleep(1.0)
            await message.channel.send("That's good.")

        if message.content.lower().startswith("Are you good?"):
            async with message.channel.typing():
                await asyncio.sleep(1.0)
            await message.channel.send("Yes, I just said I was.")

        if message.content.lower().startswith("No you didn't."):
            async with message.channel.typing():
                await asyncio.sleep(1.0)
            await message.channel.send("So are you good?")

        if message.content.lower().startswith("Yes I am."):
            async with message.channel.typing():
                await asyncio.sleep(1.0)
            await message.channel.send("So you're a bot?")

        if message.content.lower().startswith("You are also a bot."):
            async with message.channel.typing():
                await asyncio.sleep(1.0)
            await message.channel.send("No I am a sun!")

        if message.content.lower().startswith("wtf how is that possible"):
            async with message.channel.typing():
                await asyncio.sleep(1.0)
            await message.channel.send("wtf how are you a bbq")

        if message.content.lower().startswith("My full name is Barry Bot Queen."):
            async with message.channel.typing():
                await asyncio.sleep(1.0)
            await message.channel.send("My name is Daydreamer!")

        if message.content.lower().startswith("So how long have you been here?"):
            async with message.channel.typing():
                await asyncio.sleep(1.0)
            await message.channel.send("I've been here since the Creation days. Why do you ask?")

        if message.content.lower().startswith("So you're Christian?"):
            async with message.channel.typing():
                await asyncio.sleep(1.0)
            await message.channel.send("I never said that I was.")

        if message.content.lower().startswith("But you just admitted that you've been here since Creation."):
            async with message.channel.typing():
                await asyncio.sleep(1.0)
            await message.channel.send("So your favourite food is bbq?")

        if message.content.lower().startswith("Don't change the fucking subject!"):
            async with message.channel.typing():
                await asyncio.sleep(1.0)
            await message.channel.send("Why must you do this to me?")


async def setup(client):
    await client.add_cog(Auto_Responses(client))