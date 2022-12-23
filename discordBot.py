import utils
import discord
from discord.ext import commands, tasks
from discord.flags import Intents

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "/", intents = intents)

@bot.event
async def on_ready():
    print(f'acordei!\nconectado como: {bot.user}')
    # remenber.start()	

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    await bot.process_commands(message)
    
    
@bot.command(name = 'notas') 
async def get_grade(ctx, site, login, password):
    
    # ainda tem coisas para arrumar aqui, muitas coisas
    try:
        msg = utils.get_grades(site, login, password)
        if msg == 'nenhum elemento encontrado':
            await ctx.author.send('não encontrei nenhuma nota')
        else:
            await ctx.author.send(f'aqui estão suas notas até o momento:\n\n')
            for k in msg:
                await ctx.author.send(f'{msg[k]}')
    except discord.errors.Forbidden:
        if msg == 'nenhum elemento encontrado':
            ctx.send('não encontrei nenhuma nota')
        else:
            await ctx.send('Não posso enviar menssagens no seu privrado!\ncaso queira receber habilite a opção para receber mensagens de qualquer pessoa.')
    

# ainda não tenho o porque usar algo assim, mas tá aqui no caso de algum dia precisar
@tasks.loop(seconds = 20) 
async def remenber():
    channel = bot.get_channel(951921333128790039)
    
    await channel.send('eu ainda estou aqui!')


bot.run('TOKEN')
