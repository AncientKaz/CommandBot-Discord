from http.client import FORBIDDEN
import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#Discord Intents Import
intents = discord.Intents.default()
intents.members = True  # Members Info
intents.reactions = True
intents.messages = True  # Utilize commands
client = discord.Client(intent=intents)

# --! Role on Join !--#
AUTO_JOIN_ROLE = "Server Member"

# --! Initialize Bot !--#
yoruko = commands.Bot(command_prefix='*', intents=intents)


@yoruko.event
async def log_in():
    print(f'{client.user.name}, ID: {client.user.id} has logged in.')
    print(f'Bot is listening for events.')


@yoruko.event
async def new_member(member):
    print(f'New Member: {member.name} (ID: {member.id})')
    try:
        join_role = discord.utils.get(member.guild.roles, name=AUTO_JOIN_ROLE)
        await member.add_roles(join_role)
        # if join_role:
        #   await member.add_roles(join_role)
        #  print(f'Role given: {AUTO_JOIN_ROLE} to {member.name}')
        # else:
        #  print(f'Role {AUTO_JOIN_ROLE} could not be assigned.')
    except discord.Forbidden:
        print("Cannot add role")
    except Exception as e:
        print(f'unidentified error. check logs: {e}')


# --! Gets bot to run !--#
yoruko.run(TOKEN)
