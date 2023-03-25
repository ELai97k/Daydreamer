import random
import asyncio
from discord.ext import commands

class Facts(commands.Cog):
    """Cog for fun facts."""
    def __init__(self, client):
        self.client = client

    @commands.command(help="Command for random fun facts.")
    async def fact(self, ctx):
        if ctx.author == self.client.user:
            return
        
        facts = [
            "I was the first Discord bot that `my creator` created to learn Discord bot programming.",
            "`My creator` used discord.js for Discord bot programming before converting to discord.py.",
            "`My creator` is a dumb idiot.",
            "`My creator` likes Linkin Park.",
            "`My creator` can memorise song lyrics than any of their homework or assignments in their lifetime.",
            "`My creator` likes writing poems to express themselves.",
            "`My creator's` most played game is Team Fortress 2, with 124 hrs on record.",
            "`My creator's` favourite game from Valve is Portal 2.",
            "`My creator's` favourite movie of all time is 'Ip Man' from 2008.",
            "`My creator's` favourite song of all time is 'Leave Out All The Rest' by Linkin Park.",
            "`My creator's` favourite game from the Xbox 360 is Forza Horizon 1.",
            "`My creator's` favourite game series from Nintendo is Animal Crossing.",
            "`My creator's` favourite childhood anime is 'Keroro Gunso' or 'Sergeant Frog' in English dubs.",
            "`My creator's` favourite colour is blue.",
            "`My creator's` favourite superhero is Spider-Man.",
            "`My creator's` first video game ever was Age Of Empires 1.",
            "`My creator's` favourite online PC game from the 2000s era is MapleStory and Club Penguin.",
            "`My creator's` favourite video game character of all time is Aigis from Persona 3.",
            "Question: are you tired of these fun facts about `my creator`?",
            "Question: are you tired of these fun facts about `my creator` yet?",
            "Singapore used to be a part of Malaysia before they broke off from the federation on 9 August, 1965. This date became Singapore's Independence Day.",
            "Malaysia has 13 states, 3 of which are Federal Territories, meaning that they are governed directly by the Federal Government of Malaysia.",
            "Did you know? There are so many game engines to choose from to start making games! Which made `my creator` overwhelmed (and a lazy ass).",
            "Bahasa Malaysia and Bahasa Indonesia are incredibly similiar, so we can mutally speak and understand each other. Bahasa means langauge.",
            "Before Among Us, there was TellTale's The Wolf Among Us."
        ]
        async with ctx.channel.typing():
            await asyncio.sleep(3)
        await ctx.channel.send(f"{random.choice(facts)}")


async def setup(client):
    await client.add_cog(Facts(client))

async def teardown(client):
    await client.remove_cog(Facts(client))