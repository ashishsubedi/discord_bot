import discord
from discord.ext import commands



# @client.event
# async def on_message(message):

#     if message.author == client.user:
#         return
    
#     if message.content.startswith("!"):
#         msg = message.content.split()[0][1:]
#         if msg not in commands:
#             await wrongCommand(message)
#         else:  
#             if msg == 'hello':
#             elif msg == 'dad':
#                 headers = {
#                     'Accept':"text/plain"
#                 }
#                 r = requests.get('https://icanhazdadjoke.com/',headers=headers)

#                 await message.channel.send(f"{message.author.mention}! \n {r.text}")

#             elif msg == 'memeit':
#                 #Message format:
#                 # !memeit / <id> /<text0>/ <text<1>
#                 content = message.content.split('/')[1:]
#                 template_key = content[0]
#                 texts = content[1:]
                
#                 url = f"https://api.memegen.link/templates/{template_key}"
#                 data = {
#                     'text_lines':texts,
#                     "extension": "string",
#                     "redirect": False
#                 }
#                 headers = {
#                     'content-type':'application/json'
#                 }
#                 res = requests.post(url,json=data,headers=headers)
               
#                 if res.status_code == 201:

#                     result = res.json()
#                     image_url = result['url']
#                     e = discord.Embed()
#                     e.set_image(url=image_url)
#                     await message.channel.send(f"{message.author.mention}",embed=e)

#                 elif res.status_code == 400:
#                     await wrongCommand(message)
#             elif msg == 'templates':
#                 print(msg)
#                 url = 'https://api.memegen.link/templates'
#                 headers = {
#                     'content-type':'application/json'
#                 }
#                 res = requests.get(url,headers=headers)
#                 print(res.status_code)
#                 if res.status_code == 200:

#                     result = res.json()
#                     newMessage = '```Name|\t\tId|\tLines|\tExample\n'
#                     for data in result:
#                         name = data['name']
#                         template_id = data['key']
#                         lines=data['lines']
#                         example = data['example']
#                         newMessage += f'{name}|{template_id}|{lines}|{example}\n'
#                         if len(newMessage) > 1600:
#                             newMessage+='```'
#                             await message.channel.send(f"{message.author.mention}\n{newMessage}")
#                             newMessage = '```Name|\t\tId|\tLines|\tExample\n'

#                     newMessage+='```'
#                     await message.channel.send(f"{message.author.mention}\n{newMessage}")

#                 elif res.status_code == 400:
#                     await wrongCommand(message)
#             elif msg == 'help':
#                 newMessage  = '```Usage of bot. Put ! before every command\nCommands | Example\n'
#                 for key,val in commands.items():
#                     newMessage +=f'{key} = {val}\n'
#                 newMessage  += '```'
#                 await message.channel.send(f"{message.author.mention}\n{newMessage}")

