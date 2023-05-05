from discord.ext import commands
import random

class Code_Experimentation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def cipher(self, ctx, *, input, shift=random.randrange(1, 27)):
        original_string = input
        encrypted_output = ''

        for char in original_string:
            encrypted_character = chr(ord(char) + shift)
            encrypted_output += encrypted_character
        await ctx.send(f"Input: {input}\nOutput: {encrypted_output}")


def setup(client):
    client.add_cog(Code_Experimentation(client))