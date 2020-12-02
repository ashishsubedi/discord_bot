import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import random
import ctypes
import ctypes.util
 
print("ctypes - Find opus:")
a = ctypes.util.find_library('opus')
print(a)
discord.opus.load_opus(a)
if not discord.opus.is_loaded():
    print('Opus failed to load')


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

helloList = ["Marhaba",
"Grüß Gott",
"Namaskar",
"Zdraveite",
"Hola",
"Hafa adai",
"Nǐ hǎo",
"Dobro Jutro",
"Dobar dan",
"Dobra većer",
"God dag",
"Hoi",
"Hallo",
"hyvää päivää",
"Bonjour",
"Dia dhuit",
"Guten tag",
"Yasou",
"Shalom",
"Namaste",
"Jo napot",
"Góðan dag",
"Nde-ewo",
"Selamat siang",
"Salve",
"Konnichiwa",
"Ahn nyong ha se yo",
"Salve",
"Sveiki",
"Moïen",
"Bonġu",
"Niltze",
"Namastē",
"Hallo",
"Salam",
"Cześć",
"Olá",
"Bună ziua",
"Zdravstvuyte",
"Zdravo",
"Ahoj",
"Hola",
"Hujambo",
"Hallå",
"Ia orna",
"Sawasdee",
"Avuxeni",
"Merhaba",
"Zdravstvuyte",
"Assalamo aleikum",
"xin chào",
"Shwmae",
"Sawubona"]


@bot.command()
async def load(ctx: commands.Context,extension):
    bot.load_extension(f'cogs.{extension}')
@bot.command()
async def unload(ctx: commands.Context,extension):
    bot.unload_extension(f'cogs.{extension}')

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    word = random.sample(helloList,1)[0]
    await ctx.channel.send(f"{word}, {ctx.message.author.mention}!")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        bot.load_extension(f'cogs.{filename[:-3]}')
 
bot.run(TOKEN)