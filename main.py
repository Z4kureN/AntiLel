import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
from datetime import datetime

bot = commands.AutoShardedBot(command_prefix = commands.when_mentioned_or("~"), case_insensitive = True, description = "Delete all messages that contain a lel!")
bot.launchtime = datetime.now()
bot.remove_command("help")
bot.load_extension("jishaku")

@bot.event
async def on_ready():
    print("Ready as", bot.user)
    await bot.change_presence(status = discord.Status.dnd, activity = discord.Activity(type = discord.ActivityType.listening, name = "LUL is better!"))

for a in os.listdir("./cogs"):
    if a.endswith(".py"):
        bot.load_extension(f"cogs.{a[:-3]}")

load_dotenv(dotenv_path=".env")
token = os.environ.get("token")
bot.run(token)
