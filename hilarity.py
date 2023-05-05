import random
from discord.ext import commands

class Hilarity(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def simp(self, ctx):
        await ctx.send('horny jail. now.')

    @commands.command()
    async def vibecheck(self, ctx):
        iVibes = random.randrange(1, 101)
        await ctx.send(iVibes)

    @commands.command()
    async def dimitrescu(self, ctx):
        sSimp = "🤤🤤🤤"
        await ctx.send(sSimp)

    @commands.command()
    async def funny(self, ctx):
        sFunnyResponses = ["I'm gonna throw my trash away.",
                           "Sorry, guys. Papa John really did somethin' to me.",
                           "You can never fix what was never whole in the first place.",
                           "Always look on the bright side of life!",
                           "I'm here, you twat!",
                           "You're funny",
                           "I don't have anything funny to say here, but you know what *isn't* funny? MAPs.",
                           "cock",
                           "b!funny",
                           "This is an inside joke.",
                           "ligma",
                           "What's 10 in Spanish?",
                           "Yeah, I have an edgy sense of humor. *racism*"]
        await ctx.send(random.choice(sFunnyResponses))

    @commands.command()
    async def succ(self, ctx):
        await ctx.send('https://cdn.discordapp.com/attachments/781180611510534167/842118802996723789/succ.mp4')

    @commands.command()
    async def sex(self, ctx):
        await ctx.send("🤨")


def setup(client):
    client.add_cog(Hilarity(client))