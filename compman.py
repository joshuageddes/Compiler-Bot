import discord
from discord.ext import commands
from compile import runCode

client = commands.Bot(command_prefix=".")
language = "python"

@client.event
async def on_ready():
    print("bot is ready")
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="for ."))


@client.command(aliases=["S"])
async def s(ctx):
    await ctx.send("You ever just sploch on a homie")



@client.command()
async def language(ctx):
    global langauge
    languages = ["python", "java"]

    code = ctx.message.content.split()

    if len(code) == 1:
        await ctx.send(f"Current language is ```{langauge}```")

    
    
    else :
        code[1] = code[1].lower()
        if code[1] == "list":
            out = "Supported languages include :"
            for lan in languages :
                out += f"\n```{lan}```"
            
            
        elif code[1] in languages:

            langauge = code[1]
            out = f"Language set to ```{code[1]}```"

        else :
            out = f"Langauge '{code[1]}' does not exist.\nUse ```.language list``` for a list of supported langauges"

    

    await ctx.send(out)

@client.command()
async def compile(ctx):
    global langauge
    code = ctx.message.content
    

    #splitting the string into a list for each line
    lines = code.split('\n')
    

    parsedLines = []

    #want to exclude the .compile and the ```
    #might be a simpler way to do this
    for i in range(2, len(lines) - 1):
        parsedLines.append(lines[i])

    
    print(language)
    if language == 'python':
        f = open("compile.txt", "w")# w allows for overwriting the text file each time
        f.write('\n'.join(parsedLines)) # joins the parsed list of lines with a new line at the end of each and writes that to the text file

        
        f.close()

        code_output = runCode('python','compile.txt')
        await ctx.send(f'```\n{code_output}\n```')
    elif language == 'javascript':
        f = open('compile.txt', 'w')
        f.write('\n'.join(parsedLines))
        f.close()

        code_output = runCode('javascript', 'compile.txt')
        await ctx.send(f'```\n{code_output}\n```')
    





#IMPORTANT: add client run with token
#client.run("ODU4MjA3OTIyMzY2NDQ3NjQ2.YNayaQ.2f9QvJJ75S3eRtii5Gl0kIX07Pk")
