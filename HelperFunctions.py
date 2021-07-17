import discord

def getFlagsFromArgs(flags, args):
    for i in range(len(args) -1, -1, -1):
        arg = args[i]
        values = arg.split("=")
        if values[0] in flags:
            flags[values[0]] = values[1]
            args.remove(arg)

def getFormattedPacksOutput(data, isVerbose):
    formattedOutput = discord.Embed(title="Found Training Packs", color=discord.Color.blue())

    if(len(data) == 0):
        formattedOutput.add_field(name="No Packs Found", value="Try using only keywords or flags - !help packs")
        return formattedOutput

    if isVerbose:
        [formattedOutput.add_field(name="{}".format(entry['creator']), value="{}\n{}\n{}\n{}\nNotes: {}\n{}".format(
            entry['name'],
            entry['code'], 
            getEmojiForDifficulty(entry['difficulty']), 
            entry['platform'],
            entry['notes'],
            entry['videoUrl'])) 
            for index, entry in enumerate(data) if index < 6]
        formattedOutput.set_footer(text='This query returns a maximum of 6 results, refine the search or check #browse-packs for more')
    else:
        [formattedOutput.add_field(name="{}".format(entry['creator']), value="{}\n{}\n{}".format(
            entry['name'],
            entry['code'], 
            getEmojiForDifficulty(entry['difficulty']))) 
            for index, entry in enumerate(data) if index < 12]
        formattedOutput.set_footer(text='This query returns a maximum of 12 results, refine the search or check #browse-packs for more')
    return formattedOutput

def getEmojiForDifficulty(difficulty) -> str:
    emojis = { 'Supersonic Legend': '<:Supersonic_Legend:849650907364982824>',
    'Grand Champion':'<:Grand_champion3:849650869129576479>',
    'Champion': '<:Champion3:849650848308658206>',
    'Diamond': '<:Diamond3:849650835620495360>',
    'Platinum': '<:Platinum3:849650882089189386>',
    'Gold': '<:Gold3:849650858505535548>',
    'Silver': '<:Silver3:849650894182023228>',
    'Bronze': '<:Bronze3:849650820692705300>',
    'Viewer': '<:Viewer:850202932544012309>' }

    if difficulty == "":
        return emojis['Viewer']
    try:
        code = emojis[str(difficulty)]
    except KeyError:
        return difficulty
    return code