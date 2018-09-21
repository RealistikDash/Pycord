#PyCord Responder by RealistikDash
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
		print("Logged in as", bot.user.name)
		username = input("Enter a username: ")
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
				print("Please write a message! Empty messages cannot be sent!")
			#Changes the presence
			elif msg.startswith("/setgame"):
				game = msg[9:]
				await bot.change_presence(game=discord.Game(name=game))
				print("Game set to " + msg[9:])
			#Send file command (Use: /sendfile file.png), all formats supported as long as it is under 8MB
			elif msg.startswith("/sendfile"):
				print("Sending file...")
				await bot.send_file(discord.Object(id=channelId), msg[10:])
			#Lets the user set the parameters for the send
			elif msg.startswith("/customsend"):
				print("Attempting custom send...")
				eval("""await bot.send_message(""" + msg[12:] + ")")
			#Changes pycord username
			elif msg.startswith("/changeuser"):
				username = msg[12:]
				print("Username changed to " + username)
			#Import custom modules for use with /customsend
			elif msg.startswith("/python.import"):
				eval("import " + msg[15:])
				print("Import attempted. Successful unless given an error.")
			#Opens a text file and says it's contents in discord
			elif msg.startswith("/sendtxt"):
				file = open(msg[9:], 'r')
				await bot.send_message(discord.Object(id=channelId), file.read())
			#Change channel ID
			elif msg.startswith("/changeid"):
				channelId = msg[10:]
			#If none of the requirements above are met, send the message
			else:
				await bot.send_message(discord.Object(id=channelId), "`[" + username + "]` " + msg)


bot.run(botToken) #Connects the bot.