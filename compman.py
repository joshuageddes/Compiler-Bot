import discord
from discord.ext import commands

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait



client = commands.Bot(command_prefix=".")

@client.event
async def on_ready():
    print("bot is ready")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for ."))


@client.command(aliases=["S"])
async def s(ctx):
    await ctx.send("You ever just sploch on a homie")


@client.command()
async def compile(ctx):
    code = ctx.message.content
    print(type(code))
    print(code)



