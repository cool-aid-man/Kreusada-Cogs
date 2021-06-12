import discord

from typing import Literal
from redbot.core.commands import BadArgument

from .formatting import curl

class RaffleSafeMember(object):
    """Used for formatting `discord.Member` attributes safely."""

    def __init__(self, member: discord.Member, obj: Literal["winner", "user"]):
        self.name = member.name
        self.mention = member.mention
        self.id = member.id
        self.display_name = member.display_name
        self.discriminator = member.discriminator
        self.name_and_discriminator = f"{self.name}#{self.discriminator}"

        self.obj = obj

    def __str__(self):
        return self.name

    def __getattr__(self, attr):
        curled = curl(f"{self.obj}.{attr}")
        quote = lambda x: f'"{x}"'
        exc = "{} is not valid! {} has no attribute {}.".format(
            curl(f"{self.obj}.{attr}"), self.obj.capitalize(), quote(attr)
        )
        raise BadArgument(exc)