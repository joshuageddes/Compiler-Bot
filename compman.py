import discord
from discord.ext import commands
from compile import runCode


client = commands.Bot(command_prefix=".")


@client.event
async def on_ready():
    print("bot is ready")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for ."))


global currentLanguage
currentLanguage = 'python'


@client.command()
async def language(ctx):
    global currentLanguage
    languages = ["python", "javascript"]

    code = ctx.message.content.split()

    if len(code) == 1:
        out = discord.Embed(title=f"Current language:", color=0x00b3ff)
        out.add_field(
            name="---", value=f"```{currentLanguage}```", inline=False)

    else:
        code[1] = code[1].lower()
        if code[1] == "list":
            out = discord.Embed(
                title=f"Supported languages include:", color=0x00b3ff)
            out.add_field(name="---", value="Python, Javascript", inline=False)

        elif code[1] in languages:

            currentLanguage = code[1]
            out = discord.Embed(title=f"Language set to: ", color=0x00b3ff)
            out.add_field(name="---", value=f"```{code[1]}```", inline=False)

        else:
            out = discord.Embed(title=f"Language not Found: ", color=0x00b3ff)
            out.add_field(
                name="---", value=f"language '{code[1]}' does not exist.\nUse ```.language list``` for a list of supported languages", inline=False)


    await ctx.send(embed=out)


@client.command()
async def compile(ctx):
    global currentLanguage
    code = ctx.message.content

    # splitting the string into a list for each line
    lines = code.split('\n')

    parsedLines = []

    # want to exclude the .compile and the ```
    # might be a simpler way to do this
    for i in range(2, len(lines) - 1):
        parsedLines.append(lines[i])

    # parses the lines for the language --> probably an easier way to send parameters from the discord bot
    # language = lines[0].split(' ')[1]
    if currentLanguage == 'python':
        # w allows for overwriting the text file each time
        f = open("compile.txt", "w")
        # joins the parsed list of lines with a new line at the end of each and writes that to the text file
        f.write('\n'.join(parsedLines))

        f.close()

        code_output = runCode('python', 'compile.txt')

        embed = discord.Embed(title="Code Output", color=0x00b3ff)
        embed.add_field(
            name="---", value=f"```\n{code_output}\n```", inline=False)
        await ctx.send(embed=embed)

    elif currentLanguage == 'javascript':
        f = open('compile.txt', 'w')
        f.write('\n'.join(parsedLines))
        f.close()

        code_output = runCode('javascript', 'compile.txt')
        embed = discord.Embed(title="Code Output", color=0x00b3ff)
        embed.add_field(
            name="---", value=f"```\n{code_output}\n```", inline=False)
        await ctx.send(embed=embed)


# IMPORTANT: add client run with token
client.run("ODU4MjA3OTIyMzY2NDQ3NjQ2.YNayaQ.akV8i2h2-4gT4Xhhettf4B2X0qs")
