print("Loading Pycord Viewer...")
print("Please note that this is a veeeery early version and might be buggy if it works at all.")
from basicFunc import *
LoadingBar(0, 5)

try:
    from discord.ext import commands
    import discord

except Exception as e:
    ErrorMessage("Modules : {}".format(e))

LoadingBar(1, 5)

settings = JsonOpen()
bot = discord.Client()
bot.CoNfIgUrAtIoN = settings
RealistikCoolest = True #Take that drago
ConfigAyOk = ConfigIntegrityCheck(bot.CoNfIgUrAtIoN)

if ConfigAyOk == False:
    ErrorMessage("Failed verifying config file! Make sure it exists and it matches the newest version available on GitHub")

LoadingBar(2, 5)

@bot.event
async def on_ready():
    LoadingBar(5, 5)
    print(" Loading finished!\nLogged into Discord via", bot.user.name)

LoadingBar(3, 5)

@bot.event
async def on_message(msg):
    ViewerConfig = bot.CoNfIgUrAtIoN["Viewer"]
    if ViewerConfig["ViewAll"] == 1:
        ctx = msg.clean_content
        Username = msg.author.name
        ctx = "[{}] {}".format(Username, ctx)
        FinalPrint = TimeFormat(ViewerConfig["TimeFormat"], ctx)
        print(FinalPrint)
    
    elif ViewerConfig["ViewAll"] == 0 and msg.channel.id in ViewerConfig["ChannelWhitelist"]:
        ctx = msg.clean_content
        Username = msg.author.name
        ctx = "[{}] {}".format(Username, ctx)
        FinalPrint = TimeFormat(ViewerConfig["TimeFormat"], ctx)
        print(FinalPrint)
    

LoadingBar(4, 5)

try:
    bot.run(settings["token"])
except Exception as e:
    ErrorMessage("LoginError: {}".format(e))
