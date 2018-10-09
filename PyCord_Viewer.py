#PyCord Viewer by RealistikDash
print("Initialising Pycord Viewer")

#Required imports
import discord
import asyncio
from settings import * #Imports variables you set in the setup
######################################

#Welcome message
welcome= """---------------------------------------------------------------------
Welcome to Pycord Viewer
Pycord Viewer has succesfully logged into {}!
---------------------------------------------------------------------"""
######################################

bot = discord.Client()

@bot.event
async def on_ready():
	print(welcome.format(bot.user.name))


#On message, the message is being displayed and who sent it.
@bot.event
async def on_message(message):
	if focusonchannel == 1:
		if message.channel.id == channelId:
			print("[",message.author,"in",message.channel, "]",message.clean_content)
	else:
		print("[",message.author,"in",message.channel, "]",message.clean_content)







bot.run(botToken)
