#PyCord Responder by RealistikDash
#From https://github.com/RealistikDash/PyCord
print("Initialising Pycord Responder")

#All the necessary imports
try:
	from Pycord import pycord
except ImportError:
	print("Could not import the Pycord module! Cannot continue!")
	exit()
try: #Attempts to import
	import discord
	import asyncio
	import random
	import time
	from Pycord import pycord
	import os
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
			try:
				os.system("python3 setup.py")
				exit()
			except Exception:
				pycord.errorLog("There was an error while attempting to run the setup. Pycord cannot proceed.")
				time.sleep(3)
				exit()
######################################

#Message list
cmdlist="""The currently available commands are:
Discord Based Commands
-/setgame		Sets your presence to a given input.
-/sendfile		Sends a file with a given name.
-/customsend		Lets you choose the variables such as the channel id, message and any other attributes.
-/changeuser		Changes your Pycord username (does not edit settings.py and therefore is temporary).
-/sendtxt		Sends the contents of a specified txt file.
-/embed 		Sends an embed with your selected variables (Usage: /embed [title] - [content])
-/changeid		Changes the channel id to which your messages are being sent to.
-/shrug			Sends a ¯\_(ツ)_/¯
-/ping			Measures the speed of your connection to discord (lower is better)
-/exit			Exits Pycord"""


exitMsg = """---------------------------------------------------------------------
Thank you for using Pycord!
Make sure to report any issues on GitHub.
The program will turn off in 3 seconds
---------------------------------------------------------------------"""
######################################

#Tips
tips = ["Is the Discord AIP blocked too? Try using repl.it and run Pycord there!"]
######################################

bot = discord.Client()

#Makes variables accessable in on_ready()
bot.pycordUsername = username
bot.channelId = channelId
#########################################


@bot.event
async def on_ready():
		try:
			channelId = bot.channelId
			username = bot.pycordUsername
		except Exception:
			pass
		
		###MISSING VARIABLE CHECK###
		try:
			channelId = channelId #checks if the variable can be accessed
			
		except Exception:
			errorForId = 1
			pycord.errorLog("Error loading channel id from file...")
			while errorForId == 1: #A loop that is run while the user is entering their new channel id
				channelId = input("Please enter the channel id: ")
				if pycord.checkNumber(channelId) == 'false': #checknumber returns true if it is a number and false if it itn't
					pycord.errorLog("Invalid channel id!")
				else:
					errorForId = 0
					break
			
		try:
			username = username #checks if the variable can be accessed
				
		except Exception:
			pycord.errorLog("Error getting username from settings.py...")
			usernameLoop = 1
			while usernameLoop == 1: #cheks for invalid usernames
				username = input("Enter your username: ")
				if username == "":
					pycord.errorLog("Invalid username!")
				if username == " ":
					pycord.errorLog("Invalid username!")
				else:
					usernameLoop = 0
					break
					
		channelId = discord.Object(id=channelId) #Makes the variable a discord object
		
		#####################################
		
		#Checks ping
		t1 = time.time()
		await bot.send_typing(channelId)
		t2 = time.time()
		ping = (t2-t1)*1000
		ping = round(ping, 2)
		######################################
		
		pycord.log("Logged into {}".format(bot.user.name)) #Sets game
		
		#Welcome message
		print("Welcome to Pycord {}!".format(username))
		print(cmdlist)
		print("---------------------------------------------------------------------")
		print("Connection info:")
		print("Logged into: {}".format(bot.user.name))
		print("Your ping is: {}".format(ping))
		print("---------------------------------------------------------------------")
		print(random.choice(tips))
		print("---------------------------------------------------------------------")
		######################################
		
		await bot.send_message(channelId, "**{}** logged into Pycord.".format(username))

		while True : #The main loop
			
			
			msg = input("Pycord> ")
			#Checks if the msg is empty
			if msg == "":
				pycord.errorLog("Cannot send empty message.")

			#Changes the presence
			elif msg.startswith("/setgame"):
				game = msg[9:]
				await bot.change_presence(game=discord.Game(name=game))
				pycord.log("Game set to {}".format(msg[9:]))

			#Send file command (Use: /sendfile file.png), all formats supported as long as it is under 8MB
			elif msg.startswith("/sendfile"):
				pycord.log("Sending file {}...".format(msg[10:]))
				try:
					await bot.send_file(channelId, msg[10:])
				
				except Exception:
					pycord.errorLog("An error occured while sending the file...")

			#Lets the user set the parameters for the send
			elif msg.startswith("/customsend"):
				pycord.log("Attempting custom send...")
				eval("""await bot.send_message({})""".format(msg[12:]))

			#Changes pycord username
			elif msg.startswith("/changeuser"):
				username = msg[12:]
				pycord.log("Username changed to {}".format(username))

			#Opens a text file and says it's contents in discord
			elif msg.startswith("/sendtxt"):
				try:
					file = open(msg[9:], 'r')
					pycord.log("Sending txt file...")
					try:
						await bot.send_message(channelId, """`[{}]` TXT FILE 
""".format(username) + file.read())
					except Exception:
						pycord.errorLog("An error occured while sending the message...")
				except Exception:
					pycord.errorLog("An error occured opening the file...")
			
			#Change channel ID
			elif msg.startswith("/changeid"):
				channelIdNew = msg[10:]
				if pycord.checkNumber(channelIdNew) == false: #Checks if channelIdNew is a number or not. If it fails, the below is executed.
					pycord.errorLog("Could not change the id. Failed checkNumber check.")
				else:
					channelId = discord.Object(id=channelIdNew)
					pycord.log("Channel Id changed to {}".format(channelId))

			#Lists all the commands
			elif msg.startswith("/help"):
				print(cmdlist)

			#Exits PyCord
			elif msg.startswith("/exit"):
				print(exitMsg)
				time.sleep(3)
				await bot.send_message(channelId, "**{}** logged out of Pycord.".format(username))
				await bot.close() #Logs out
				break #Breaks the loop
			
			#Sends the shrug emote
			elif msg.startswith("/shrug"):
				try:
					await bot.send_message(channelId, "`[{}]` ¯\_(ツ)_/¯".format(username))
				except Exception:
					pycord.errorLog("An error occured while sending the message...")
			
			#A ping command
			elif msg.startswith("/ping"):
				try:
					t1 = time.time()
					await bot.send_typing(channelId)
					t2 = time.time()
					ping = (t2-t1)*1000
					ping = round(ping, 2)
					pycord.log("Your ping is {}ms".format(ping))
					
				except Exception:
					pycord.errorLog("An error occured while sending the message...")
			
			#Embed command
			elif msg.startswith("/embed"):
				args = msg[7:]
				try:
					title, content = args.split("-")
					content = content[1:]
					embed = discord.Embed(title=title, description=content)
					try:
						await bot.send_message(channelId, embed=embed)
					except Exception:
						pycord.errorLog("Failed sending the message")
				except Exception:
					pycord.errorLog("Splitting failed. Required argumends might have not been met. Make sure to split the title and content with a dash and space like '- '.")
				
					

			#If none of the requirements above are met, send the message
			else:
				try:
					await bot.send_message(channelId, "`[{}]` {}".format(username, msg))
				except Exception:
					pycord.errorLog("An error occured while sending the message...")
		
		pycord.log("Loop broken")

try:
	bot.run(botToken) #Connects the bot.
except Exception:
	pycord.errorLog("Could not connect to Discord. Check your token. Login aborted.")
	time.sleep(3)
	exit()
