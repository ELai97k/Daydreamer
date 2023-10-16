import random
from discord.ext import commands

class AutoResponses(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        if message.content.lower().startswith("good morning"):
            await message.channel.typing()
            await message.channel.send(f"Good morning {message.author.name}!")

        if message.content.lower().startswith("good afternoon"):
            await message.channel.typing()
            await message.channel.send(f"Good afternoon {message.author.name}!")

        if message.content.lower().startswith("good evening"):
            await message.channel.typing()
            await message.channel.send(f"Good evening {message.author.name}!")

        if message.content.lower().startswith("good night") or message.content.lower().startswith("goodnight") or message.content.lower().startswith("good nite") or message.content.lower().startswith("goodnite") or message.content.lower().startswith("gnite"):
            await message.channel.typing()
            await message.channel.send(f"Good night {message.author.name}!")

        if message.content.lower().startswith("everybody do what youre doing") or message.content.lower().startswith("everybody do what you're doing") or message.content.lower().startswith("everybody do what ur doing") or message.content.lower().startswith("every body do what youre doing") or message.content.lower().startswith("every body do what you're doing") or message.content.lower().startswith("every body do what ur doing"):
            await message.channel.typing()
            await message.channel.send("Smile will make a sunshine day!")

        if ":(" in message.content.lower():
            await message.channel.typing()
            await message.channel.send("Turn that frown upside down!")

            reply_message = await self.client.wait_for("message")
            if "no" in reply_message.content.lower():
                await message.channel.typing()
                await message.channel.send("How dare you!")

            if ":)" in reply_message.content.lower():
                await message.channel.typing()
                await message.channel.send("Excellent!")

            if "(:" in reply_message.content.lower():
                await message.channel.typing()
                await message.channel.send("Very good!")

            if "):" in reply_message.content.lower():
                await message.channel.typing()
                await message.channel.send("I'll burn you!")


        if "e" in message.content and "!" not in message.content and message.author.id != 696008187991687189:
            chance = random.randint(1, 190)
            responses = [
                "What's going on here?",
                "What is going on here?",
                "yes",
                "Yes",
                "no",
                "No",
                "whatever",
                "Whatever",
                "I thought you did",
                "Okay",
                "okay",
                "Ok",
                "ok",
                "Oh",
                "oh",
                "Oh okay",
                "oh okay",
                "Hi",
                "hi",
                "Hi there",
                "hi there",
                "Hello",
                "hello",
                "hello there",
                "Hello there",
                "Hello world",
                "hello world",
                "Are you still there?",
                "I see you",
                "Help",
                "help",
                "Help?",
                "help?",
                "Help me",
                "help me",
                "Help me?",
                "help me?",
                "cough",
                "aaaaaaaaaaaaaaaaa",
                "waaaaaaaaaaaaaaaaa"
            ]
            if chance == 76:
                await message.channel.send(random.choice(responses))


async def setup(client):
    await client.add_cog(AutoResponses(client))

async def teardown(client):
    await client.remove_cog(AutoResponses(client))