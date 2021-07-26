import discord
from discord.ext import commands
from discord_slash import SlashCommand
from discord_slash.utils.manage_commands import create_option, create_choice
from dotenv import load_dotenv
from os import getenv
import requests
import json
import sys
from HelperFunctions import *
from BotStrings import *

load_dotenv()
isProd = getenv("BOTTOKENDEV") == None
bot = commands.Bot(command_prefix="!" if isProd else "~",
                   description="Custom bot to find training packs and run the Wayprotein discord made by Daelisk")
slash = SlashCommand(bot, sync_commands=True)
BASE_URL = ''
headers = {}
guild_ids = None if isProd else [836296449070727238]


@bot.event
async def on_ready():
    print("Ready {}".format(bot.command_prefix))


@slash.slash(name='ping', guild_ids=guild_ids)
async def _ping(ctx):
    await ping(ctx)


@bot.command()
async def ping(ctx):
    await ctx.send('**pong**')


@slash.slash(name='allpacks', guild_ids=guild_ids, description="Get The Spreadsheet")
async def _allpacks(ctx):
    await allpacks(ctx)


@bot.command()
async def allpacks(ctx, description="Get The Spreadsheet"):
    await ctx.send(
        'https://docs.google.com/spreadsheets/d/1riHFd8KBBO9IqmbUbKPzgSDVpKOQXcb2UYaUUwFDs6M/edit#gid=1648371681')


@slash.slash(name='tags',
             description="Get the list of tags",
             guild_ids=guild_ids,
             options=[
                 create_option(name='sort',
                               required=False,
                               option_type=3,
                               description='How to sort the tags',
                               choices=[create_choice(name="Packs", value='packs')]),
                 create_option(name='order',
                               required=False,
                               description='Order',
                               option_type=3,
                               choices=[
                                   create_choice(name="Descending", value='desc'),
                                   create_choice(name="Ascending", value="asc")
                               ]),
                 create_option(name="page", required=False, description="Page number", option_type=4)
             ])
async def _tags(ctx, **kwargs):
    await tags(ctx, *[f"{key}={value}" for key, value in kwargs.items()])


@bot.command()
async def tags(ctx, *args, descritption="Get the list of tags"):
    flags = {'sort': '', 'page': 1, 'order': 'desc'}
    getFlagsFromArgs(flags, list(args))
    errorText = ""
    if flags['order'] != 'desc' and flags['order'] != 'asc':
        errorText += BotStrings.ORDER_ASCENDING_DESCENDING
    if flags['sort'] != "" and flags['sort'] != 'packs':
        errorText += BotStrings.SORT_ARGUEMENTS.format('packs')
    if len(errorText) > 0:
        await ctx.send(errorText)
        return

    response = requests.request('GET', BASE_URL + 'tags', headers=headers, params=flags)
    data = response.json()['data']
    formattedOutput = getFormattedTagsOutput(data)
    await ctx.send(embed=formattedOutput)


@slash.slash(
    name='Creators',
    description="Get the list of Creators",
    guild_ids=guild_ids,
    options=[
        create_option(name='sort',
                      required=False,
                      option_type=3,
                      description='How to sort the Creators',
                      choices=[create_choice(name="Packs", value='packs'), create_choice(name="Name", value='name')]),
        create_option(
            name='order',
            required=False,
            description='Order',
            option_type=3,
            choices=[create_choice(name="Descending", value='desc'), create_choice(name="Ascending", value="asc")]),
        create_option(name="page", required=False, description="Page number", option_type=4)
    ])
async def _creators(ctx, **kwargs):
    await creators(ctx, *[f"{key}={value}" for key, value in kwargs.items()])


@bot.command()
async def creators(ctx, *args, descritption="Get the list of creators"):
    flags = {'sort': '', 'page': 1, 'order': 'desc'}
    getFlagsFromArgs(flags, list(args))
    errorText = ""
    if flags['order'] != 'desc' and flags['order'] != 'asc':
        errorText += BotStrings.ORDER_ASCENDING_DESCENDING
    if flags['sort'] != "" and flags['sort'] != 'name':
        errorText += BotStrings.SORT_ARGUEMENTS.format('name')
    flags['sort'] = '' if flags['sort'] == 'name' else 'packs'
    response = requests.request('GET', BASE_URL + 'creators', headers=headers, params=flags)
    formattedOutput = getFormattedCreatorsOutput(response.json()['data'])
    await ctx.send(embed=formattedOutput)


@slash.slash(name='packs',
             description="Get the list of training packs",
             guild_ids=guild_ids,
             options=[
                 create_option(name='query', required=False, description="What to search for", option_type=3),
                 create_option(name='sort',
                               required=False,
                               option_type=3,
                               description='How to sort the tags',
                               choices=[create_choice(name="Difficulty", value='difficulty')]),
                 create_option(name='creator', required=False, description="Search by Creator", option_type=3),
                 create_option(name='order',
                               required=False,
                               description='Order',
                               option_type=3,
                               choices=[
                                   create_choice(name="Descending", value='desc'),
                                   create_choice(name="Ascending", value="asc")
                               ]),
                 create_option(name="verbose", required=False, description="Detailed Packs Output", option_type=5),
                 create_option(name="page", required=False, description="Page number", option_type=4)
             ])
async def _packs(ctx, **kwargs):
    await packs(ctx, *[f"{key}={value}" if key != 'query' else f"{value}" for key, value in kwargs.items()])


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
        errorText += BotStrings.ORDER_ASCENDING_DESCENDING
    if flags['sort'] != "" and flags['sort'] != 'difficulty':
        errorText += BotStrings.SORT_ARGUEMENTS.format('difficulty')
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