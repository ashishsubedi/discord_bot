import discord
from discord.ext import commands
import requests
import json

class Meme(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"Logged in as {self.bot.user}")

    @commands.command()
    async def dad(self,ctx):
        headers = {
            'Accept':"text/plain"
        }
        r = requests.get('https://icanhazdadjoke.com/',headers=headers)

        await ctx.message.channel.send(f"{ctx.message.author.mention}! \n {r.content.decode('utf-8')}")

    @commands.command()
    async def memeit(self,ctx,*,message):
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

    @commands.command()
    async def templates(self,ctx):
        
        url = 'https://api.memegen.link/templates'
        headers = {
            'content-type':'application/json'
        }
        res = requests.get(url,headers=headers)
        
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

                    

def setup(bot:commands.Bot):
    bot.add_cog(Meme(bot))