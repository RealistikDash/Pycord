#PyCord Responder
print("Starting PyCord Responder")
import discord
import asyncio
import random

bot = discord.Client()

@bot.event
async def on_ready():
		print("Logged in as", bot.user.name)
		while True :
			msg = input("Message: ")
			await bot.send_message(discord.Object(id='channelid'), msg)









bot.run("token")
