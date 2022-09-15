import discord
import os
import asyncio
from discord.ext import commands

intents = discord.Intents().default().all()
intents.members = True

client = commands.Bot(command_prefix="D!", case_insensitive=True, intents=intents)


# cogs
for filename in os.listdir("./cogs"):
    if filename.endswith(".py"):
        client.load_extension(f'cogs.{filename [:-3]}')


# on ready event
@client.event
async def on_ready():
  # bot login
  print(f"{client.user} logged in successfully!")

  # bot default status
  await client.change_presence (
    activity = discord.Activity (
      type = discord.ActivityType.listening, name = "Sunshine Day"
    )
  )


client.run(os.getenv('TOKEN'))