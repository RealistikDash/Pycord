#Pycord Setup
#Imports
import os
from Pycord import moduleManagement as mm
from getpass import getpass
try:
  from Pycord import pycord
except ImportError:
  mm.installModule("colorama") # gets colorama for the pycord module
  from Pycord import pycord
  pycord.clear()

import time
###########################################

pycord.title("Pycord Setup")

sampleDict = { #Sample dictionary to save
  'botToken' : """""",
  'channelId' : '',
  'focusonchannel' : 0,
  'username' : ""
}

def checkForInt(var):
  """Checks if the given var is a number"""
  try: #Tries to change var into int
    var = int(var)
  except Exception:
    pycord.errorLog("Variable does not consist of only numbers. Aborting...")
    time.sleep(3)
    exit()

def editFile():
  #Function called to edit settings.py
  pycord.log("Settings file already found. A new file won't be created.")
  editFileQuestionmark = input("Do you want to edit your current settings? (y/N) ")
  editFileQuestionmark = editFileQuestionmark.lower()

  if editFileQuestionmark == "y": #The editing part
    #Grabs all the variables
    newUsername = input("Input your new username: ")
    newToken = getpass(prompt='Input your new token (invisible): ', stream=None)
    newChannelId = input("Input your new channel id: ")
    #Debug purposes
    try:
      checkForInt(newChannelId)
    except Exception:
      pycord.errorLog("checkForInt() failed!")
    #############################################
    newFocusMode = input("Do you want to enable Focus Mode? (Y/n)")

    newFocusMode = newFocusMode.lower()
    if newFocusMode == "n":
      newFocusMode = 0

    else:
      newFocusMode = 1

    file = open("settings.py","w+") #opens the file so it can be edited
    sampleDict['botToken'] = newToken
    sampleDict['channelId'] = newChannelId
    sampleDict['focusonchannel'] = newFocusMode
    sampleDict['username'] = newUsername

    settingsFile = "#This is the Pycord Save file. This is where all your Pycord information is stored. This is not to be ran but rater edited.\ndetails = {}".format(sampleDict)

    try:
      file.write(settingsFile) #writes to the file

    except Exception:
      pycord.errorLog("Error writing file! Aborting...")
      time.sleep(3)
      exit()
    file.close() #closes the file and applies changes

    pycord.log("Edit successful! Closing...")
    time.sleep(3)
    exit()





  elif editFileQuestionmark == "n":
    pycord.log("Quitting...")
    time.sleep(1)
    exit()

  else:
    pycord.log("Invalid response. Quitting...")
    time.sleep(1)
    exit()

#Welcome
print("-----------------------------------------")
print("Welcome to the Pycord setup.")
print("-----------------------------------------")
print("")

try: #Tries to import settings
  from settings import *
  editFile()

except ImportError: #except when you don't have it
  pycord.log("No settings file. Creating one.")
  x = input("Do you want to start the setup (y/N)? ")
  x = x.lower() #Changes x into lower case
  if x == "y":
    pycord.log("Starting to install modules...")
    mm.installModule("-r requirements.txt")
    pycord.log("Installing modules done!")
    time.sleep(1)
    pycord.log("Building modules for quicker imports...")

    #Module building
    try:
      import discord
    except ImportError:
      pycord.errorLog("Failed to import discord! Try re-running the setup.")
      time.sleep(3)
      exit()

    try:
      import requests
    except ImportError:
      pycord.errorLog("A non-fatal (for now) error occured. Failed to import requests!")
    import aiohttp
    try:
      from colorama import Fore, Back, Style
      from colorama import init
    except ImportError:
      pass

    ################

    pycord.log("Done!")
    pycord.log("Setting up bot.")
    botToken = getpass(prompt='Enter the bot token (invisible): ', stream=None)
    botChannelId = input("What channel shall the messages be sent to (channel id): ")
    checkForInt(botChannelId)
    focusModeOnQ = input("Do you want to enable Focus Mode (for viewer)? Y/n ")
    if focusModeOnQ == "n":
      focusModeEnabled = 0
    else:
      focusModeEnabled = 1
    username = input("Enter your Pycord Responder username: ")
    file = open("settings.py","w+") #creates a file called settings.py that will store all your variables

    sampleDict['botToken'] = botToken
    sampleDict['channelId'] = botChannelId
    sampleDict['focusonchannel'] = focusModeEnabled
    sampleDict['username'] = username

    settingsFile = "#This is the Pycord Save file. This is where all your Pycord information is stored. This is not to be ran but rater edited.\ndetails = {}".format(sampleDict)

    pycord.log("Attempting to write settings to file...")
    file.write(settingsFile) #writes to the file
    file.close() #applies the edits
    pycord.log("Done!")
    pycord.log("Setup complete!")
    print("-----------------------------------------")
    print("The Pycord setup was completed!")
    print("Exiting in 5 seconds...")
    print("-----------------------------------------")
    time.sleep(5)
    pycord.log("Exitting...")
    exit()
