from typing import Text
import discord
import os
from os import listdir
from os.path import isfile, join
import os
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

@client.event
async def on_server_join(guild):
    await update_activity(client)
    await guild.owner.send(f"Hey thank you for helping to fight scams to report a scam please use our discord or spead to the maker. If this bot helps please feel free to donate to keep the database alive \n <https://www.buymeacoffee.com/Michaelrbparker> \n <https://discord.gg/FQHbfnC7hE>")
    

@client.slash_command()
async def reportlink(ctx,message:str):
    await ctx.respond(f"<{message}> has been reported")
    reportchannel = await client.fetch_channel(969795532736323665)
    await reportchannel.send(f"<{message}> has been reported")



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

@client.slash_command()
async def donations(self,ctx):
    em = discord.Embed(title = 'Donation', description = 'Donate to the bot to help keep it running!', color = 0x8BE002)
    em.add_field(name = ':BTC :', value = '**3Fi97A4fLw8Yycv7F3DwSfMgBJ3zjB1AFL**')
    em.add_field(name = ':ETH :', value = '**0x7Cfa740738ab601DCa9740024ED8DB585E2ed7478**')
    em.add_field(name = ':Doge :', value = '**DQVkWKqGoTGUY9MeN3HiUt49JfcC9aE7fp**')
    em.add_field(name = ':MPL  :', value = '**0xbDBb6403CA6D1681F0ef7A2603aD65a9F09AF138**')
    em.add_field(name = ':XMR  :', value = '**43rsynRD1qtCA1po9myFsc7ti5havFcXUZPdSZuMexU4DnEyno55TE16eWqFkMLMbwZ7DuRW4ow5kcWzQQYu96NH7XMk6cE**')
    em.add_field(name="Buy me a coffee", value="[Click here](https://www.buymeacoffee.com/Michaelrbparker)")
    
    
    await ctx.respond(embed = em)
 
    
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