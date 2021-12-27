# Training Pack Bot
This is the repository for editing the custom discord bot that provides in-depth training pack integration with Discord to search through currated lists.

## Usage
- Default prefix is `!`
- search for training packs using command `!packs`
- ### TODO - maybe autogenerate these by pulling from the code. That would be pretty neat. No idea if it's possible


### Development

- Clone Repository
- Python 3 Environment
- Required packages are `python-dotenv` and `discord`
- create `.env` file in repository root level with the 2 following values
  - Token for the DevBot `BOTTOKENDEV = 'TOKEN HERE'`
  - API Bearer token available in `#version-0point1` pinned as `APIBEARER = 'BEARER HERE'`
- ## ABSOLUTELY DO NOT COMMIT THESE TWO TOKEN VALUES ANYWHERE FOR SECURITY REASONS

You can now change code for whatever you need for the bot and run it on command with the `TrainingPackBot.py` file.
