# CharAlfred.py
# Date: 2025-09-05
# Author: Jamie
#
# Description: A simple Discord bot that responds to a ping command with pong.
#
# Requires discord.py and python-dotenv packages.
# Make sure to set your bot token in a .env file with the variable name TOKEN.

import discord
import os
import json
from dotenv import load_dotenv
from discord.ext import commands

# Load environment variables from a .env file
# Environment variable needs to have TOKEN set to your bot's token
load_dotenv()

#  Set up the bot with command prefix of ! and intents
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

# Define a simple ping command
@bot.command()
async def ping(ctx):
    await ctx.send('pong')

# Run the bot with the token from environment variable (works if uncommented)
# bot.run(os.getenv("TOKEN"))

# Read JSON data from a file
with open("player_data.json", "r", encoding="utf-8") as read_file:
    data = json.load(read_file)

for key, value in data["player"].items():
    print(f"{key}")