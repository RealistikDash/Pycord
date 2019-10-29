#Another global module. This one is for modules.
import time
import asyncio
import platform
from config import *

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
                    return True
                else:
                    return False
            return False
        except Exception:
            return False

def nn():
    """Creates an empry line"""
    print("\n")
