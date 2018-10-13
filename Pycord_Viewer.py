#PyCord Viewer by RealistikDash
print("Initialising Pycord Viewer")

#Required imports
try:
	import discord
	import asyncio
	import time
	from settings import * #Imports variables you set in the setup

except ImportError: #This is run if there is an error while importing
	pycord.errorLog("There was an error while importing! Pycord cannot continue. Make sure you ran setup.py before launching Pycord")
	print("")
	runSetup = input("Do you want to run the setup now? (y/N)")
	runSetup = runSetup.lower() #Turns runSetup into lower case letters
	
	if runSetup == "y":
		try:
			os.system("python setup.py")
			exit()
		except Exception: #In case the system uses "python3" for it's commands, that will happen
			os.system("python3 setup.py")
			exit()
		else:
			pycord.errorLog("There was an error while attempting to run the setup. Pycord cannot proceed.")
			time.sleep(3)
			exit()
######################################

#Welcome message
if focusonchannel == "0":
	welcome= """---------------------------------------------------------------------
Welcome to Pycord Viewer
Pycord Viewer has succesfully logged into {}!
---------------------------------------------------------------------
Connection status:
Focus Mode: Off
Ping: {}
---------------------------------------------------------------------"""
######################################

else:
	welcome= """---------------------------------------------------------------------
Welcome to Pycord Viewer
Pycord Viewer has succesfully logged into {}!
---------------------------------------------------------------------
Connection status:
Focus Mode: On (focusing on {})
Ping: {}
---------------------------------------------------------------------"""
######################################

bot = discord.Client()

@bot.event
async def on_ready():
	#Checks ping
	t1 = time.time()
	await bot.send_typing(discord.Object(id=channelId))
	t2 = time.time()
	ping = (t2-t1)*1000
	ping = round(ping, 2)
	######################################
	print(welcome.format(bot.user.name, channelId, ping))


#On message, the message is being displayed and who sent it.
@bot.event
async def on_message(message):
	if focusonchannel == 1:
		if message.channel.id == channelId:
			print("[",message.author,"in",message.channel, "]",message.clean_content)
	else:
		print("[",message.author,"in",message.channel, "]",message.clean_content)







try:
	bot.run(botToken) #Connects the bot.
except Exception:
	pycord.errorLog("Could not connect to Discord. Check your token. Login aborted.")
