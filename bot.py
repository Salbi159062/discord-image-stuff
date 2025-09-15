import discord
from discord.ext import commands
from model import idk

#activate intents 
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='/', intents=intents)


#create first bot.event
@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
#commands
@bot.command()
async def hello(ctx):
    await ctx.send(f'Hi! I am a bot {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)


@bot.command()
async def check(ctx):
    
    if ctx.message.attachments:  # - This checks if a reply with the command is a document
        for file in ctx.message.attachments:
            print(type(file))   # prints the file name on the blackboard
            
            await file.save(f"./images/{file.filename}") #Saves the image into the folder
            await ctx.send(f"Saved {file.filename}")
            await ctx.send(idk(img=f"./images/{file.filename}"))  #Sends the class the document belongs to

    else:
        await ctx.send("Please enter an image")

    await ctx.send()

bot.run("TOKEN HERE!")
