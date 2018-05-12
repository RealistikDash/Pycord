#PyCord Viewer
print("Starting PyCord ")
import discord
import asyncio
import random

bot = discord.Client()

@bot.event
async def on_ready():
	print("Logged in as", bot.user.name)


@bot.event
async def on_message(message):
	print("[",message.author,"in",message.channel, "]",message.clean_content)







bot.run("token")