import discord
from discord.ext import commands
# import commandHandler
import os
from dotenv import load_dotenv


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.command()
async def load(ctx: commands.Context,extension):
    bot.load_extension(f'cogs.{extension}')
@bot.command()
async def unload(ctx: commands.Context,extension):
    bot.unload_extension(f'cogs.{extension}')

@bot.command()
async def hello(ctx):
    await ctx.channel.send(f"Ola, {ctx.message.author.mention}!")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
 
bot.run(TOKEN)