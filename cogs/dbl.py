import dbl
import discord
from discord.ext import commands

class TopGG(commands.Cog):
  
    """Handles interactions with the top.gg API"""

    def __init__(self, bot):

        self.bot = bot
        self.token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjY0MzUwMDE4NTU5MDE2OTYxMSIsImJvdCI6dHJ1ZSwiaWF0IjoxNTc0ODgwNzIxfQ.QbyEoH83fuS9liuYlg6G0lEn3fSeT_fe6hNImzIwnHc'
        self.dblpy = dbl.DBLClient(self.bot, self.token, autopost = True)

    async def on_guild_post():

        print("Server count posted successfully")

def setup(bot):
    bot.add_cog(TopGG(bot))