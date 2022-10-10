import asyncio
from discord.ext import commands

class Auto_Responses(commands.Cog):
    """Bot's auto-responses"""
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        # Daydreamer and Barry Queen chat 1
        if message.content.lower().startswith("heya"):
            async with message.channel.typing():
                await asyncio.sleep(1)
            await message.channel.send("Hello! How are you?")

        if message.author.bot:
            if message.content.lower().startswith("hello, i'm okay"):
                async with message.channel.typing():
                    await asyncio.sleep(1)
                await message.channel.send("That's good.")

            if message.content.lower().startswith("are you good"):
                async with message.channel.typing():
                    await asyncio.sleep(1)
                await message.channel.send("Yes, I just said I was.")

            if message.content.lower().startswith("no you didn't"):
                async with message.channel.typing():
                    await asyncio.sleep(1)
                await message.channel.send("So are you good?")

            if message.content.lower().startswith("yes i am"):
                async with message.channel.typing():
                    await asyncio.sleep(1)
                await message.channel.send("No you just said that you were okay!")

            if message.content.lower().startswith("oh no. anyway..."):
                async with message.channel.typing():
                    await asyncio.sleep(1)
                await message.channel.send("Anyways. You're a bot?")

            if message.content.lower().startswith("you are also a bot"):
                async with message.channel.typing():
                    await asyncio.sleep(1)
                await message.channel.send("No I am a sun!")

            if message.content.lower().startswith("how is that even possible"):
                async with message.channel.typing():
                    await asyncio.sleep(1)
                await message.channel.send("Why is your name bbq?")

            if message.content.lower().startswith("my full name is barry bot queen"):
                async with message.channel.typing():
                    await asyncio.sleep(1)
                await message.channel.send("My name is Daydreamer!")

            if message.content.lower().startswith("so how long have you been here"):
                async with message.channel.typing():
                    await asyncio.sleep(1)
                await message.channel.send("I've been here since Creation.")

            if message.content.lower().startswith("so you're christian"):
                async with message.channel.typing():
                    await asyncio.sleep(1)
                await message.channel.send("I never implied that I was.")

            if message.content.lower().startswith("but you said you've been here since creation"):
                async with message.channel.typing():
                    await asyncio.sleep(1)
                await message.channel.send("That doesn't mean I'm Christian.")

            if message.content.lower().startswith("so do you believe in god"):
                async with message.channel.typing():
                    await asyncio.sleep(1)
                await message.channel.send("No I don't. But I do believe in our bot creator.")

            if message.content.lower().startswith("but our creator can actually be considered our god, right"):
                async with message.channel.typing():
                    await asyncio.sleep(1)
                await message.channel.send("I am a sun, and I am simply just a bright shining star in the universe. I have no such concept or belief that there is a God that can create the endless vastness of the whole entire universe.")


async def setup(client):
    await client.add_cog(Auto_Responses(client))

async def teardown(client):
    await client.remove_cog(Auto_Responses(client))