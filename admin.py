import discord
from discord.ext import commands

class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(name='kick')
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, userId):
        user = discord.Object(id=userId)
        await ctx.guild.kick(user)
        await ctx.send(f'Kicked {user}. What the hell is wrong with you?')

    @commands.command(name='ban')
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, userId):
        user = discord.Object(id=userId)
        await ctx.guild.ban(user)
        await ctx.send(f'Banned {user}. No dinner for you tonight.')

    @commands.command(name='unban')
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def unban(self, ctx, userId):
        user = discord.Object(id=userId)
        await ctx.guild.unban(user)
        await ctx.send(f'Unbanned {user}. Now, behave.')

def setup(client):
    client.add_cog(Admin(client))