from disnake import *
from disnake.ext import commands

class PointsSystem2(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message(self,msg:Message):
        if msg.author.bot or not msg.guild:
            return

def setup(bot):
    bot.add_cog(PointsSystem2(bot))
