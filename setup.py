#Pycord Setup
#Imports
from Pycord import moduleManagement as mm
from Pycord import pycord
import time
###########################################


#Welcome
print("-----------------------------------------")
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
  pycord.log("Setup complete!")
  print("-----------------------------------------")
  print("The Pycord setup was completed!")
  print("Exiting in 5 seconds...")
  print("-----------------------------------------")
  time.sleep(5)
  pycord.log("Exitting...")
  exit()
  
