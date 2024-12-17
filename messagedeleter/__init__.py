from redbot.core.bot import Red
from redbot.core.utils import get_end_user_data_statement

from .messagedeleter import MessageDeleter

__red_end_user_data_statement__ = get_end_user_data_statement(__file__)


async def setup(bot: Red):
    await bot.add_cog(MessageDeleter(bot))
