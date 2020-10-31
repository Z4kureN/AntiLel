import discord
from discord.ext import commands 
from gtts import gTTS
from subprocess import call

async def tts(message, author, guild):
        tts = gTTS(text=message, lang='en')
        tts.save("tts.mp3")
        call(["ffplay", "-nodisp", "-autoexit", "tts.mp3"])
        f = open("messages.txt", "a")
        f.write(f"[{str(author)}][{guild}] {message}\n")
        f.close()
        print(message)

class Loud(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self, message):
        await tts(message.content, message.author, message.guild.name)

def setup(bot):
    bot.add_cog(Loud(bot))