import discord
from discord.ext import commands
from dotenv import load_dotenv
from os import getenv
import requests
import json
import sys
from HelperFunctions import *

load_dotenv()
isProd = getenv("BOTTOKENDEV") == None
bot = commands.Bot(command_prefix="!" if isProd else "~",
                   description="Custom bot to find training packs and run the Wayprotein discord made by Daelisk")
BASE_URL = ''
headers = {}


@bot.event
async def on_ready():
    print("Ready !")


@bot.command()
async def ping(ctx):
    await ctx.send('**pong**')


@bot.command()
async def allpacks(ctx, description="Get The Spreadsheet"):
    await ctx.send(
        'https://docs.google.com/spreadsheets/d/1riHFd8KBBO9IqmbUbKPzgSDVpKOQXcb2UYaUUwFDs6M/edit#gid=1648371681')


@bot.command()
async def tags(ctx, *args, descritption="Get the list of tags"):
    flags = {'sort': '', 'page': 1, 'order': 'desc'}
    getFlagsFromArgs(flags, args)
    errorText = ""
    if flags['order'] != 'desc' and flags['order'] != 'asc':
        errorText = "Order arguement must be 'asc' or 'desc' "
    if flags['sort'] != "" and flags['sort'] != 'packs':
        errorText = errorText + "Sort arguement must be 'packs' "
    if len(errorText) > 0:
        await ctx.send(errorText)
        return

    response = requests.request('GET', BASE_URL + 'tags', headers=headers, params=flags)
    data = response.json()['data']
    formattedOutput = getFormattedTagsOutput(data)
    await ctx.send(embed=formattedOutput)


# @bot.command()
# async def creators(ctx, descritption="Get the list of creators"):
#     response = requests.request('GET', BASE_URL + 'creators', headers=headers)
#     flags = {'sort': '', 'page': 1, 'order': 'desc'}
#     getFlagsFromArgs(flags, args)
#     errorText = ""
#     if flags['order'] != 'desc' and flags['order'] != 'asc':
#         errorText = "Order arguement must be 'asc' or 'desc' "
#     if flags['sort'] != "" and flags['sort'] != 'packs':
#         errorText = errorText + "Sort arguement must be 'packs' "
#     formattedOutput = discord.Embed(title="Here is a list of creators you can search by", color=discord.Color.blue())
#     formattedOutput.add_field(name="Creators", value=str(['{}\n'.format(creator) for creator in enumerate(response.json()['data'])]))


@bot.command()
async def packs(ctx,
                *args,
                help='Usage: `!packs`\t`!packs double tap creator=wayprotein sort=difficulty order=asc`',
                description="Get Training Packs"):
    # flags map on possible args/options. https://ballchasingcoach.com/docs#apiv1training-packs gives list
    flags = {'verbose': False, 'sort': '', 'page': 1, 'order': 'desc', 'creator': ''}
    oldArgsLen = len(args)
    args = [val for val in args if val != 'verbose']
    flags['verbose'] = oldArgsLen > len(args)
    getFlagsFromArgs(flags, args)
    errorText = ""
    if flags['order'] != 'desc' and flags['order'] != 'asc':
        errorText = "Order arguement must be 'asc' or 'desc' "
    if flags['sort'] != "" and flags['sort'] != 'difficulty':
        errorText = errorText + "Sort arguement must be 'difficulty' "
    if len(errorText) > 0:
        await ctx.send(errorText)
        return
    params = {'page': flags['page'], 'sort': flags['sort'], 'order': flags['order'], 'creator': flags['creator']}
    if len(args) > 0:
        params['query'] = " ".join(args)
    response = requests.request('GET', BASE_URL + 'training-packs', headers=headers, params=params)
    data = response.json()['data']

    formattedOutput = getFormattedPacksOutput(data, flags['verbose'])
    await ctx.send(embed=formattedOutput)


if __name__ == "__main__":
    BASE_URL = 'https://ballchasingcoach.com/api/v1/'
    headers = {
        'Authorization': 'Bearer ' + str(getenv("APIBEARER")),
        'Content-Type': 'application/json',
        'Accept': 'application/json',
    }
    bot.run(getenv("BOTTOKEN") if isProd else getenv("BOTTOKENDEV"))