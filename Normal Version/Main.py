import discord
from discord.ext import commands
import os
import random

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# List of quotes, associated picture and source URLs.
quotes = [
    {"quote": "You must be the change you wish to see in the world.", 
     "cover_url": "https://img.freepik.com/fotos-premium/bild-von-mahatma-gandhi-in-schwarz-weiss-farbe_789916-4021.jpg",
     "source_url": "https://blog.hubspot.com/sales/famous-quotes"},

  {"quote": "Spread love everywhere you go. Let no one ever come to you without leaving happier.", 
     "cover_url": "https://hips.hearstapps.com/hmg-prod/images/mother-teresa-9504160-1-402.jpg",
     "source_url": "https://blog.hubspot.com/sales/famous-quotes"},

  {"quote": "The only thing we have to fear is fear itself.", 
     "cover_url": "https://cdn.prod.www.spiegel.de/images/89d94ec1-0002-0004-0000-0000d0e3fb5e_w1048_r1_fpx50_fpy55.29.jpg",
     "source_url": "https://blog.hubspot.com/sales/famous-quotes"}
]

@bot.command()
async def ping(ctx):
    await ctx.send('I´m nice at ping pong')

@bot.command()
async def quote(ctx):
    try:
        # Select random quote
        selected_quote = random.choice(quotes)
        quote = selected_quote["quote"]
        cover_url = selected_quote["cover_url"]
        source_url = selected_quote["source_url"]

        # Send message with quote and cover image
        embed = discord.Embed(title='Quote', description=quote, color=0xFFFFFF)
        embed.set_image(url=cover_url)
        if source_url:
            embed.add_field(name="from", value=source_url, inline=False)
        await ctx.send(embed=embed)
    except Exception as e:
        print('Error getting quote', e)
        await ctx.send('An error has occurred. Try again later.')

# Replace "Your DiscordToken" with your actual Discord Token.
bot.run("YourDiscordToken")