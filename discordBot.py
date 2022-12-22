import discord
from discord.ext import commands, tasks
from discord.flags import Intents

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "/", intents = intents)

@bot.event
async def on_ready():
    print(f'acordei!\nconectado como: {bot.user}')
    remenber.start()	

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)

@bot.command(name = 'oi') 
async def say_hi(ctx):
    
    username = ctx.author.name
    await ctx.send(f'olá {username}!')

# ainda não tenho o porque usar algo assim, mas tá aqui no caso algum dia precisar
@tasks.loop(seconds = 20) 
async def remenber():
    channel = bot.get_channel(951921333128790039)
    
    await channel.send('eu ainda estou aqui!')


bot.run('MTA1NTQ3ODk5NjM1NzM2MTcyNg.Gd0VNq.tXYG9m-nn8eSqyvt4CL4KyHRoCgHc5Kpt_4GQE')
