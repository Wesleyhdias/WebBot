import utils
import discord
from discord.ext import commands, tasks
from discord.flags import Intents

intents = discord.Intents.all()
bot = commands.Bot(command_prefix = "?", intents = intents)

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
        notas = utils.get_grades(site, login, password, toStr=True)
        if notas == False:
            await ctx.author.send('não encontrei nenhuma nota')
            await ctx.author.send('mas não se preocupe, os professores podem simplesmente não ter postado ainda, pesquise outra vez mais tarte, ou fale diretamente com algum professor')
        else:
            embed = discord.Embed(
                title = "Tabela de notas",
                description= "Podem haver erros ou mudanças nas notas",
                color = 0x0000FF)
            # precisa ficar um pouco mais apresentavel
            embed.add_field(name = 'Matérias', value = f'{notas[0]}')
            embed.add_field(name = 'Prova B1', value = notas[1])
            embed.add_field(name = 'Trabalho B1', value = notas[2])
            embed.add_field(name = 'Substitutiva B1', value = notas[3])
            embed.add_field(name = 'Prova B2', value = notas[4])
            embed.add_field(name = 'Trabalho B2', value = notas[5])
            embed.add_field(name = 'Substitutiva B2', value = notas[6])
            
            await ctx.author.send(f'aqui estão suas notas até o momento:\n\n')
            await ctx.send(embed=embed)
                           
    except discord.errors.Forbidden:
        if notas == False:
            await ctx.send('não encontrei nenhuma nota')
            await ctx.author.send('mas não se preocupe, os professores podem simplesmente não ter postado ainda, pesquise outra vez mais tarte, ou fale diretamente com algum professor')
        else:
            await ctx.send('Não posso enviar menssagens no seu privrado!\ncaso queira receber habilite a opção para receber mensagens de qualquer pessoa.')
    

# ainda não tenho o porque usar algo assim, mas tá aqui no caso de algum dia precisar
@tasks.loop(seconds = 5) 
async def remenber():
    channel = bot.get_channel(1055487703472406538)
    
    await channel.send('eu ainda estou aqui!')

bot.run('Token')
