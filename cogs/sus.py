import discord
from discord.ext import commands


class SomeCog(commands.Cog):
    def __init__(self, takaso):
        self.takaso = takaso
        self._previous_message = None


    @commands.command()
    async def first(self, ctx):
        message = await ctx.send("I'll edit this message when you type `$next`")
        self._previous_message = message


    @commands.command()
    async def next(self, ctx):
        if self._previous_message is None: # Exiting if the `test` command wasn't called before, i.e the message is a NoneType
            return await ctx.send("You need to invoke first `$test`")

        await self._previous_message.edit(content="Edited the message")

def setup(takaso):
    takaso.add_cog(SomeCog(takaso))