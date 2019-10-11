#Another global module. This one is for modules.
import time
import asyncio

async def DateFormat(messageFormat, message):
    """Adds date etc to the line. Currently reserved for later"""
    return

def ErrorMessage(message):
    """Template for error messages (not finished)"""
    print("An error has occured with Pycord!\nError: {}".format(message))

async def AsyncErrorMessage(message):
    """Template for error messages. But guess what? It's asyncronous (not finished)"""
    print("An error has occured with Pycord!\nError: {}".format(message))

def ConfigIntegrityCheck(config):
    """Checks the integrity of the config and whether or not it will crash Pycord"""
    if type(config) is dict:
        try:
            #only real way of trying i know
            coolVariable = config["token"]
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
