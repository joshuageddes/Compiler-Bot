import discord
from discord.ext import commands
from compile import runCode

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
    

    #splitting the string into a list for each line
    lines = code.split('\n')
    

    parsedLines = []

    #want to exclude the .compile and the ```
    #might be a simpler way to do this
    for i in range(2, len(lines) - 1):
        parsedLines.append(lines[i])

    #parses the lines for the language --> probably an easier way to send parameters from the discord bot
    language = lines[0].split(' ')[1]
    print(language)
    if language == 'python':
        f = open("compile.txt", "w")# w allows for overwriting the text file each time
        f.write('\n'.join(parsedLines)) # joins the parsed list of lines with a new line at the end of each and writes that to the text file

        
        f.close()

        code_output = runCode('python','compile.txt')
        await ctx.send(f'```\n{code_output}\n```')
    elif language == 'javascript':
        f = open('test.js', 'w')
        f.write('\n'.join(parsedLines))
        f.close()

        code_output = runCode('javascript', 'test.js')
        await ctx.send(f'```\n{code_output}\n```')
    




#IMPORTANT: add client run with token
#client.run("ODU4MjA3OTIyMzY2NDQ3NjQ2.YNayaQ.2f9QvJJ75S3eRtii5Gl0kIX07Pk")