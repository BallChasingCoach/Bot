

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