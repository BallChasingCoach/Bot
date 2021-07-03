import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
import requests
import json
import sys
from HelperFunctions import *

load_dotenv()
BASE_URL = 'https://ballchasingcoach.com/api/v1/'
headers = {
    'Authorization': 'Bearer ' + str(getenv("APIBEARER")),
    'Content-Type': 'application/json',
    'Accept': 'application/json',
}
bot = commands.Bot(command_prefix="!", description="The description")

@bot.event
async def  on_ready():
    print("Ready !")

@bot.command()
async def ping(ctx):
    await ctx.send('**pong**')

@bot.command()
async def packs(ctx, *args):
    isVerbose = False
    if 'verbose' in args:
        args = [val for val in args if val != 'verbose']
        isVerbose = True
    params = {'page': 1}

    # not sure how this works with the query, ask Ray
    if len(args) > 0:
        params['query'] = ",".join(args)
    response = requests.request('GET', BASE_URL + 'training-packs', headers=headers, params=params)
    data = response.json()['data']
    formattedOutput = discord.Embed(title="Found Training Packs", color=discord.Color.blue())
    if isVerbose:
        [formattedOutput.add_field(name="{}".format(entry['creator']), value="{}\n{}\n{}\n{}\nNotes: {}\n{}".format(
            entry['name'],
            entry['code'], 
            getEmojiForDifficulty(entry['difficulty']), 
            entry['platform'],
            entry['notes'],
            entry['videoUrl'])) 
            for index, entry in enumerate(data) if index < 6]
        formattedOutput.set_footer(text='This query returns a maximum of 6 results, refine the search of check #browse-packs for more')
    else:
        [formattedOutput.add_field(name="{}".format(entry['creator']), value="{}\n{}\n{}".format(
            entry['name'],
            entry['code'], 
            getEmojiForDifficulty(entry['difficulty']))) 
            for index, entry in enumerate(data) if index < 12]
        formattedOutput.set_footer(text='This query returns a maximum of 12 results, refine the search of check #browse-packs for more')
    await ctx.send(embed=formattedOutput)
    
if __name__ == "__main__":
    bot.run(getenv("BOTTOKEN"))