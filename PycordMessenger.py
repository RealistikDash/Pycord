from basicFunc import *
print(LText.StartupLoading)
print(LText.BetaNotice)
LoadingBar(0, 5)

try:
    import time
    import asyncio
    from discord.ext import commands
    import discord
    import platform
    import threading
except Exception as e:
    print(LText.ModuleError)
    time.sleep(4)
    exit()

settings = JsonOpen()

LoadingBar(1, 5)

configIsGood = ConfigIntegrityCheck(settings) #check if config is aay ok

if configIsGood == False:
    nn()
    try:
        ErrorMessage(LText.ConfigInvalid)
    except Exception:
        print("Failed verifying config file! Make sure it exists and it matches the newest version available on GitHub") #in case the lang part doesnt work
    time.sleep(2)
    exit()

LoadingBar(2, 5)

ListOfCommands = """-------------------------------------
{}:
/help           {}
/file <path>    {}  
/game <text>    {}
/exit           {}
-------------------------------------""".format(LText.CommandIntro, LText.HelpExplain, LText.FileExplain, LText.GameExplain, LText.ExitExplain)

bot = discord.Client()
bot.PycConfig = settings
bot.PycConfig["commands"] = ListOfCommands

@bot.event
async def on_ready():
    LoadingBar(5, 5)
    print(LText.LoadingDone, bot.user.name)
    #sets the playing message
    if bot.PycConfig["Messenger"]["defaultGame"] != False:
        try:
            await bot.change_presence(activity=discord.Game(name=bot.PycConfig["Messenger"]["defaultGame"]))
        except Exception as e:
            ErrorMessage(LText.GameChangingError.format(e))
    ###VARIABLES###
    ch = bot.get_channel(bot.PycConfig['Messenger']["channelId"])
    ######

    Contributors()

    print(bot.PycConfig["commands"])

    while True:
        action = input("Pycord> ")
        if action == "" or action == " ":
            print(LText.EmptyMessageError)

        elif action == "/exit":
            await bot.close()
            exit
        
        elif action.startswith("/file"):
            try:
                await ch.send(file=discord.File(action[6:]))
            except Exception as e:
                ErrorMessage(LText.FileSendingError.format(e))
        elif action.startswith("/game"):
            game = action[6:]
            if game == "False" or game == "false" or game == "off":
                await bot.change_presence(activity=None)
            else:
                await bot.change_presence(activity=discord.Game(name=game))
        else:
            try:
                await ch.send(action)
            except Exception as e:
                await AsyncErrorMessage(LText.MessageSendingError.format(e))

LoadingBar(3, 5)
def connect(botToken):
    """Connects the bot. Made function for threading module"""
    try:
        bot.run(botToken)
    except Exception as e:
        ErrorMessage(LText.LoginError.format(e))
        time.sleep(2)

LoadingBar(4, 5)

try:
    if platform.system() == "Linux":
        bot.run(settings["token"]) #so the windows solution doesnt work on linux because aiohttp so this
    else:
        thread_list = []
        thread = threading.Thread(target=connect, args = (settings["token"],))
        thread_list.append(thread)
        thread.start()
except Exception as e:
    nn()
    ErrorMessage(LText.LoginError.format(e))
    time.sleep(2)
