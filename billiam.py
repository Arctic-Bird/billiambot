import discord
import datetime
import random
from discord.ext import commands, tasks
from itertools import cycle

client = commands.Bot(command_prefix='b!', intents=discord.Intents.all())
status = cycle(['Apex Legends', 'Minecraft', 'ROBLOX', 'Call of Duty®: Modern Warfare®', "Tom Clancy's Rainbow Six Siege"])

# Bot is ready notification
@client.event
async def on_ready():
    change_status.start()
    print("Howdy y'all")

    channel = client.get_channel(781180611510534167)
    await channel.send("howdy y'all")

# Ping!
@client.command()
async def ping(ctx):
    await ctx.send(f'your ping is {round(client.latency * 1000)}ms')

# Status changes
@tasks.loop(minutes=30)
async def change_status():
    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game(next(status)))

# Member joining notification
@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

# Member leaving notification
@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

# Load cogs
@client.command()
async def load(ctx, extension):
    await client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Extension loaded!')

# Unload cogs
@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')
    await ctx.send(f'Extension unloaded!')

# Reload cogs
@client.command()
async def reload(ctx, extension):
    await client.unload_extension(f'cogs.{extension}')
    await client.load_extension(f'cogs.{extension}')
    await ctx.send(f'Extension successfully reloaded!')

# 8-ball command and responses
@client.command(aliases=['8ball'])
async def _8ball(ctx, *, sQuestion):
    s8BallResponses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful.",
                 "Maybe someday.",
                 "What?",
                 "beep boop code no work sorry",
                 "Error 404",
                 "Uhhhhhhhhhhhhhhhhhh",
                 "Of course!",
                 "I don't see why not.",
                 "I fail to comprehend your question, mortal.",
                 "Nothing.",
                 "leedle leedle leedle lee",
                 "No, fellow Discord user, mayonnaise is not an instrument.",
                 "What am I, some sort of magic conch shell?",
                 "This post was fact checked by REAL American patriots!"]
    if "do you like black people" == sQuestion:
        await ctx.send("yes, what the fuck? do you think i'm racist?!")
    elif "it's so sad that steve jobs died of ligma" == sQuestion:
        await ctx.send("who is steve jobs?")
    elif "deez" in sQuestion:
        await ctx.send("deez nuts")
    elif "candice" in sQuestion:
        await ctx.send("candice dick fit in your mouth")
    elif "rhydon" in sQuestion:
        await ctx.send("rhydon deez nuts")
    elif "sugma" in sQuestion:
        await ctx.send("sugma nuts")
    elif "ligma" in sQuestion:
        await ctx.send("ligma balls")
    elif "sugondese" in sQuestion:
        await ctx.send("sugondese balls")
    else:
        await ctx.send(f'Question: {sQuestion}\nAnswer: {random.choice(s8BallResponses)}')
    return

# Clear command
@client.command()
async def clear(ctx, iClearAmount=5):
    await ctx.channel.purge(limit=iClearAmount)

# Hello command and responses
@client.command()
async def hello(ctx):
    sHelloResponses = [":eye:",
                 "Hello! How are you?",
                 "I would rather not speak right now.",
                 "I'm busy.",
                 "Sorry! Can't hear ya!",
                 "What year is it?",
                 "hi"]
    await ctx.send(f'{random.choice(sHelloResponses)}')

# Pog, goodnight, & pensive reaction
@client.event
async def on_message(sMessage):
    await client.process_commands(sMessage)

    cEmoji = '<:pogchamp:740784164176920657>'
    if sMessage.author == client.user:
        return

    if 'pog' in sMessage.content.lower():
        await sMessage.add_reaction(cEmoji)

# Coin flip command
@client.command()
async def coinflip(ctx):
    sCoinFlip = ["Heads",
                 "Tails"]
    await ctx.send(random.choice(sCoinFlip))

# Year command
@client.command(aliases=['2023'])
async def year(ctx):
    currentYear = datetime.date.today().year
    sYearReaction = '<:currentyear:747454483579011132>'
    await ctx.send(f"The current year is: {currentYear} {sYearReaction}")

# Curdling command
@client.command()
async def curdling(ctx):
    eCurdling = discord.Embed(
        title='The Curdling',
        description="I'm gonna go throw my trash away! Oh my God, I'm so sorry, I-I'll go get some paper towels! Oh my gosh, I have to get to class, I'm sorry! That cretin knows not what he's invoked. Hey man, what's up? Nothin' much, how 'bout you? Ah, you know. School. Ah. Actually, I spilled this guy's milk during lunch yesterday, and I felt really bad. O-Oh, did you... did you help him clean it up? No, the bell rang before I could help him, and I'm sure he understood, but... I don't know, he felt kinda suspicious. W-What do you mean? I don't know. What is it? Oh, nothing, nothing. Alright, uh, I'll see you later man. ME taking it the wrong way... heh heh heh... how rich. Now, let us look through your personal life, shall we? Any address-oriented slip-ups here and there? Oh... OH... It's YOU, too. And she lives two doors down from me, too. Heh heh heh... What is this? If you want to see her again, consider this an invitation. We're in the shed behind the brick house two doors down from her place. See you soon. My God.",
        colour=discord.Colour.blue()
    )
    eCurdling.set_image(url='https://cdn.discordapp.com/attachments/739188472820269169/750080923025932288/my_god.png')
    await ctx.send(embed=eCurdling)

# Curdling 2 command
@client.command()
async def curdling2(ctx):
    eCurdling_2 = discord.Embed(
        title='The Curdling Part 2',
        description="Hello there. Dude, what the hell?! You showed me neglect I've encountered far too often in this uncaring world, and for that I knew I needed to make you pay for being the straw to break this camel's back! Are you talking about when I accidentally spilled your milk? Precisely! You, who had not the consideration to keep your attention focused, deprived me of necessary nourishment!! Dude, you're literally crying over spilled milk. Well, maybe you too would make mountains out of molehills if you knew how many it took to make unstable ground!! I'LL SCOOP YOUR EYES OUT! Oh my God, thank you so much, I was so scared! It was the right thing to do. What are you proving right now? NOTHING! You and your worthless girlfriend- Actually, we're just friends now- IRRELEVANT! SILENCE! Prove it, then. Prove to me, why you're allowed to go play the hero while I've never been given the chance to make anything of myself! Maybe because I didn't plot an insane revenge plan over literal milk? You think you're so high and mighty. You'd be surprised at how easy it is to come crashing DOWN! Got milk? Well then, I guess years of isolation can really do that to a person. This really says something about our mental state of plenty of people across the nation, and stuff like this actually can really happen. Who cares though, you're a hero dude! EVERYWHERE YOU LOOK",
        colour=discord.Colour.blue()
    )
    eCurdling_2.set_image(url='https://cdn.discordapp.com/attachments/782781498230308864/782784610173976636/curdle.gif')
    await ctx.send(embed=eCurdling_2)

@client.command()
async def lactose(ctx):
    sLactoseURL = 'https://www.youtube.com/channel/UCvk_r-B51sUKDNQ_8g-W7Qw'
    await ctx.send(f'Subscribe to Lactose Films! \n{sLactoseURL}')

# Die command
@client.command()
async def die(ctx):
    sDieEmoji = '<:die:750436277026816120>'
    await ctx.send(sDieEmoji)

# Smile command
@client.command()
async def smile(ctx):
    eSmilingWalter = discord.Embed(
        title='Smile!',
        colour=discord.Colour.gold()
    )
    eSmilingWalter.set_image(url='https://cdn.discordapp.com/attachments/739188472820269169/751171885332561980/walter.png')
    await ctx.send(embed=eSmilingWalter)

# Frown command
@client.command()
async def frown(ctx):
    eFrowningWalter = discord.Embed(
        title = "What hope is left?",
        colour = discord.Colour.darker_grey()
    )
    eFrowningWalter.set_image(url='https://cdn.discordapp.com/attachments/739188472820269169/753026189786087424/fisheyewalter.png')
    await ctx.send(embed=eFrowningWalter)

# Cringe command
@client.command()
async def MemberCringe(ctx, sMember : discord.Member):
        eMemberCringe = discord.Embed(
            title=f'{sMember} is Cringe',
            colour=discord.Colour.dark_red()
        )
        eMemberCringe.set_image(url = 'https://cdn.discordapp.com/attachments/739188472820269169/751170201277431808/cringe.png')
        await ctx.send(embed = eMemberCringe)


@client.command()
async def StrCringe(ctx, *, sNoun):
    eStringCringe = discord.Embed(
        title = f'{sNoun} is Cringe',
        colour = discord.Colour.dark_red()
    )
    eStringCringe.set_image(url = 'https://cdn.discordapp.com/attachments/739188472820269169/751170201277431808/cringe.png')
    await ctx.send(embed = eStringCringe)

@client.command()
async def NotCringe(ctx, sMember : discord.Member):
    memberNotCringe = discord.Embed(
        title=f'{sMember} is Not Cringe!',
        colour=discord.Colour.purple()
    )
    memberNotCringe.set_image(url='https://cdn.discordapp.com/attachments/781180611510534167/962194719499243540/not_cringe.png')
    await ctx.send(embed=memberNotCringe)

@client.command()
async def funnysong(ctx):
    eFunnySong = discord.Embed(
        title = "haha funny song",
        description = "https://youtu.be/gNkKq9mVeVc",
        colour = discord.Colour.orange()
    )
    await ctx.send(embed = eFunnySong)

# Error-handling
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.errors.MissingRequiredArgument):
        await ctx.send("Please enter all of the required arguments.")
    elif isinstance(error, commands.errors.CommandNotFound):
        await ctx.send("This command does not exist.")
    elif isinstance(error, commands.errors.MemberNotFound):
        await ctx.send("This member does not exist. Try ``@[member]``")
    else:
        raise error

@client.command()
async def guyslook(ctx):
    await ctx.send("https://youtu.be/xSxV9PTZlwA")

client.run('NzM5MTcyMDY0MDA2NzY2Njcy.XyWloQ.BOkOBU63fmPMcmkmhOhwkeeid_A')
