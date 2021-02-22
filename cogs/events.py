import discord
from discord.ext import commands

class Events(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_guild_join(self, guild):

        ch = self.bot.get_channel(607358470907494420)

        emb = discord.Embed(description = f"""<:join:694105538316992532> | {self.bot.user.mention} joined **{guild.name}**!
🆔 | {guild.id}
👤 | {guild.owner}
🔢 | {guild.member_count} Members
🍰 | Created at {guild.created_at.strftime("%m / %d / %Y (%H:%M)")}""", colour = discord.Colour.green())
        emb.set_footer(text = f"{len(self.bot.guilds)} guilds", icon_url = self.bot.user.avatar_url)
        emb.set_thumbnail(url = guild.icon_url)

        if guild.banner:
            emb.set_image(url = guild.banner_url)

        await ch.send(embed = emb)

    @commands.Cog.listener()
    async def on_guild_remove(self, guild):

        ch = self.bot.get_channel(607358470907494420)

        emb = discord.Embed(description = f"""<:leave:694103681272119346> | {self.bot.user.mention} left **{guild.name}**!
🆔 | {guild.id}
👤 | {guild.owner}
🔢 | {guild.member_count} Members
🍰 | Created at {guild.created_at.strftime("%m / %d / %Y (%H:%M)")}""", colour = discord.Colour.red())
        emb.set_footer(text = f"{len(self.bot.guilds)} guilds", icon_url = self.bot.user.avatar_url)
        emb.set_thumbnail(url = guild.icon_url)

        if guild.banner:
            emb.set_image(url = guild.banner_url)

        await ch.send(embed = emb)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):

        if isinstance(error, commands.CommandNotFound):
            return

        elif isinstance(error, commands.MissingPermissions):
            emb = discord.Embed(description = f"❌ | {ctx.author.mention} you don't have **Manage Messages** permission!", colour = discord.Colour.red())
            return await ctx.send(embed = emb)

        emb = discord.Embed(title = "❌ | Error", description = f"Need help? Join the [Support Server](https://discord.gg/w8cbssP)```py\n{error}\n```", colour = discord.Colour.red())
        emb.set_author(name = ctx.author.display_name, icon_url = ctx.author.avatar_url_as(static_format = "png"))
        await ctx.send(embed = emb)

def setup(bot):
    bot.add_cog(Events(bot))
