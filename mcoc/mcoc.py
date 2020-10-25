from redbot.core import commands, checks, Config
import discord
import random
import json
import os
from .bc import BCB
from .mdtembed import Embed
from .featureds import FEATUREDS
from .featureds import FULL_NAMES
from .featureds import ALIASES
from .portraits import PORTRAITS
from .crystal import CRYSTAL
from discord.utils import get


class Mcoc(commands.Cog):
    """Fun Games and Tools for Marvel Contest of Champions."""
    def __init__(self, bot):
        self.bot = bot
        self.config = Config.get_conf(
            self, identifier=153607829, force_registration=True)
        self.config.register_guild()
        self.config.register_user(roster={})
    
#    def readable_dict(self, dictionary: dict):
#        x = []
#        for key, item in dictionary.items():
#            y = "{0}: {1}".format(key, item)
#            x.append(y)
#            return "\n".join(x)
    
    @commands.group(invoke_without_command=True)
    async def vslink(self, ctx):
        """VanguardSkein invite link."""
        await ctx.send("https://discord.gg/JmCFyq7")

    @commands.group(invoke_without_command=True,)
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def crystal(self, ctx,):
        """Chooses a random champion from MCOC."""
        # author = ctx.message.author
        data = Embed.create(self, ctx, title='You got... :gem:')
        image = (random.choice(CRYSTAL))
        data.set_image(url=image)
        await ctx.send(embed=data)
        
    @commands.group()
    async def battlechip(self, ctx,):
        """Opens a battlechip crystal from MCOC."""
        
    @battlechip.group(invoke_without_command=True)
    @commands.cooldown(1, 10, commands.BucketType.user)
    async def basic(self, ctx):
        """Open a basic battlechip crystal."""
        print("[BCB]",random.__file__)
        key = random.choice(list(BCB.keys()))
        data = Embed.create(self, ctx, title="You got {}!".format(key))
        url = BCB[key]
        image = url
        data.set_image(url=image)
        await ctx.send(embed=data)
    
        
#    @crystal.command(name="roster") #, alias["mychamps"])
#    async def crystal_roster(self, ctx,  roster_champion):
#        """Shows your roster from the champions you've obtained."""
#        if user is None:
#            user = ctx.author
#        try:
#            CRYSTAL = await self.config.user(user).get_raw("roster")
#        except:
#            await ctx.send("{0.display_name} testing".format(user))
#           return
#        roster_list_clean = self.readable_dict(roster_list)
#        await ctx.send("{0.display_name}'s roster:\n{1}".format(user, roster_list_clean))
            
#    @commands.group()
#    async def champ(self, ctx):
#        """Find champion images."""

#    @champ.command()
#    async def featured(self, ctx, alias: str):
#        await ctx.send("`I'm getting this command rebuilt right now!` :star_struck:\nFor more updates, please stay tuned to my support server: https://discord.gg/JmCFyq7")
#        champion = FULL_NAMES.get(alias, alias)
#        try:
#            data = Embed.create(self, ctx, title="Featured Image.".format(
#                champion.capitalize()), image=FEATUREDS[champion.lower()])
#            await ctx.send(embed=data)
#        except KeyError:
#            await ctx.send("`I could not find that champion.`\n`Please check your spelling, or your alias might not be available just yet.` :fearful:\n\n`Additionally, this command has not yet been completed. I'm working on it asap!`")

#    @champ.command()
#    async def portrait(self, ctx, champion: str):
#        champion = FULL_NAMES.get(alias, alias)
#        try:
#            data = Embed.create(self, ctx, title="Portrait Image.".format(
#                champion.capitalize()), image=PORTRAITS[champion.lower()])
#            await ctx.send(embed=data)
#        except KeyError:
#            await ctx.send("`I could not find that champion.`\n`Please check your spelling, or your alias might not be available just yet.` :fearful:\n\n`Additionally, this command has not yet been completed. I'm working on it asap!`")
