import discord
from discord.ext import commands
import json
import asyncio

colour = 0xbf794b

class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(hidden = True)
    async def help(self, ctx, *, command: str = None):

        prf = "~"

        error = f'```css\nThat command, "{command}", does not exist!\n```'

        emb = discord.Embed(title = "Help", colour = discord.Colour.red())
        emb.set_thumbnail(url = self.bot.user.avatar_url)
        emb.set_footer(text = f"Need help about a command? Try {prf}help [command]")

        if command:

            cmd = self.bot.get_command(command)

            if not cmd:

                await ctx.send(error)
                return

            if not cmd.hidden:

                if cmd.parent:
                    emb.add_field(value = f'`{prf}{cmd.parent} {cmd.name} {cmd.signature}`', name = cmd.help, inline = False)

                else:
                    emb.add_field(value = f'`{prf}{cmd.name} {cmd.signature}`', name = cmd.help, inline = False)

                if cmd.aliases:
                    aliases = ""

                    for a in cmd.aliases:
                        aliases += f"\n`{a}`"
                    emb.add_field(name = 'Aliases', value = aliases, inline = False)

            try:
                commands = ""

                for a in cmd.commands:

                    commands += f"`{prf}{cmd.name} {a.name} {a.signature}`\n"

                emb.add_field(name = "Subcommands", value = commands, inline = False)

            except:
                pass
            else:
                await ctx.send(error)
                return

            await ctx.send(embed = emb)
            return

        for c in self.bot.commands:

            if not c.hidden:

                antilel = ""

                for a in self.bot.commands:
                    if a.cog_name == "AntiLel":
                        if not a.hidden:
                            antilel += f"`{a.name} {a.signature}` | {a.help}\n"

                            try:

                                for b in a.commands:

                                    antilel += f"`{a.name} {b.name} {b.signature}` | {b.help}\n"

                            except:

                                 pass

                misc = ""

                for a in self.bot.commands:
                    if a.cog_name == "Misc":
                        if not a.hidden:
                            misc += f"`{a.name} {a.signature}` | {a.help}\n"

                            try:

                                for b in a.commands:

                                    misc += f"`{a.name} {b.name} {b.signature}` | {b.help}\n"

                            except:

                                 pass

                emb.description = f"""[Support Server](https://discord.gg/w8cbssP)"""

        emb.add_field(name = "AntiLel", value = antilel, inline = False)
        emb.add_field(name = "Misc", value = misc, inline = False)
        await ctx.send(embed = emb)

def setup(bot):
    bot.add_cog(Help(bot))
