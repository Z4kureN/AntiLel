import discord
from discord.ext import commands
import json

class AntiLol(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.lols = ["lol", "l0l", "|o|", "|0|", ":regional_indicator_l: :regional_indicator_o: :regional_indicator_l:", ":regional_indicator_l::regional_indicator_o::regional_indicator_l:"]

    @commands.Cog.listener()
    async def on_message(self, message):

        if not message.guild:
            return

        member = message.guild.get_member(message.author.id)

        if message.author == self.bot.user:
            return

        with open("data/guilds.json", "r") as f:
            l = json.load(f)

        if str(message.guild.id) not in l:
            return

        if member.guild_permissions.manage_messages:
            if l[str(message.guild.id)]["mods"] == "enabled":
                return

            elif l[str(message.guild.id)]["mods"] == "disabled":
                pass

        for a in self.lols:
            if a.lower() in message.content.lower():
                await message.delete()
                emb = discord.Embed(description = f"Don't say **LOL**! Say **LEL** because it's better!", colour = discord.Colour.red())
                emb.set_footer(text = "This will be deleted in 10 seconds.")
                await message.channel.send(content = f"😡 | {message.author.mention}", embed = emb, delete_after = 10)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):

        if before.author == self.bot.user:
            return

        with open("data/guilds.json", "r") as f:
            l = json.load(f)

        if str(before.guild.id) not in l:
            return

        if before.author.guild_permissions.manage_messages:
            if l[str(before.guild.id)]["mods"] == "enabled":
                return
            elif l[str(before.guild.id)]["mods"] == "disabled":
                pass

        for a in self.lols:
            if a.lower() in after.content.lower():
                await after.delete()
                emb = discord.Embed(description = f"Don't say **LOL**! Say **LEL** because it's better!", colour = discord.Colour.red())
                emb.set_footer(text = "This will be deleted in 10 seconds.")
                await after.channel.send(content = f"😡 | {after.author.mention}", embed = emb, delete_after = 10)


    @commands.command()
    @commands.has_permissions(manage_messages = True)
    @commands.bot_has_permissions(manage_messages = True)
    async def enable(self, ctx):
        
        "Enable the Anti Lol"

        with open("data/guilds.json", "r") as f:
            l = json.load(f)

        # guilds = []
        # for a in l:
        #    guilds.append(a)

        if str(ctx.guild.id) in l:
            emb = discord.Embed(description = f"❌ | **{ctx.guild.name}**'s Anti Lol is already enabled!", colour = discord.Colour.red())
            return await ctx.send(embed = emb)

        l[str(ctx.guild.id)] = {"mods": "enabled"}       

        with open("data/guilds.json", "w") as f:
            json.dump(l, f, indent = 4)

        emb = discord.Embed(description = f"✅ | Anti Lol enabled for **{ctx.guild.name}**.", colour = discord.Colour.red())
        await ctx.send(embed = emb)

    @commands.command()
    @commands.has_permissions(manage_permissions = True)
    @commands.bot_has_permissions(manage_messages = True)
    async def disable(self, ctx):
        
        "Disable the Anti Lol"

        with open("data/guilds.json", "r") as f:
            l = json.load(f)

        if str(ctx.guild.id) not in l:
            emb = discord.Embed(description = f"❌ | Anti Lol is not enabled in **{ctx.guild.name}**!", colour = discord.Colour.red())
            return await ctx.send(embed = emb)

        else:
            l.pop(str(ctx.guild.id))
            with open("data/guilds.json", "w") as f:
                json.dump(l, f, indent = 4)
            emb = discord.Embed(description = f"✅ | Anti Lol disabled for **{ctx.guild.name}**.", colour = discord.Colour.red())
            await ctx.send(embed = emb)

    @commands.command(usage = "[enable | disable]", aliases = ["mod"])
    @commands.has_permissions(manage_messages = True)
    @commands.bot_has_permissions(manage_messages = True)
    async def mods(self, ctx, enable_disable: str):

        "Set if mods can say lol"

        with open("data/guilds.json", "r") as f:
            l = json.load(f)

        if str(ctx.guild.id) not in l:
            emb = discord.Embed(description = f"❌ | Anti Lol is not enabled in **{ctx.guild.name}**! Enable with `enable`", colour = discord.Colour.red())
            return await ctx.send(embed = emb)

        if enable_disable.lower() == "enable":
            if l[str(ctx.guild.id)]["mods"] == "enabled":
                emb = discord.Embed(description = f"❌ | Mods Option is already enabled, mods can send **lol**s!", colour = discord.Colour.red())
                return await ctx.send(embed = emb)
            l[str(ctx.guild.id)]["mods"] = "enabled"

            with open("data/guilds.json", "w") as f:
                json.dump(l, f, indent = 4)

            emb = discord.Embed(description = f"✅ | Mods option enabled for **{ctx.guild.name}**. Mods can now send **lol**s.", colour = discord.Colour.red())
            await ctx.send(embed = emb)

        elif enable_disable.lower() == "disable":
            if l[str(ctx.guild.id)]["mods"] == "disabled":
                emb = discord.Embed(description = f"❌ | Mods Option is already disabled, mods can't send **lol**s!", colour = discord.Colour.red())
                return await ctx.send(embed = emb)
            l[str(ctx.guild.id)]["mods"] = "disabled"

            with open("data/guilds.json", "w") as f:
                json.dump(l, f, indent = 4)

            emb = discord.Embed(description = f"✅ | Mods option disabled for **{ctx.guild.name}**. Mods can't send **lol**s.", colour = discord.Colour.red())
            await ctx.send(embed = emb)

def setup(bot):
    bot.add_cog(AntiLol(bot))