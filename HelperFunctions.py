import discord
from BotStrings import *


def getFlagsFromArgs(flags, args):
    for i in range(len(args) - 1, -1, -1):
        arg = args[i]
        values = arg.split("=")
        if values[0] in flags:
            flags[values[0]] = values[1]
            args.remove(arg)


def getFormattedPacksOutput(data, isVerbose):
    formattedOutput = discord.Embed(title="Found Training Packs", color=discord.Color.blue())

    if (len(data) == 0):
        formattedOutput.add_field(name=BotStrings.NO_RESULTS.format('packs'),
                                  value="Try using only keywords, flags, or creators - !help packs")
        return formattedOutput

    if isVerbose:
        MAX_RESULTS = 6
        for index, entry in enumerate(data):
            if index >= MAX_RESULTS:
                break
            nameString = entry['creator']
            valueString = "{}\n{}\n{}\n{}\nNotes: {}\n{}".format(entry['name'],
                                                                 entry['code'],
                                                                 getEmojiForDifficulty(entry['difficulty']),
                                                                 entry['platform'],
                                                                 entry['notes'],
                                                                 entry['videoUrl'])
            formattedOutput.add_field(name=nameString, value=valueString)
        formattedOutput.set_footer(text=BotStrings.QUERY_MAXIMUM.format(MAX_RESULTS) +
                                   BotStrings.PACKS_SEARCH_REFINE)
    else:
        MAX_RESULTS = 12
        for index, entry in enumerate(data):
            if index >= MAX_RESULTS:
                break
            nameString = entry['creator']
            valueString = "{}\n{}\n{}".format(entry['name'], entry['code'], getEmojiForDifficulty(entry['difficulty']))
            formattedOutput.add_field(name=nameString, value=valueString)
        formattedOutput.set_footer(text=BotStrings.QUERY_MAXIMUM.format(MAX_RESULTS) +
                                   BotStrings.PACKS_SEARCH_REFINE)
    return formattedOutput


def getFormattedTagsOutput(data):
    formattedOutput = discord.Embed(title=BotStrings.LIST_OF_SEARCHABLE.format('tags'), color=discord.Color.blue())
    if len(data) == 0:
        formattedOutput.add_field(name=BotStrings.NO_RESULTS.format('tags'), value=BotStrings.TRY_REDUCED_PAGES)
        return formattedOutput

    tagsString = "".join(
        ['**{}** : {}\n'.format(tag["name"], tag['counts']['packs']) for index, tag in enumerate(data)])
    formattedOutput.add_field(name="Tag : Count", value=tagsString)
    MAX_RESULTS = 15
    formattedOutput.set_footer(text=BotStrings.QUERY_MAXIMUM.format(MAX_RESULTS) +
                               ' Change page number for more results `page=2`')
    return formattedOutput


def getFormattedCreatorsOutput(data):
    formattedOutput = discord.Embed(title=BotStrings.LIST_OF_SEARCHABLE.format('creators'), color=discord.Color.blue())

    if (len(data) == 0):
        formattedOutput.add_field(name=BotStrings.NO_RESULTS.format('creators'), value=BotStrings.TRY_REDUCED_PAGES)
        return formattedOutput

    creatorsString = "".join(
        ["**{}** : {}\n".format(creator['name'], creator['counts']['packs']) for index, creator in enumerate(data)])
    formattedOutput.add_field(name="Creator : Packs Count", value=creatorsString)
    MAX_RESULTS = 15
    formattedOutput.set_footer(text=BotStrings.QUERY_MAXIMUM.format(MAX_RESULTS) +
                               ' Change page number for more results `page=2`')
    return formattedOutput


def getEmojiForDifficulty(difficulty) -> str:
    emojis = {
        'Supersonic Legend': '<:Supersonic_Legend:849650907364982824>',
        'Grand Champion': '<:Grand_champion3:849650869129576479>',
        'Champion': '<:Champion3:849650848308658206>',
        'Diamond': '<:Diamond3:849650835620495360>',
        'Platinum': '<:Platinum3:849650882089189386>',
        'Gold': '<:Gold3:849650858505535548>',
        'Silver': '<:Silver3:849650894182023228>',
        'Bronze': '<:Bronze3:849650820692705300>',
        'Viewer': '<:Viewer:850202932544012309>'
    }

    if difficulty == "":
        return emojis['Viewer']
    try:
        code = emojis[str(difficulty)]
    except KeyError:
        return difficulty
    return code