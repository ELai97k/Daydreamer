import asyncio
import random
from discord.ext import commands

class Jokes(commands.Cog):
    """Cog for jokes."""
    def __init__(self, client):
        self.client = client

    @commands.command(help="Command for jokes and puns I guess.")
    async def jokes(self, ctx):
        if ctx.author == self.client.user:
            return
        
        jokes = [
            "What time did Godzilla eat the Japanese Prime Minister? Eight pm.",
            "Want to hear a pizza joke? Never mind, it's too cheesey.",
            "Did you hear about the man who ate a clock? It was time consuming, and he even went back for seconds.",
            "Roti itu semakin bodoh lepas pergi Jepun. Dia s'karang roti baka.",
            "What do you call an alligator in a vest? An in-vest-igator.",
            "What do you call a crocodile that is also a detective? An investi-gator.",
            "Did you hear about the claustrophobic astronaut? He just needed some space.",
            "What do you call a fake noodle? An impasta.",
            "What did the buffalo say when his son left? Bison.",
            "What do you call a psychic little person who has escaped from prison? A small medium at large.",
            "I don't trust stairs. They're always up to something.",
            "I'm done with the VTuber community. They're all rigged.",
            "One windmill asked another windmill, 'What's your favourite genre of music?' The other windmill replied, 'Oh, I'm a big metal fan!'",
            "How many lips does a flower have? Tulips.",
            "Why couldn't the bicycle stand on its own? It was two tired!",
            "Imagine if Americans switched from pounds to kilograms overnight. There would be mass confusion.",
            "What do you call it when Dwayne Johnson buys a cutting tool? Rock pay for scissors.",
            "Why did the scarecrow win an award? He was outstanding in his field!",
            "What board game can you play on your computer? Motherboard.",
            "Do you know what the national fruit is in Paris? The Pear Is."
        ]
        async with ctx.channel.typing():
            await asyncio.sleep(3)
        await ctx.channel.send(f"{random.choice(jokes)}")


    @commands.Cog.listener()
    async def on_message(self, message):
        if message.author == self.client.user:
            return
        
        if message.content.lower().startswith("tell me a joke"):
            jokes = [
                "What time did Godzilla eat the Japanese Prime Minister? Eight pm.",
                "Want to hear a pizza joke? Never mind, it's too cheesey.",
                "Did you hear about the man who ate a clock? It was time consuming, and he even went back for seconds.",
                "Roti itu semakin bodoh lepas pergi Jepun. Dia s'karang roti baka.",
                "What do you call an alligator in a vest? An in-vest-igator.",
                "What do you call a crocodile that is also a detective? An investi-gator.",
                "Did you hear about the claustrophobic astronaut? He just needed some space.",
                "What do you call a fake noodle? An impasta.",
                "What did the buffalo say when his son left? Bison.",
                "What do you call a psychic little person who has escaped from prison? A small medium at large.",
                "I don't trust stairs. They're always up to something.",
                "I'm done with the VTuber community. They're all rigged.",
                "One windmill asked another windmill, 'What's your favourite genre of music?' The other windmill replied, 'Oh, I'm a big metal fan!'",
                "How many lips does a flower have? Tulips.",
                "Why couldn't the bicycle stand on its own? It was two tired!",
                "Imagine if Americans switched from pounds to kilograms overnight. There would be mass confusion.",
                "What do you call it when Dwayne Johnson buys a cutting tool? Rock pay for scissors.",
                "Why did the scarecrow win an award? He was outstanding in his field!",
                "What board game can you play on your computer? Motherboard.",
                "Do you know what the national fruit is in Paris? The Pear Is."
            ]
            async with message.channel.typing():
                await asyncio.sleep(3)
            await message.channel.send(f"{random.choice(jokes)}")


async def setup(client):
    await client.add_cog(Jokes(client))

async def teardown(client):
    await client.remove_cog(Jokes(client))