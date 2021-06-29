import discord
from discord.ext import commands, tasks
import random

bot = commands.Bot(command_prefix = "!", description = "Bot de Titouan")
status = ["!help",
		"A votre service",
		"je suis un bot qui protege vos serveur ", 
		"bot crée par Worksase#7777", 
		]

@bot.event
async def on_ready():
	print("Ready !")
	changeStatus.start()

@bot.command()
async def start(ctx, secondes = 20):
	changeStatus.change_interval(seconds = secondes)

@tasks.loop(seconds = 5)
async def changeStatus():
	game = discord.Game(random.choice(status))
	await bot.change_presence(status = discord.Status.dnd, activity = game)
    
bot.run("")
