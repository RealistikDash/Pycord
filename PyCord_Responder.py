#PyCord Responder
print("Starting PyCord Responder")
import discord
import asyncio
import random



bot = discord.Client()

@bot.event
async def on_ready():
		print("Logged in as", bot.user.name)
		game = input("What shall the playing message be? (say none for no game) ")
		if game != "none":
			await bot.change_presence(game=discord.Game(name=game))
		while True :
			msg = input("Message: ")
			await bot.send_message(discord.Object(id='channel id'), msg)









bot.run("token")
