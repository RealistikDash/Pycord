#PyCord Viewer by RealistikDash
print("Initialising Pycord Viewer")

#Required imports
import discord
import asyncio
######################################

#Welcome message
welcome= """---------------------------------------------------------------------
Welcome to Pycord Viewer
Pycord Viewer has succesfully logged into {}!
---------------------------------------------------------------------"""
######################################

#Focus channel (only recieve messages form a certain channel, set focuschannel to 0 to switch it off)
focusonchannel = 1
channelId = ''

#Bot Setup (setup your bot with a token)
botToken = ''
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