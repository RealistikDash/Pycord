from basicFunc import *
print(LText.StartupLoading)
print(LText.BetaNotice)
LoadingBar(0, 5)

try:
    from discord.ext import commands
    import discord
    import time

except Exception:
    ErrorMessage(LText.ModuleError)

LoadingBar(1, 5)

settings = JsonOpen()
bot = discord.Client()
bot.CoNfIgUrAtIoN = settings
RealistikCoolest = True #Take that drago
ConfigAyOk = ConfigIntegrityCheck(bot.CoNfIgUrAtIoN)

if ConfigAyOk == False:
    nn()
    try:
        ErrorMessage(LText.ConfigInvalid)
    except Exception:
        print("Failed verifying config file! Make sure it exists and it matches the newest version available on GitHub") #in case the lang part doesnt work
    time.sleep(2)
    exit()

LoadingBar(2, 5)

@bot.event
async def on_ready():
    LoadingBar(5, 5)
    print(LText.LoadingDone, bot.user.name)

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
    ErrorMessage(LText.LoginError.format(e))
