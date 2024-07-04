import discord
from discord.ext import commands
from TOKEN import TOKEN
from WORD import keyword_responses

intents = discord.Intents.default()
intents.messages = True  

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot conectado como {bot.user}')

@bot.event
async def on_message(message):
    if message.author == bot.user:  
        return
    
    for keyword, response in keyword_responses.items():
        if keyword in message.content.lower():
            await message.channel.send(response)
            return
    
    await bot.process_commands(message)  

bot.run(TOKEN)
