from typing import Text
import discord
import os
from os import listdir
from os.path import isfile, join
import aiosqlite
from dotenv import load_dotenv
from discordLevelingSystem import DiscordLevelingSystem, RoleAward, LevelUpAnnouncement
from pyparsing import Word

load_dotenv()


def micsid(ctx):
    return ctx.author.id == 481377376475938826 or ctx.author.id == 624076054969188363




from discord.ext import commands, tasks



intents = discord.Intents.all()
intents.presences = True
intents.members = True
intents.guilds=True

client = commands.Bot(command_prefix="!", intents=intents, presences = True, members = True, guilds=True, case_insensitive=True, allowed_mentions = discord.AllowedMentions(everyone=False))

async def update_activity(client):
    await client.change_presence(activity=discord.Game(f"On {len(client.guilds)} servers! | .help"))
    print("Updated presence")

@client.event
async def on_ready():
    # Setting `Playing ` status
    print("we have powered on, I an alive.")
    await update_activity(client)
    



with open('database/links.txt') as file:
    file = file.read().split()


#----------------------------------EVENTS----------------------------------

@client.event 
async def on_message(message):
    for badword in file:
        if badword in message.content.lower():
            await message.channel.send(f'{message.author.mention}! That Link is a scam. Please do not share it!')
            await message.add_reaction('<:SCAM:969878289537716234>')
        else:
            await client.process_commands(message)

with open('database/userfile.txt') as userfile:
    userfile = userfile.read().split('\n') 

@client.event
async def on_member_join(member):
    for names in userfile:
        if str(member.id) in names:
            print(f"{member.name} has joined the server!")
            user = member.guild.owner
            await user.send(f'{member.mention}! is a known scammer. He joined your server {member.guild.name} Please keep a eye on him and report any links he shares so we can add them to our database')


    
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