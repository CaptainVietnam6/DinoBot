#imports related to discord or discord packages
import discord
from discord.ext import commands
from discord.utils import get
from discord.ext.commands import cooldown
from discord.ext.commands import BucketType
from discord import FFmpegPCMAudio


#other important imports for system
import os
from os import system
import random
from random import randint
import time
import youtube_dl
import shutil
import asyncio

#imports from other files
from keep_alive import keep_alive
from BOT_TOKEN import BOT_TOKEN


#intents
intents = discord.Intents(messages=True, guilds=True, reactions=True, members=True)

#bot prefix
bot_prefixes = ["-", "/"]
client = commands.Bot(command_prefix = bot_prefixes)
bot = commands.Bot(command_prefix = "/", intents = intents)

#remove original help command 
client.remove_command("help") 


'''START OF MODERATION AND SETUP COMMANDS'''


#ALERTS WHEN DINOBOT IS READY
@client.event
async def on_ready():
    await client.change_presence(status = discord.Status.online, activity = discord.Game("Programmed by CaptainVietnam6#0001 in Python 3.8.2"))
    await asyncio.sleep(3)
    print("DinoBot is ready")

    #notifs for Dino City Server
    channel = client.get_channel(813513873419665470)
    await channel.send("DinoBot is online")
    #notifs for CV6's Playground server
    channel = client.get_channel(816179144961818634)
    await channel.send("DinoBot is online")
    #notifs for CV6's Bots server
    channel = client.get_channel(812974446801059860)
    await channel.send("DinoBot is online")

    #joins vc on ready
    channel = client.get_channel(815933179378270208)
    await channel.connect()


#CREDIT  
@client.command(aliases = ["credit", "credits", "Credit", "Credits"])
async def _botcredits(ctx):
    await ctx.send("Hi!, My name is DinoBot and I was created and programmed by CaptainVietnam6 for the 『Dino City』discord server.")


#RETURNS BOT'S PING IN MILLISECONDS
@client.command()
async def ping(ctx):
    await ctx.send(f"Pong {client.latency * 1000}ms")


#SERVER COLOR HEX CODE REMINDER THINGY
@client.command(aliases = ["serhexcode"])
async def _serverhexcode(ctx):
    await ctx.send("the server theme hex code is #008080")


#chat purge command cleared out as suspicion of passing rate limit
'''
#CHAT PURGE COMMAND
@client.command(aliases = ["clear", "Clear", "Purge", "purge"])
@commands.has_any_role("【smol dinos】", "❀ dino nuggies")
@cooldown(1, 180, BucketType.default)
async def _chat_clear(ctx, amount = 100):
    await ctx.channel.purge(limit = amount + 1)
    await asyncio.sleep(float(1.5))
    await ctx.send (f"cleared {amount} messages from chat")
    await asyncio.sleep(float(0.5))
    await ctx.send("Please wait 3 minutes before using this command again :)")
'''


#RULES COMMAND
@client.command(aliases = ["rules", "Rules"])
@cooldown(1, 30, BucketType.default)
async def _therules(ctx):
    heart_emoji = "\u2764\ufe0f"
    embed = discord.Embed(
        title = "「Server rules! (✿^‿^)」",
        description = "1. Use the correct channels\n2. Don't spam, use common sense\n3. No nsfw.\n4. Keep your nickname respectful and unoffensive\n5. Religion and politics are complex and controversial topics therefore should be best kept out of this server.\n6. No racial slurs or other racially offensive terms and or anything resembling it or meant to carry the same meaning.\n7. Be respectful to others, no discrimination unless it's meant as a joke and both parties reconise it as one.\n8. Use common sense, don't try find loopholes in my rules and don't be a smartass about it. Just use common sense and you'll be fine\n",
        color = 0x008080
    )
    embed.set_footer(text = f"Bot and rules made with love by CaptainVietnam6 (◍•ᴗ•◍){heart_emoji}")
    embed.set_thumbnail(url = "https://media.discordapp.net/attachments/811850521370427413/812968784344252416/image0-9.png?width=473&height=473")
    await ctx.send(embed = embed)


'''END OF MODERATION AND SETUP COMMANDS'''

'''START OF HELP COMMANDS'''


#HELP COMMAND
@client.group(invoke_without_command = True, aliases = ["help", "Help"])
async def _help(ctx):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**Help command categories**",
        description = "**These are the commands you can run to see the list of commands in each category.**\n\nFun commands: **-help fun**\nMusic commands: **-help music**\nSoundboard commands: **-help sb**\nGame commands: **-help game**\nEmoji commands: **-help emoji**\nModeration commands: **-help mod**\n",
        color = 0x008080
    )
    embed.set_footer(text = f"Requested by {author_name}")
    await ctx.send(embed = embed)

#HELP - FUN COMMANDS
@_help.command(aliases = ["fun", "Fun"])
async def _help_fun(ctx):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**Fun/responses related commands list**",
        description = "**These are commands that relate to fun or responses features of DinoBot**\n\n",
        color = 0x008080
    )
    embed.set_footer(text = f"Requested by {author_name}")
    await ctx.send(embed = embed)

#HELP - MUSIC COMMANDS
@_help.command(aliases = ["music", "Music"])
async def _help_music(ctx):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**Music related commands list**",
        description = "**These are commands that relate to music features of MonarchBot**\n\nJoin VC: **-join**\nLeave VC: **-leave**\nPlay song: **-play (youtube url)**\nQueue song: **-queue (youtube url)**\nPause music: **-pause**\nResume music: **-resume**\nStop music: **-stop**\n",
        color = 0x0008080
    )
    embed.set_footer(text = f"Requested by {author_name}")
    await ctx.send(embed = embed)

#HELP - SOUNDBOARD COMMANDS
@_help.command(aliases = ["sb", "Sb", "SB", "soundboard", "SoundBoard", "Soundboard"])
async def _help_soundboard(ctx):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**Soundboard related commands list**",
        description = "**These are commands that relate to voice channel soundboard features of MonarchBot**\n\nJoin VC: **-join**\nLeave VC: **-leave**\nAirhorn: **-sb airhorn**\nAli-a intro: **-sb alia**\nBegone thot: **-sb begonethot**\nDamn son where'd you find this: **-sb damnson**\nDankstorm: **-sb dankstorm**\nDeez nuts: **-sb deeznuts**\nDeja Vu: **-sb dejavu**\nLook at this dude: **-sb dis_dude**\nAnother fag left the chat: **-sb fleft**\nFart: **-sb fart**\nHah gaaayyy: **-sb hahgay**\nIt's called hentai and it's art: **-sb henart**\nIlluminati song: **-sb illuminati**\nBitch Lasagna: **-sb lasagna**\nLoser: **-sb loser**\nNoob: **-sb noob**\nOof sound: **-sb oof**\nPickle Rick: **-sb picklerick**\nNice: **-sb nice**\nWhy don't we just relax and turn on the radio: **-sb radio**\nRick roll: **-sb rickroll**\nThis is sparta: **-sb sparta**\nTitanic flute fail: **-sb titanic**\nGTA V Wasted: **-sb wasted**\nWubba lubba dub dub: **-sb wubba**\n",
        color = 0x008080
    )
    embed.set_footer(text = f"Requested by {author_name}")
    await ctx.send(embed = embed)

#HELP - GAME COMMANDS
@_help.command(aliases = ["game", "Game"])
async def _help_game(ctx):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**Game related commands list**",
        description = "**These are commands that relate to game features of DinoBot**\n\n8ball command: **-8ball (your question)**\nDice command, returns 1-6: **-dice**\nRock Paper Scissors: **-rps (rock, paper, or scissors)**\nMeme command: **-meme**\nHentai command: **-hentai**\n",
        color = 0x008080
    )
    embed.set_footer(text = f"Requested by {author_name}")
    await ctx.send(embed = embed)

#HELP - EMOJI COMMANDS
@_help.command(aliases = ["emoji", "Emoji"])
async def _help_emoji(ctx):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**Emoji related commadns list**",
        description = "**The commands with an $ have an auto detection feature to detect a certain keyword in your message**\n\nSo fake$: **-fake**\nX to doubt$: **-doubt**\nStonks$: **-stonks**\nSimp pill$: **-simp**\nUwU*: **-uwu**\nWat: **-wat**\nAdmin abooz: **-abooz**\n60s Timer$: **-timer**\nThats racist$: **-racist**\nPolice$: **-police**\nF-spam emoji: **-fpsam**\nClap emoji: **-clap**\nYou tried: **-youtried**\nPython logo: **-python**\nPepe pog: **-pepepog**\nGay flag$: **-gay**\nBisexual flag$: **-bisexual**\nTrans flag$: **-trans**",
        color = 0x008080
    )
    embed.set_footer(text = f"Requested by {author_name}")
    await ctx.send(embed = embed)

#HELP - MODERATION COMMANDS
@_help.command(aliases = ["mod", "Mod", "moderation", "Moderation"])
async def _help_moderation(ctx):
    author_name = ctx.author.display_name
    embed = discord.Embed(
        title = "**Moderation related commands list**",
        description = "**These are commands that relate to moderation features of DinoBot, most require administrative powers**\n\nKick command: **/kick (tag member, reason)**\nBan command: **/ban (tag member, reason)**\nHelp directory: **/help**\n",
        color = 0x008080
    )
    embed.set_footer(text = f"Requested by {author_name}")
    await ctx.send(embed = embed)


'''END OF HELP COMMANDS'''

'''START OF VOICE CHANNEL AND MUSIC AND SOUNDBOARD COMMANDS'''


#VOICE CHANNEL JOIN
@client.command(pass_context = True, aliases = ["Join", "join", "j", "J", "connect", "Connect"])
async def _join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        await ctx.send("I joined your voice channel (≧▽≦)")
        print("DinoBot joined a voice channel")


#VOICE CHANNEL LEAVE
@client.command(pass_context = True, aliases = ["Leave", "leave", "L", "l", "Disconnect", "disconnect"])
async def _leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild = ctx.guild)

    if voice and voice.is_connected():
        await voice.disconnect()
        print(f"DinoBot is disconnected from {channel} voice channel")
        await ctx.send(f"I left the '{channel}' voice channel  (´；ω；`)")
    else:
        print("command given to leave voice channel but bot wasn't in a voice channel")
        await ctx.send("Invalid command: bot wasn't in any voice channels")


#VOICE CHANNEL PLAY YOUTUBE URL
@client.command(pass_context = True, aliases = ["play", "Play", "p", "P"])
async def _play(ctx, url: str):
    def check_queue():
        Queue_infile = os.path.isdir("./Queue")
        if Queue_infile is True:
            DIR = os.path.abspath(os.path.realpath("Queue"))
            length = len(os.listdir(DIR))
            still_queue = length - 1 #outprints how many are left in queue after new song is played
            try:
                first_file = os.listdir(DIR)[0] #first file inside directory
            except:
                print("No more songs in queue\n")
                queues.clear
                return
            main_location = os.path.dirname(os.path.realpath(__file__))
            song_path = os.path.abspath(os.path.realpath("Queue") + "//" + first_file)
            
            if length != 0:
                print("Sone finished playing, loading next song\n")
                print(f"Songs still in queue: {still_queue}")
                is_song_there = os.path.isfile("song.mp3")
                if is_song_there: 
                    os.remove("song.mp3")
                shutil.move(song_path, main_location) #moves queued song to main directory
                for file in os.listdir("./"):
                    if file.endswith(".mp3"):
                        os.rename(file, "song.mp3")
                vcvoice.play(discord.FFmpegPCMAudio("song.mp3"), after = lambda e: check_queue()) #plays the song
                vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
                vcvoice.source.value = 0.05
            
            else: #if queues = 0, clearns it
                queues.clear()
                return

        else: #is there is no queue folder
            queues.clear()
            print("No songs queued after last song\n")

    #end of queue section thingy for play command
    is_song_there = os.path.isfile("song.mp3")
    try: #code will try to remove song, if it's playing then no remove
        if is_song_there:
            os.remove("song.mp3")
            queues.clear()
            print("Removed an old song file")
    except PermissionError:
        print("Failed to remove song file, song file in use")
        ctx.send("Error: song file cannot be removed because it's playing")
        return

    #this section is here to remove the old queue folder
    Queue_infile = os.path.isdir("./Queue")
    try:
        Queue_folder = "./Queue"
        if Queue_infile is True:   #if there is an old queue file, it will try to remove it
            print("Removed old queue folder")
            shutil.rmtree(Queue_folder)
    except:
        print("No old queue folder")

    #rest of play command to play songs
    await ctx.send("Getting everything ready (≧▽≦) (this may take a bit to load)")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "256",
        }], #code above to specify options in ydl
    }
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloaded audio file\n")
        ydl.download([url])
    #renames file name 
    for file in os.listdir("./"): #./ for current directory
        if file.endswith(".mp3"):
            audio_file_name = file
            print(f"Renamed File {file}\n")
            os.rename(file, "song.mp3")
    #checks to see if audio has finished playing, after then it will print
    vcvoice.play(discord.FFmpegPCMAudio("song.mp3"), after = lambda e: check_queue())
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05
    new_name = audio_file_name.rsplit("-", 2)
    await ctx.send(f"Playing {new_name}")
    print("playing\n")


#VOICE CHANNEL MUSIC PAUSE COMMAND
@client.command(pass_context = True, aliases = ["pause", "Pause"])
async def _pause(ctx):
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    
    if vcvoice and voice.is_playing():
        vcvoice.pause()
        print("Music paused")
        await ctx.send("Music paused")
    else:
        print("Music wasn't playing but there was a request to pause music")
        await ctx.send("Music wasn't playing so i can't pause it")


#VOICE CHANNEL MUSIC RESUME COMMAND
@client.command(pass_context = True, aliases = ["resume", "Resume"])
async def _resume(ctx):
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    
    if vcvoice and voice.is_paused():
        vcvoice.resume()
        print("Music resumed")
        await ctx.send("Music has been resumed pogs")
    else:
        print("Music was not paused but a request was sent for music pause")
        await ctx.send("Music can't be resumed as it wasn't paused smh")


#VOICE CHANNEL MUSIC STOP COMMAND
@client.command(pass_context = True, aliases = ["stop", "Stop"])
async def _stop(ctx):
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)

    queues.clear() #clears queue when stop command ran

    if vcvoice and voice.is_playing():
        vcvoice.stop()
        print("Music stopped")
        await ctx.send("Music stopped")
    else:
        print("Music could not be stopped")
        await ctx.send("Music can't be stopped if there aint music playing")


#VOICE CHANNEL MUSIC queue
#this command is for music to be queued up if you use the ".play" multiple times while music is still playing
queues = {}
@client.command(pass_context = True, aliases = ["Queue", "queue", "Q", "q"])
async def _queue(ctx, url: str):
    Queue_infile = os.path.isdir("./Queue")
    if Queue_infile is False:
        os.mkdir("Queue")      #sees if there is any song files in queue, if there is any then it counts them
    DIR = os.path.abspath(os.path.realpath("Queue"))
    queue_num = len(os.listdir(DIR)) #gets/counts ammount of files in the queue
    queue_num += 1 #adds another to queue
    add_queue = True
    while add_queue:
        if queue_num in queues:
            queue_num += 1
        else:
            add_queue = False
            queues[queue_num] = queue_num

    queue_path = os.path.abspath(os.path.realpath("Queue") + f"//song{queue_num}.%(ext)s")
    #takes the real path of song in queue and number of it
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl" : queue_path,
        "postprocessors": [{
            "key": "FFmpegExtractAudio",
            "preferredcodec": "mp3",
            "preferredquality": "1024",
        }], #code above to specify options in ydl
    }
    #downloads song and puts into queue path above ^
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print("Downloaded audio file\n")
        ydl.download([url])
    await ctx.send("Adding song " + str(queue_num) + " to the queue")
    print("added a song to queue\n")


'''END OF MUSIC AND VOICE CHANNEL RELATED COMMANDS'''

'''START OF VOICE CHANNEL SOUNDBOARD COMMANDS'''


#SOUNDBOARD COMMAND GROUP & HELP
@client.group(invoke_without_command = True, aliases = ["sb", "SB", "soundboard", "Soundboard", "SoundBoard"])
async def _soundboard(ctx):
    await ctx.send("**Soundboard Commands List**\n")

#SB AIRHORN 
@_soundboard.command(aliases = ["airhorn", "Airhorn"])
async def _soundboard_airhorn(ctx):
    await ctx.send("Playing **airhorn** sound effect from soundboard")
    print("\nPlayed airhorn sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/airhorn.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB ALI-A SOUNDTRACK
@_soundboard.command(aliases = ["ali_a", "alia", "Ali-a", "Alia"])
async def _soundboard_ali_a(ctx):
    await ctx.send("Playing **ali_a** sound effect from soundboard")
    print("\nPlayed ali_a sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/ali_a.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB BEGONE THOT
@_soundboard.command(aliases = ["begone_thot", "begonethot", "Begone_thot", "Begonethot"])
async def _soundboard_begone_thot(ctx):
    await ctx.send("Playing **begone_thot** sound effect from soundboard")
    print("\nPlayed begone_thot sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/begone_thot.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB DAMN SON WHERE'D U FIND THIS
@_soundboard.command(aliases = ["damn_son", "Damn_son", "damnson", "Damnson"])
async def _soundboard_damn_son(ctx):
    await ctx.send("Playing **damn_son** sound effect from soundboard")
    print("\nPlayed damn_son sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/damn_son.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB DANKSTORM
@_soundboard.command(aliases = ["dankstorm", "Dankstorm"])
async def _soundboard_dankstorm(ctx):
    await ctx.send("Playing **dankstorm** sound effect from soundboard")
    print("\nPlayed dankstorm sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/dankstorm.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB DEEZNUTS
@_soundboard.command(aliases = ["deez_nuts", "deeznuts", "Deez_nuts", "Deeznuts"])
async def _soundboard_deez_nuts(ctx):
    await ctx.send("Playing **deez_nuts** sound effect from soundboard")
    print("\nPlayed deez_nuts sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/deez_nuts.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB DEJA VU
@_soundboard.command(aliases = ["deja_vu", "dejavu", "Deja_vu", "Dejavu"])
async def _soundboard_deja_vu(ctx):
    await ctx.send("Playing **deja_vu** sound effect from soundboard")
    print("\nPlayed deja_vu sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/deja_vu.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB LOOK AT THIS DUDE
@_soundboard.command(aliases = ["dis_dude", "this_dude", "disdude", "thisdude", "Dis_dude", "This_dude", "Disdude", "Thisdude" ])
async def _soundboard_this_dude(ctx):
    await ctx.send("Playing **dis_dude** sound effect from soundboard")
    print("\nPlayed dis_dude sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/dis_dude.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB ANOTHER FAG LEFT THE CHAT
@_soundboard.command(aliases = ["f_left", "fleft", "F_left", "Fleft"])
async def _soundboard_f_left(ctx):
    await ctx.send("Playing **f_left** sound effect from soundboard")
    print("\nPlayed f_left sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/f_left.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB FART
@_soundboard.command(aliases = ["fart", "Fart"])
async def _soundboard_fart(ctx):
    await ctx.send("Playing **fart** sound effect from soundboard")
    print("\nPlayed fart sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/fart.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB HAH GAAAYY
@_soundboard.command(aliases = ["hah_gay", "hahgay", "Hah_gay", "Hahgay"])
async def _soundboard_hah_gay(ctx):
    await ctx.send("Playing **hah_gay** sound effect from soundboard")
    print("\nPlayed hah_gay sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/hah_gay.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB IT'S CALLED HENTAI, AND IT'S ART
@_soundboard.command(aliases = ["hen_art", "henart", "Hen_art", "Henart"])
async def _soundboard_hentai_art(ctx):
    await ctx.send("Playing **henart (hentai art)** sound effect from soundboard")
    print("\nPlayed henart sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/hen_art.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB ILLUMINATI X-FILES SOUNDTRACK
@_soundboard.command(aliases = ["illuminati", "Illuminati"])
async def _soundboard_illuminati(ctx):
    await ctx.send("Playing **illuminati** sound effect from soundboard")
    print("\nPlayed illuminati sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/illuminati.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB BITCH LASAGNA
@_soundboard.command(aliases = ["lasagna", "Lasagna", "bitch_lasagna", "Bitch_lasagna"])
async def _soundboard_bitch_lasagna(ctx):
    await ctx.send("Playing **bitch_lasagna** sound effect from soundboard")
    print("\nPlayed bitch_lasagna sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/lasagna.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB LOOSER
@_soundboard.command(aliases = ["looser", "Looser", "loser", "Loser"])
async def _soundboard_loser(ctx):
    await ctx.send("Playing **loser** sound effect from soundboard")
    print("\nPlayed loser sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/loser.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB NOOB 
@_soundboard.command(aliases = ["noob", "Noob"])
async def _soundboard_noob(ctx):
    await ctx.send("Playing **noob** sound effect from soundboard")
    print("\nPlayed noob sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/noob.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB OOF SOUND
@_soundboard.command(aliases = ["oof", "Oof"])
async def _soundboard_oof(ctx):
    await ctx.send("Playing **oof** sound effect from soundboard")
    print("\nPlayed oof sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/oof.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB I'M PICKLE RICKKKK
@_soundboard.command(aliases = ["pickle_rick", "Pickle_rick", "picklerick", "Picklerick"])
async def _soundboard_pickcle_rick(ctx):
    await ctx.send("Playing **pickle_rick** sound effect from soundboard")
    print("\nPlayed pickle_rick sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/pickle_rick.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB *POP* NICE  
@_soundboard.command(aliases = ["nice", "Nice"])
async def _soundboard_nice(ctx):
    await ctx.send("Playing **nice** sound effect from soundboard")
    print("\nPlayed nice sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/nice.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB WHY DON'T WE JUST RELAX, TURN ON THE RADIO, WOULD YOU LIKE AM OR FM
@_soundboard.command(aliases = ["radio", "Radio"])
async def _soundboard_radio(ctx):
    await ctx.send("Playing **radio** sound effect from soundboard")
    print("\nPlayed radio sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/radio.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB RICKROLL
@_soundboard.command(aliases = ["rick_roll", "Rick_roll", "rickroll", "Rickroll"])
async def _soundboard_rick_roll(ctx):
    await ctx.send("Playing **rick_roll** sound effect from soundboard")
    print("\nPlayed rick_roll sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/rick_roll.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB SPARTA
@_soundboard.command(aliases = ["sparta", "Sparta"])
async def _soundboard_sparta(ctx):
    await ctx.send("Playing **sparta** sound effect from soundboard")
    print("\nPlayed sparta sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/sparta.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB TITANIC FLUTE MEME
@_soundboard.command(aliases = ["titanic", "Titanic"])
async def _soundboard_titanic(ctx):
    await ctx.send("Playing **titanic** sound effect from soundboard")
    print("\nPlayed titanic sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/titanic.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB GTAV WASTED SOUND
@_soundboard.command(aliases = ["wasted", "Wasted"])
async def _soundboard_wasted(ctx):
    await ctx.send("Playing **wasted** sound effect from soundboard")
    print("\nPlayed wasted sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/wasted.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05

#SB RICK & MORTY WUBBA LUBBA DUB DUB
@_soundboard.command(aliases = ["wubba", "Wubba"])
async def _soundboard_wubba(ctx):
    await ctx.send("Playing **wubba** sound effect from soundboard")
    print("\nPlayed wubba sound effect\n")
    vcvoice = discord.utils.get(client.voice_clients, guild = ctx.guild)
    vcvoice.play(discord.FFmpegPCMAudio("soundboard/wubba.mp3"))
    vcvoice.source = discord.PCMVolumeTransformer(vcvoice.source)
    vcvoice.source.value = 0.05


'''END OF VOICE CHANNEL SOUNDBOARD COMMANDS'''

'''START OF GAME COMMANDS'''


#8BALL COMMAND
@client.command(aliases=["8ball", "eightball"])
async def _8ball(ctx, *, user_question):
    author_name = ctx.author.display_name
    responses = [
        "As I see it, yes.",
        "Ask again later.",
        "Better not tell you now.",
        "Cannot predict now.",
        "Concentrate and ask again.",
        "Don’t count on it.",
        "It is certain.",
        "It is decidedly so.",
        "Most likely.",
        "My reply is no.",
        "My sources say no.",
        "Outlook not so good.",
        "Outlook good.",
        "Reply hazy, try again.",
        "Signs point to yes.",
        "Very doubtful.",
        "Without a doubt.",
        "Yes.",
        "Yes – definitely.",
        "You may rely on it.",
        "No it'll never happen give up.",
        "It might happen but ehhhhhhh.",
        "stfu i aint god."]
    final_response = random.choice(responses)
    embed = discord.Embed(
        title = "8ball command",
        description = f"Question: **{user_question}**\nAnswer: **{final_response}**",
        color = 0x008080
    )
    embed.set_footer(text = f"Requested by {author_name}")
    await ctx.send(embed = embed)


#MEME COMMAND
@client.command(aliases = ["meme", "Meme"])
async def _sendsmeme(ctx):
    random_meme_number = randint(1,5000)
    embed = discord.Embed(
        color = 0x008080
    )
    embed.set_image(url = f"https://ctk-api.herokuapp.com/meme/{random_meme_number}")
    await ctx.send(embed = embed)


'''END OF GAME COMMANDS'''


'''START OF FUNNY RESPONSES COMMANDS'''


#PRINT COMMAND; SENDS A FANCY EMBED IMAGE WITH AUTHOR'S MESSAGE
@client.command(aliases = ["print", "Print"])
@cooldown(1, 15, BucketType.default)
async def _printmessage(ctx, *, user_print_message):
    embed = discord.Embed(
        color = 0x008080
    )
    embed.set_image(url = f"https://flamingtext.com/net-fu/proxy_form.cgi?script=crafts-logo&text={user_print_message}+&_loc=generate&imageoutput=true")
    await ctx.send(embed = embed)


#REPLY SPAM COMMAND
#spams what you type after "/spam" 5 times
@client.command(aliases = ["spam", "Spam"])
@cooldown(1, 60, BucketType.default)
async def _replyspam(ctx, *, user_spam_input):
    print("Someone activated the reply spam command")
    await asyncio.sleep(float(0.5))
    for i in range(5):
        await ctx.send(f"{user_spam_input}")
        print(f"Reply spam loop {i}")
    await asyncio.sleep(float(0.25))
    print("Reply spam command ended")
    await ctx.send("Please wait 60 seconds to use this command again.")


#REPEAT COMMAND; BOT REPEATS AFTER USER
@client.command(aliases = ["repeat", "Repeat", "say", "Say"])
@cooldown(5, 60, BucketType.default)
async def _repeat_after_user(ctx, *, user_repeat_input):
    await ctx.send(f"{user_repeat_input}")


#WELCOME
@client.command(aliases = ["welcome", "Welcome"])
async def _welcomecommand(ctx):
    embed = discord.Embed(
        title = "Welcome!",
        description = "Welcome to 『Dino City』! This server's owner is <@447282425681412096> and <@560785028771217421>. Please check out our rules in #「rules」",
        color = 0x008080
    )
    await ctx.send(embed = embed)


#-BENICE SEND FUNNY 'BE NICE TO SERVER STAFF'
@client.command(aliases = ["benice", "Benice", "BeNice"])
async def _benicetoserverstaff(ctx):
    await ctx.send("https://media.discordapp.net/attachments/709672550707363931/721226547817873519/tenor.gif")


#REPLIES SEND THIGH PICS
@client.command(aliases = ["thighpics", "thigh_pics", "thighpic", "thigh_pic"])
async def _thighpics(ctx):
    await ctx.send("send thigh pics uwu")


#ZERO TWO GIF
@client.command(aliases = ["zerotwo", "02", "ZeroTwo", "zero two", "Zero Two", "Zero two", "Zerotwo"])
async def _zerotwo(ctx):
    await ctx.send("bruh-")
    await asyncio.sleep(float(0.5))
    await ctx.send("https://tenor.com/view/darling-in-the-franxx-zero-two-dance-gif-14732606")
    print("someone's being a simp")
    await asyncio.sleep(float(1.5))
    await ctx.send("fuckin simp....")


#DICTIONARY COMMAND, GIVES YOU A DICTIONARY LINK TO THE WORD YOU MENTIONED
@client.command(aliases = ["Dictionary", "dictionary", "Dict", "dict"])
@cooldown(3, 30, BucketType.default)
async def _dictionarylink(ctx, user_dictionary_request):
    print(f"Someone used the dictionary command for the word {user_dictionary_request}")
    await ctx.send(f"Getting you the dictionary link for the word {user_dictionary_request}")
    await asyncio.sleep(float(0.5))
    await ctx.send(f"Here you go!\nhttps://www.dictionary.com/browse/{user_dictionary_request}?s=t")


'''
#CAPT GET PINGED ANGR
@client.listen("on_message")
async def captgetpinged(message):
    if message.author.bot:
        return
    #mobile varient
    if "<@467451098735837186>" in message.content:
        await message.channel.send("you're fucked ಠ◡ಠ")
    #PC varient
    if "<@!467451098735837186>" in message.content:
        await message.channel.send("you're fucked ಠ◡ಠ")
'''


'''END OF RESPONSES OR RELATED COMMANDS'''

'''START OF EMOJI RESPONSES COMMANDS'''


#SO FAKE EMOJI
'''
@client.listen("on_message")
async def _sofakeemoji(message):
    if message.author.bot:
        return
    if "fake" in message.content:
        await message.channel.send("<:cv6_so_fake:812995927605903400>")
    if "Fake" in message.content:
        await message.channel.send("<:cv6_so_fake:812995927605903400>")
'''

@client.command(aliases = ["fake", "Fake"])
async def _sofakeemojisend(ctx):
    await ctx.send("<:cv6_so_fake:812995927605903400>")


#DOUBT EMOJI
'''
@client.listen("on_message")
async def _doubtemoji(message):
    if message.author.bot:
        return
    if "Doubt" in message.content:
        await message.channel.send("<:cv6_X_doubt:812995858781438022>")
    if "doubt" in message.content:
        await message.channel.send("<:cv6_X_doubt:812995858781438022>")
'''

@client.command(aliases = ["doubt", "Doubt"])
async def _doubtemojisend(ctx):
    await ctx.send("<:cv6_X_doubt:812995858781438022>")


#STONKS EMOJI
@client.listen("on_message")
async def _stonksemoji(message):
    if message.author.bot:
        return
    if "stonk" in message.content:
        await message.channel.send("<:cv6_stonks:812995837613309992>")
    if "Stonk" in message.content:
        await message.channel.send("<:cv6_stonks:812995837613309992>")

@client.command(aliases = ["stonks", "stonk", "Stonks", "Stonk"])
async def _stonksemojisend(ctx):
    await ctx.send("<:cv6_stonks:812995837613309992>")


#SIMP PILLS EMOJI
@client.listen("on_message")
async def _simppills(message):
    if message.author.bot:
        return
    if "simp" in message.content:
        await message.channel.send("<:cv6_simp_pills:812995814904561695>")
    if "Simp" in message.content:
        await message.channel.send("<:cv6_simp_pills:812995814904561695>")


@client.command(aliases = ["simp", "Simp"])
async def _simppillsemojisend(ctx):
    await ctx.send("<:cv6_simp_pills:812995814904561695>")


#UWU EMOJI
@client.listen("on_message")
async def _uwuemoji(message):
    if message.author.bot:
        return
    if "uwu" in message.content:
        await message.channel.send("uwu daddy smack me harder <:cv6_uwu:812995744247447563>")
    if "UwU" in message.content:
        await message.channel.send("uwu daddy smack me harder <:cv6_uwu:812995744247447563>")

@client.command(aliases = ["uwu", "UwU"])
async def _uwuemojisend(ctx):
    await ctx.send("uwu daddy smack me harder <:cv6_uwu:812995744247447563>")


#WAT EMOJI
@client.command(aliases = ["what", "What", "wat", "Wat"])
async def _watemojisend(ctx):
    await ctx.send("<:cv6_wat:812995793278468117>")


#ADMIN ABOOZ EMOJI
@client.command(aliases = ["abooz", "Abooz"])
async def _adminaboozemojisend(ctx):
    await ctx.send("<:cv6_abooz:812995683740418068>")


#60S TIMER EMOJI
@client.listen("on_message")
async def _timeremoji(message):
    if message.author.bot:
        return
    if "timer" in message.content:
        await message.channel.send("<a:cv6_60s_timer:812995903421022221>")
    if "Timer" in message.content:
        await message.channel.send("<a:cv6_60s_timer:812995903421022221>")


@client.command(aliases = ["timer", "Timer"])
async def _timeremojisend(ctx):
    await ctx.send("<a:cv6_60s_timer:812995903421022221>")


#RACIST EMOJI
@client.listen("on_message")
async def _racistemoji(message):
    if message.author.bot:
        return
    if "racist" in message.content:
        await message.channel.send("<:cv6_rascist:812995663817342986>")
    if "Racist" in message.content:
        await message.channel.send("<:cv6_rascist:812995663817342986>")


@client.command(aliases = ["racist", "Racist"])
async def _racistemojisend(ctx):
    await ctx.send("<:cv6_rascist:812995663817342986>")


#GAY EMOJI
@client.command(aliases = ["gay", "Gay"])
async def _gayemojisend(ctx):
    await ctx.send("<:cv6_gay:812995646919147550>")


#BISEXUAL EMOJI
@client.command(aliases = ["Bisexual", "bisexual", "bi", "Bi"])
async def _bisexualemojisend(ctx):
    await ctx.send("<:cv6_bisexual:812995628950618112>")


#TRANS EMOJI
@client.command(aliases = ["transgender", "Transgender", "Trans", "trans"])
async def _transemojisend(ctx):
    await ctx.send("<:cv6_trans:812995611270840371>")


#POLICE EMOJI
@client.listen("on_message")
async def _policeemoji(message):
    if message.author.bot:
        return
    if "police" in message.content:
        await message.channel.send("<a:cv6_police:812995767639212032>")
    if "Police" in message.content:
        await message.channel.send("<a:cv6_police:812995767639212032>")


@client.command(aliases = ["police", "Police"])
async def _policeemojisend(ctx):
    await ctx.send("<a:cv6_police:812995767639212032>")


#Fspam EMOJI
@client.command(aliases = ["fspam", "Fspam"])
async def _fspamemojisend(ctx):
    await ctx.send("<a:cv6_Fspam:812995726710669342>")


#CLAP EMOJI
@client.command(aliases = ["clap", "Clap"])
async def _clapemojisend(ctx):
    await ctx.send("<a:cv6_clap:812995595613896714>")


#YOU TRIED EMOJI
@client.command(aliases = ["youtried", "Youtried"])
async def _uoutriedemojisend(ctx):
    await ctx.send("<a:cv6_youtried:812995570906038292>")


@client.command(aliases = ["python", "Python"])
async def _pythonemojisend(ctx):
    await ctx.send("<a:cv6_python:812995549414162474>")


#PEPEfog emoji
@client.command(aliases = ["pepepog", "Pepepog"])
async def _pepefogemojisend(ctx):
    await ctx.send("<a:cv6_pepepog:812995528081276958>")


'''END OF EMOJI RESPONSE COMMANDS'''


#KEEP ALIVE COMMAND FOR WEBSERVER
keep_alive()

#BOT TOKEN TO CONNECT TO DISCORD'S API
client.run(BOT_TOKEN) #token can be found in the file 'BOT_TOKEN.py'
