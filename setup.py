#Pycord Setup
#Imports
from Pycord import moduleManagement as mm
from Pycord import pycord
import time
###########################################


#Welcome
print"-----------------------------------------")
print("Welcome to the Pycord setup.")
print("-----------------------------------------")
print("")
x = input("Do you want to start the setup (y/N)? ")
x = x.lower() #Changes x into lower case
if x == "y":
  pycord.log("Starting to install modules...")
  mm.installModule("-r requirements.txt")
  pycord.log("Installing modules done!")
  time.sleep(1)
  pycord.log("Building modules for quicker imports...")
  import discord
  import requests
  import aiohttp
  pycord.log("Done!")
  pycord.log("Setting up bot.")
  botToken = input("Enter the bot token you wish to use: ")
  botChannelId = input("What channel shall the messages be sent to (channel id): ")
  focusModeOnQ = input("Do you want to enable Focus Mode (for viewer)? Y/n ")
  if focusModeOnQ == "n":
    focusModeEnabled = 0
  else:
    focusModeEnabled = 1
  username = input("Enter your Pycord Responder username: ")
  file = open("settings.py","w+") #creates a file called settings.py that will store all your variables
  
  settingsFile = """#These are the bot settings for Pycord. This script is not to be ran. Pycord will just read it and get the variables from here
botToken = "{}"
channelId = "{}"
focusonchannel = {}
username = "{}"
  """.format(botToken, botChannelId, focusModeEnabled, username)
  
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
  
