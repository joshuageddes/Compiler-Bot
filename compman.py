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
async def compile(ctx, args):
    options = webdriver.ChromeOptions()
    options.add_argument("--incognito")
    browser = webdriver.Chrome(options=options)
    browser.set_window_size(1920, 1080)
    browser.maximize_window()

    browser.get("https://www.w3schools.com/python/trypython.asp?filename=demo_compiler")



client.run("ODU4MjA3OTIyMzY2NDQ3NjQ2.YNayaQ.qfD63_lhPtWrj-XfNPZBsPRlgYA")
