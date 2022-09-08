import discord
import random
from discord.ext import commands, tasks


class Bot_Statuses(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.random_status_loop.start()

    # bot watching statuses
    @tasks.loop(seconds=999.0)
    async def random_status_loop(self):
        status = [
            "this server",
            "the sun",
            "the moon",
            "the stars",
            "paint dry",
            "Youtube",
            "Netflix",
            "Matatabi Movie Labo",
            "からめる",
            "マタタビムービーラボ"
        ]
        await self.client.change_presence (
            activity = discord.Activity (
                type = discord.ActivityType.watching, name = f'{random.choice(status)}'
            )
        )


def setup(client):
    client.add_cog(Bot_Statuses(client))