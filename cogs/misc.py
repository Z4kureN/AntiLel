import discord
from discord.ext import commands
from datetime import datetime

class Misc(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def invite(self, ctx):

      "Invite the Bot to your server"

      invite = discord.utils.oauth_url(self.bot.user.id, permissions = discord.Permissions(permissions = 92160))

      emb = discord.Embed(title = "Invite Me", url = invite, colour = discord.Colour.red())
      await ctx.send(embed = emb)

    @commands.command()
    async def ping(self, ctx):

      "See if bot is alive"

      pong = round(self.bot.latency * 1000)

      emb = discord.Embed(description = f"**🏓 `{pong}ms`** | {ctx.author.mention} don't ping me, you hurt me<:worried_blob:706848159053250640>!", colour = discord.Colour.red())

      await ctx.send(embed = emb)

    @commands.command(aliases = ["ut"])
    async def uptime(self, ctx):
      uptime = datetime.now() - self.bot.launchtime
      hours, remainder = divmod(int(uptime.total_seconds()), 3600)
      minutes, seconds = divmod(remainder, 60)
      days, hours = divmod(hours, 24)

      uptime = f"{days}d {hours}h {minutes}m {seconds}s"

      emb = discord.Embed(description = f':clock: | {uptime}', colour = discord.Colour.red())
      await ctx.send(embed = emb)

def setup(bot):
    bot.add_cog(Misc(bot))