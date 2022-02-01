class BotStrings:
    # General
    WEBSITE_URL = "https://prejump.com/"
    QUERY_MAXIMUM = "This query returns a maximum of {} results."
    LIST_OF_SEARCHABLE = "Here is a list of all {} that can be searched by"
    HELP = "Bot dedicated to accessing Training Packs in Rocket League.\nFurther help can be found in original server"

    # AllPacks
    ALLPACKS_DESC = "Get The Spreadsheet"
    ALLPACKS_LINK = 'https://docs.google.com/spreadsheets/d/1riHFd8KBBO9IqmbUbKPzgSDVpKOQXcb2UYaUUwFDs6M/edit#gid=1648371681'

    # Packs
    PACKS_DESC = "Get training packs according to search criteria. Complex search suggest using /packs as guide."
    PACKS_HELP = "```**How to search**\n`!packs [Enter search terms here]` \n\nSearch term can include keywords from the title, creator, difficulty, or any combination \n\nexamples \n```!packs Wayprotein \n!packs Wayprotein Air Roll\n !Packs \"Wayprotein Air Roll Diamond\"```Optional Flags - \n *Page*: Returns that page of results from the Packs Search. Default 1 `page=2` \n*Creator*: Limit by pack creator `creator=Wayprotein` \n*Sort*: Choose how to sort the returned packs. Default order is order entered in Packs list. Current only option is difficulty `sort=difficulty` \n*Order*: Choose whether to start from the top or bottom of the packs returned. Default is descending order `sort=asc` \n*Verbose*: Get more detailed information about the packs returned `verbose` \n\n```!packs wayprotein save verbose sort=difficulty order=asc```"
    PACKS_SEARCH_REFINE = ' Refine the search or read up with !help packs'
    # Creators
    CREATORS_DESC = "Get creators according to search criteria. Complex search suggest using /creators as guide."
    # Tags
    TAGS_DESC = "Get tags according to search criteria. Complex search suggest using /tags as guide."

    # Server
    SERVER_DESC = "Get Server Link"
    SERVER_MSG = "Join the Wayprotein coaching discord here!\nhttps://discord.gg/eY2ycv3W2N"

    # Error Strings
    ORDER_ASCENDING_DESCENDING = "Order arguement must be 'asc' or 'desc' "
    SORT_ARGUEMENTS = "Sort arguement must be '{}' "
    NO_RESULTS = "No {} found"
    CONTACT_ADMINS = "Please Contact Bot and API Administrators (Daelisk#0001 & onlyray#9285)"
    TRY_REDUCED_PAGES = "Try reducing the page number."