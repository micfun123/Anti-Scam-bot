from typing import Text
import discord
import aiohttp
import os
from os import listdir
from os.path import isfile, join
import json
import os
from dotenv import load_dotenv
from pretty_help import DefaultMenu, PrettyHelp
from discordLevelingSystem import DiscordLevelingSystem, RoleAward, LevelUpAnnouncement

load_dotenv()


def micsid(ctx):
    return ctx.author.id == 481377376475938826 or ctx.author.id == 624076054969188363




from discord.ext import commands, tasks


intents = discord.Intents.all()
intents.presences = True
intents.members = True
intents.guilds=True

client = commands.Bot(command_prefix="!", intents=intents, presences = True, members = True, guilds=True, case_insensitive=True, allowed_mentions = discord.AllowedMentions(everyone=False),  help_command=PrettyHelp())

@client.event
async def on_ready():
    # Setting `Playing ` status
    print("we have powered on, I an alive.")
    await update_activity(client)
    channel = client.get_channel(925787897527926805)
    await channel.send("Online")




# Custom ending note
menu = DefaultMenu(page_left="◀", page_right="▶", remove="❌", active_time=10)

# Custom ending note
ending_note = "Thank you for using simplex!\nIf you have any questions or concerns feel free to DM me.\n "

client.help_command = PrettyHelp(menu=menu, ending_note=ending_note, color=0x20BEFF)

async def update_activity(client):
    await client.change_presence(activity=discord.Game(f"On {len(client.guilds)} servers! | .help"))
    print("Updated presence")








    
TOKEN = os.getenv("DISCORD_TOKEN")

def start_bot(client):
    lst = [f for f in listdir("cogs/") if isfile(join("cogs/", f))]
    no_py = [s.replace('.py', '') for s in lst]
    startup_extensions = ["cogs." + no_py for no_py in no_py]
    try:
        for cogs in startup_extensions:
            client.load_extension(cogs)  # Startup all cogs
            print(f"Loaded {cogs}")

        print("\nAll Cogs Loaded\n===============\nLogging into Discord...")
        client.run(TOKEN) # Token do not change it here. Change it in the .env if you do not have a .env make a file and put DISCORD_TOKEN=Token 

    except Exception as e:
        print(
            f"\n###################\nPOSSIBLE FATAL ERROR:\n{e}\nTHIS MEANS THE BOT HAS NOT STARTED CORRECTLY!")



start_bot(client)