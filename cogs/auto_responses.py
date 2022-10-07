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


async def setup(client):
    await client.add_cog(Auto_Responses(client))

async def teardown(client):
    await client.remove_cog(Auto_Responses(client))