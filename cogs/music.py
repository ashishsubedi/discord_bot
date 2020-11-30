import discord
from discord.ext import commands
import requests
import youtube_dl
import asyncio

# Suppress noise about console usage from errors
youtube_dl.utils.bug_reports_message = lambda: ''


ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': False,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'youtube-skip-dash-manifest': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)

        self.data = data

        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))

        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]

        filename = data['url'] if stream else ytdl.prepare_filename(data)
        return cls(discord.FFmpegPCMAudio(filename, **ffmpeg_options), data=data)


class Music(commands.Cog):
    def __init__(self,bot: commands.Bot):
        self.bot = bot

    @commands.command()
    async def join(self,ctx: commands.Context):
        if ctx.voice_client is not None:
            return await ctx.voice_client.move_to(ctx.message.author.voice.channel)
            
        await ctx.message.author.voice.channel.connect()


    @commands.command(aliases=['p','yt'],description="Play music from youtube")
    async def play(self,ctx: commands.Context,*,url):
        try:
            
            source= await YTDLSource.from_url(url,stream=True)
            ctx.voice_client.play(source,after= lambda e: print('Player error: %s' % e) if e else None)
            await ctx.send(f"Now Playing: {source.title} ")
            
            
        except Exception as e:
            print(e)
            await ctx.channel.send(ctx.message.author.mention+", Cannot connect to the vc")


    @commands.command(aliases=['pl','plofi','ytlofi'],description="Play lofi hiphop music from youtube")
    async def play_lofi(self,ctx: commands.Context):
        try:
            url = 'https://www.youtube.com/watch?v=5qap5aO4i9A'
            source= await YTDLSource.from_url(url,stream=True)
            ctx.voice_client.play(source,after= lambda e: print('Player error: %s' % e) if e else None)
            await ctx.send(f"Now Playing: {source.title} {url}")
            
            
        except Exception as e:
            print(e)
            await ctx.channel.send(ctx.message.author.mention+", Cannot play")
    
    @commands.command(aliases=['pw','pwhisky','whisky'],description="Play whiskey blues music from youtube")
    async def play_whisky(self,ctx: commands.Context):
        try:
            url = 'https://www.youtube.com/watch?v=1eNSWZ4x2ZU'
            source= await YTDLSource.from_url(url,stream=True)
            ctx.voice_client.play(source,after= lambda e: print('Player error: %s' % e) if e else None)
            await ctx.send(f"Now Playing: {source.title} {url}")
            
            
        except Exception as e:
            print(e)
            await ctx.channel.send(ctx.message.author.mention+", Cannot play")

    @commands.command()
    async def volume(self, ctx, volume: int):
        """Changes the player's volume"""

        if ctx.voice_client is None:
            return await ctx.send("Not connected to a voice channel.")

        ctx.voice_client.source.volume = volume / 100
        await ctx.send("Changed volume to {}%".format(volume))

    @commands.command(aliases=['leave'])
    async def stop(self, ctx):
        """Stops and disconnects the bot from voice"""

        await ctx.voice_client.disconnect()
   
    @play.before_invoke
    @play_lofi.before_invoke
    @play_whisky.before_invoke
    async def ensure_voice(self, ctx):
        if ctx.voice_client is None:
            if ctx.author.voice:
                await ctx.author.voice.channel.connect()
            else:
                await ctx.send("You are not connected to a voice channel.")

        elif ctx.voice_client.is_playing():
            ctx.voice_client.stop()

      

def setup(bot:commands.Bot):
    bot.add_cog(Music(bot))