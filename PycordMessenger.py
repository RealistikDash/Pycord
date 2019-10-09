print("Loading Pycord Messenge...")
print("Please note that this is a veeeery early version and might be buggy if it works at all.")
import sys #loadingbar requirement

#THE loading bar
def LoadingBar(value, endvalue, bar_length=20):
    """Loading bar cool right!"""

    percent = float(value) / endvalue #makes it percentage certified
    arrow = '-' * int(round(percent * bar_length)-1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write("\rPercent: [{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
    sys.stdout.flush()

LoadingBar(0, 5)

try:
    import time
    import asyncio
    from discord.ext import commands
    import discord
    from config import *
    from basicFunc import *
except Exception as e:
    print("Critical error occured during imports of critical modules!")

LoadingBar(1, 5)

configIsGood = ConfigIntegrityCheck(settings) #check if config is aay ok

if configIsGood == False:
    ErrorMessage("The config file is incorrect/corrupted! Stopping...")
    time.sleep(2)
    exit()

LoadingBar(2, 5)

bot = discord.Client()

@bot.event
async def on_ready():
    LoadingBar(5, 5)
    print("Loading finished!\n Logged into Discord via", bot.user.name)

LoadingBar(3, 5)

try:
    bot.run(settings["token"])
except Exception as e:
    print("\n")
    ErrorMessage("LoginError: {}".format(e))