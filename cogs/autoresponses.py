from discord.ext import commands

class AutoResponses(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return

        if message.content.lower().startswith("good morning"):
            await message.channel.trigger_typing()
            await message.channel.send(f"Good morning {message.author.name}!")

        if message.content.lower().startswith("good afternoon"):
            await message.channel.trigger_typing()
            await message.channel.send(f"Good afternoon {message.author.name}!")


async def setup(client):
    await client.add_cog(AutoResponses(client))

async def teardown(client):
    await client.remove_cog(AutoResponses(client))