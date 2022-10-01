import discord
import os
import asyncio
from discord.ext import commands

intents = discord.Intents.default().all()
intents.members = True

client = commands.Bot(command_prefix="?", help_command=commands.MinimalHelpCommand, case_insensitive=True, intents=intents)

# cogs
async def load_extensions():
    for filename in os.listdir("./cogs"):
        if filename.endswith(".py"):
            await client.load_extension(f'cogs.{filename [:-3]}')

async def main():
    await load_extensions()
asyncio.run(main())

# on ready event
@client.event
async def on_ready():
    # bot login
    print(f"{client.user} logged in successfully!")

    # bot status
    await client.change_presence (
        activity = discord.Activity (
            type = discord.ActivityType.listening, name = "Sunshine Day"
        )
    )

client.run(os.getenv("TOKEN"))