import discord
from discord.ext import commands
# import commandHandler
import os
from dotenv import load_dotenv
import requests
import json

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def hello(ctx):
    await ctx.channel.send(f"Ola, {ctx.message.author.mention}!")

@bot.command()
async def dad(ctx):
    headers = {
        'Accept':"text/plain"
    }
    r = requests.get('https://icanhazdadjoke.com/',headers=headers)

    await ctx.message.channel.send(f"{ctx.message.author.mention}! \n {r.content.decode('utf-8')}")

@bot.command()
async def memeit(ctx,*,message):
    #Message format:
    # !memeit <id> /<text0>/ <text<1>

    content = message.split('/')
 
    template_key = content[0]
    texts = content[1:]
    
    url = f"https://api.memegen.link/templates/{template_key}"
    data = {
        'text_lines':texts,
        "extension": "string",
        "redirect": False
    }
    headers = {
        'content-type':'application/json'
    }
    res = requests.post(url,json=data,headers=headers)
    
    if res.status_code == 201:

        result = res.json()
        image_url = result['url']
        e = discord.Embed()
        e.set_image(url=image_url)
        await ctx.channel.send(f"{ctx.message.author.mention}",embed=e)

@bot.command()
async def templates(ctx):
    
    url = 'https://api.memegen.link/templates'
    headers = {
        'content-type':'application/json'
    }
    res = requests.get(url,headers=headers)
    print(res.status_code)
    if res.status_code == 200:

        result = res.json()
        newMessage = '```Name|\t\tId|\tLines|\tExample\n'
        for data in result:
            name = data['name']
            template_id = data['key']
            lines=data['lines']
            example = data['example']
            newMessage += f'{name}|{template_id}|{lines}|{example}\n'
            if len(newMessage) > 1600:
                newMessage+='```'
                await ctx.channel.send(f"{ctx.message.author.mention}\n{newMessage}")
                newMessage = '```Name|\t\tId|\tLines|\tExample\n'

        newMessage+='```'
        await ctx.channel.send(f"{ctx.message.author.mention}\n{newMessage}")

                

 
bot.run(TOKEN)