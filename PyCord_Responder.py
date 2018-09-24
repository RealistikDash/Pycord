#PyCord Responder by RealistikDash
#From https://github.com/RealistikDash/PyCord
print("Initialising Pycord Responder")

#All the necessary imports
import discord
import asyncio
import random
######################################

#Bot Values (without editing them Pycord won't work)
channelId = "" #channel id check thing
botToken = "" #bot token
######################################


#Commands List
cmdlist="""The currently available commands are:
Discord Based Commands
-/setgame		Sets your presence to a given input.
-/sendfile		Sends a file with a given name.
-/customsend	Lets you choose the variables such as the channel id, message and any other attributes.
-/changeuser	Changes your Pycord username.
-/sendtxt		Sends the contents of a specified txt file.
-/changeid		Changes the channel id to which your messages are being sent to."""
######################################

#Tips
tips = ["Is the Discord AIP blocked too? Try using repl.it and run Pycord there!"]
######################################

bot = discord.Client()


@bot.event
async def on_ready():
		print("[Pycord Info] Logged into", bot.user.name)
		username = input("[Pycord] Enter a username: ")
		await bot.change_presence(game=discord.Game(name=username + " is using Pycord"))
		#Welcome message
		print("Welcome to Pycord {}!".format(username))
		print(cmdlist)
		print("---------------------------------------------------------------------")
		print(random.choice(tips))
		print("---------------------------------------------------------------------")
		######################################

		while True :
			msg = input("Pycord> ")
			#Checks if the msg is empty
			if msg == "":
				print("[Pycord Error] Cannot send empty message.")
			#Changes the presence
			elif msg.startswith("/setgame"):
				game = msg[9:]
				await bot.change_presence(game=discord.Game(name=game))
				print("[Pycord Info] Game set to {}".format(msg[9:]))
			#Send file command (Use: /sendfile file.png), all formats supported as long as it is under 8MB
			elif msg.startswith("/sendfile"):
				print("[Pycord Info] Sending file {}...".format(msg[10:]))
				await bot.send_file(discord.Object(id=channelId), msg[10:])
			#Lets the user set the parameters for the send
			elif msg.startswith("/customsend"):
				print("[Pycord Info] Attempting custom send...")
				eval("""await bot.send_message({})""".format(msg[12:]))
			#Changes pycord username
			elif msg.startswith("/changeuser"):
				username = msg[12:]
				print("[Pycord Info] Username changed to {}".format(username))
			#Import custom modules for use with /customsend
			elif msg.startswith("/python.import"):
				eval("import {}".format(msg[15:]))
				print("[Pycord Info] Import attempted. Successful unless given an error.")
			#Opens a text file and says it's contents in discord
			elif msg.startswith("/sendtxt"):
				file = open(msg[9:], 'r')
				print("[Pycord Info] Sending txt file...")
				await bot.send_message(discord.Object(id=channelId), """`[{}]` TXT FILE 
""".format(username) + file.read())
			#Change channel ID
			elif msg.startswith("/changeid"):
				channelId = msg[10:]
			#Lists all the commands
			elif msg.startswith("/help"):
				print(cmdlist)
			#If none of the requirements above are met, send the message
			else:
				await bot.send_message(discord.Object(id=channelId), "`[{}]` {}".format(username, msg))


bot.run(botToken) #Connects the bot.
