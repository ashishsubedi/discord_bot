import discord
from discord.ext import commands
import requests
import json
import random

class Game(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command(aliases=['rock_paper','paper_scissors'],description="Rock paper scissor game.")
    async def rps(self,ctx,choice):
        try:
            options = ['paper','scissors','rock']
            uId = options.index(choice)
            bId = random.randint(0,2)
            print(choice,bId)
            if (uId != bId):
                winner = options[bId]+' HAHAHA, I WIN!' if (bId == (uId+1)%3) else options[bId]+' '+ctx.message.author.mention+" is a CHEATERRRRRRRR. COME AT ME AGAIN YOU WANKA!"
            else:
                winner = "You bloody wanker dare drew against me?"

            await ctx.channel.send(winner)
        except:
            await ctx.channel.send(ctx.message.author.mention+", first learn to type correctly loser!")

        

      

def setup(bot:commands.Bot):
    bot.add_cog(Game(bot))