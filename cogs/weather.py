import discord
from discord.ext import commands
import requests

class Weather(commands.Cog):
    """Weather cog."""
    def __init__(self, client):
        self.client = client

    @commands.command(help="Weather command.")
    async def weather(self, ctx, *, city:str):
        if ctx.author == self.client.user:
            return
        if ctx.author.bot:
            return
        
        api_key = "40196ce69a2157b7e84fd37cd3d90813"
        base_url = "http://api.openweathermap.org/data/2.5/weather?"

        city_name = city
        complete_url = base_url + "appid=" + api_key + "&q=" + city_name
        response = requests.get(complete_url)
        x = response.json()
        channel = ctx.message.channel

        if x["cod"] != "404":
            async with channel.typing():
                y = x["main"]
                current_temperature = y["temp"]
                current_temperature_celsiuis = str(round(current_temperature - 273.15))
                z = x["weather"]
                weather_description = z[0]["description"]

                weather_description = z[0]["description"]
                embed = discord.Embed(
                    title=f"Weather in {city_name}",
                    color=0xffc90d
                )
                embed.add_field(name="Descripition", value=f"**{weather_description}**", inline=False)
                embed.add_field(name="Temperature", value=f"**{current_temperature_celsiuis}°C**", inline=False)
                embed.set_thumbnail(url="https://i.ibb.co/CMrsxdX/weather.png")
                embed.set_footer(text=f"Requested by {ctx.author.name}")
                
                await channel.send(embed=embed)
        else:
            await channel.send("City not found.")


async def setup(client):
    await client.add_cog(Weather(client))

async def teardown(client):
    await client.remove_cog(Weather(client))