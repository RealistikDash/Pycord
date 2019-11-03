print("Loading Pycord Messenger...")
print("Please note that this is a veeeery early version and might be buggy if it works at all.")
from basicFunc import *
LoadingBar(0, 5)

try:
    import time
    import asyncio
    from discord.ext import commands
    import discord
    from config import *
    import platform
    import threading
except Exception as e:
    print("\033[91m\nCritical error occured during imports of critical modules!\n{}\033[0m".format(e))
    time.sleep(4)
    exit()

LoadingBar(1, 5)

configIsGood = ConfigIntegrityCheck(settings) #check if config is aay ok

if configIsGood == False:
    nn()
    ErrorMessage("The config file is incorrect/corrupted! Stopping...")
    time.sleep(2)
    exit()

LoadingBar(2, 5)

ListOfCommands = """-------------------------------------
The list of available commands is:
{}/help{}           Shows this message
{}/file <path>{}    Sends a file with a given path  
{}/game <text>{}    Sets a custom playing presence (use off for none)
{}/exit{}           Logs out and quits Pycord
-------------------------------------""".format(colour.BOLD, colour.NORMAL, colour.BOLD, colour.NORMAL, colour.BOLD, colour.NORMAL, colour.BOLD, colour.NORMAL, )

bot = discord.Client()
bot.PycConfig = settings
bot.PycConfig["commands"] = ListOfCommands

@bot.event
async def on_ready():
    LoadingBar(5, 5)
    print(" Loading finished!\nLogged into Discord via", bot.user.name)
    #sets the playing message
    if bot.PycConfig["Messenger"]["defaultGame"] != False:
        try:
            await bot.change_presence(activity=discord.Game(name=bot.PycConfig["Messenger"]["defaultGame"]))
        except Exception as e:
            ErrorMessage("Game Changing: {}".format(e))
    ###VARIABLES###
    ch = bot.get_channel(bot.PycConfig['Messenger']["channelId"])
    ######

    print(bot.PycConfig["commands"])

    while True:
        action = input("Pycord> ")
        if action == "" or action == " ":
            print("Unable to send empty messages!")

        elif action == "/exit":
            await bot.close()
            exit
        
        elif action.startswith("/file"):
            try:
                await ch.send(file=discord.File(action[6:]))
            except Exception as e:
                ErrorMessage("File sending: {}".format(e))
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
                await AsyncErrorMessage("Mesage sending: {}".format(e))

LoadingBar(3, 5)
def connect(botToken):
    """Connects the bot. Made function for threading module"""
    try:
        bot.run(botToken)
    except Exception as e:
        ErrorMessage("Login : {}".format(e))
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
    ErrorMessage("LoginError: {}".format(e))
    time.sleep(2)
