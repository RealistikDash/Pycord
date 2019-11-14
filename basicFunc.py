#Another global module. This one is for modules.
import time
import asyncio
import platform
import sys
from datetime import datetime
import json

with open('config.json') as json_file:
    settings = json.load(json_file)

#THE loading bar
def LoadingBar(value, endvalue, bar_length=20):
    """Loading bar cool right!"""

    percent = float(value) / endvalue #makes it percentage certified
    arrow = '-' * int(round(percent * bar_length)-1) + '>'
    spaces = ' ' * (bar_length - len(arrow))

    sys.stdout.write("\r[{0}] {1}%".format(arrow + spaces, int(round(percent * 100))))
    sys.stdout.flush()

class colour:
    #All this mess is because they dont show well at all on some systems. This is a basic estimate of what system this will work on
    PermittedOS = ["Linux", "Darwin"]
    CurrentOS = platform.system()
    if CurrentOS in PermittedOS or settings["ExperimantalMode"] == 1:
        PURPLE = "\033[95m"
        CYAN = "\033[96m"
        DARKCYAN = "\033[36m"
        BLUE = "\033[94m"
        GREEN = "\033[92m"
        YELLOW = "\033[93m"
        RED = "\033[91m"
        BOLD = "\033[1m"
        UNDERLINE = "\033[4m"
        NORMAL = "\033[0m"
    else:
        PURPLE = ""
        CYAN = ""
        DARKCYAN = ""
        BLUE = ""
        GREEN = ""
        YELLOW = ""
        RED = ""
        BOLD = ""
        UNDERLINE = ""
        NORMAL = ""



async def DateFormat(messageFormat, message):
    """Adds date etc to the line. Currently reserved for later"""
    return

def ErrorMessage(message):
    """Template for error messages (not finished)"""
    print("{}An error has occured with Pycord!\nError: {}{}".format(colour.YELLOW, message, colour.NORMAL))

async def AsyncErrorMessage(message):
    """Template for error messages. But guess what? It's asyncronous (not finished)"""
    print("{}An error has occured with Pycord!\nError: {}{}".format(colour.YELLOW, message, colour.NORMAL))

def ConfigIntegrityCheck(config):
    """Checks the integrity of the config and whether or not it will crash Pycord"""
    if type(config) is dict:
        try:
            #only real way of trying i know
            coolVariable = config["token"]
            coolVariable = config["ExperimantalMode"]
            coolVariable = config["Messenger"]
            if type(coolVariable) is dict:
                int(coolVariable["channelId"])
                coolVariable["defaultGame"] = coolVariable["defaultGame"]
                coolVariable = config["Viewer"]
                if type(coolVariable) is dict:
                    Viewer = config["Viewer"]
                    int(Viewer["ViewAll"])
                    for x in Viewer["ChannelWhitelist"]:
                        int(x)
                    int(Viewer["TimeFormat"])
                    return True
                else:
                    return False
            return False
        except Exception:
            return False

def nn():
    """Creates an empry line"""
    print("\n")

def TimeFormat(FormatNr, Message):
    """Responsible for putting a time in front of the msg"""
    if TimeFormat == 0:
        return Message

    elif FormatNr == 1:
        Time = datetime.now().strftime('%H:%M:%S')
        return "[{}] {}".format(Time, Message)

    elif FormatNr == 2:
        Time = datetime.now().strftime('%H:%M')
        return "[{}] {}".format(Time, Message)
    
    elif FormatNr == 3:
        Time = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        return "[{}] {}".format(Time, Message)

    else:
        return Message

def JsonOpen():
    """Opens the json settings file and converts to dict"""
    with open('config.json') as json_file:
        data = json.load(json_file)
        return data
