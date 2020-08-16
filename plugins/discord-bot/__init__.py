plugin_meta = {
    "__author__" : "Intelligent Cat",
    "__name__" : "Discord bot",
    "__description__" : "A plugin for adding a Discord bot to GDPyS"
} # yeye this is plugin metadata

try:
    import discord # here i try to find discord.py, and if it doesnt find it, it just skips with a warning
except ImportError:
    print('Discord.py was not found, Discord bot won\'t be available.')
    exit()

from discord.ext import commands # i need this thing dont judge me
from botconfig import open_config

config = open_config()

if config == 0:
    print('Config file was generated. Please change it and run the bot again.')
    exit() # omg messy code!1!1!!1!!!1

bot = commands.Bot(command_prefix=commands.when_mentioned_or(config['bot-prefix']), case_insensitive=True) # yes making a new discord client

try:
    bot.run(config['bot-token']) # i run the bot yey
except:
    print('Could not run the bot. Please make sure the bot token in the config is correct.')
    exit()