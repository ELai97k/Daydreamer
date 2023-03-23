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


async def setup(client):
    await client.add_cog(AutoResponses(client))

async def teardown(client):
    await client.remove_cog(AutoResponses(client))