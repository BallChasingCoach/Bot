import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv

bot = commands.Bot(command_prefix="!", description="The description")
load_dotenv()

@bot.event
async def  on_ready():
    print("Ready !")

@bot.command()
async def ping(ctx):
    await ctx.send('**pong**')

bot.run(getenv("BOTTOKENDEV"))