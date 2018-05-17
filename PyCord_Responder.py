#PyCord Responder
print("Starting PyCord Responder")
import discord
import asyncio
import random



bot = discord.Client()

@bot.event
async def on_ready():
		print("Logged in as", bot.user.name)
		username = input("Username: ")
		await bot.change_presence(game=discord.Game(name=username + " is using Pycord"))

		while True :
			msg = input("Message: ")
			#replace the "channel id" with the id of the channel you want to talk in
			await bot.send_message(discord.Object(id='channel id'), "`[" + username + "]` " + msg)








#replace the token with a bot token or bot.run("email","password") for user accounts
bot.run("token")