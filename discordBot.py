import utils
import discord
from decouple import config
from discord.ext import commands, tasks

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix = "?", intents = intents)
escola = 'https://feitep.jacad.com.br/academico/aluno-v2/login'

@bot.event
async def on_ready():
    print(f'acordei!\nconectado como: {bot.user}')
    # remenber.start()	

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    await bot.process_commands(message)


# comando para ver as notas
@bot.command(name = 'notas', help='envia para o seu privado uma tabela com suas notas atualizadas direto do site de sua escola ou faculdade, os argumentos desse comando devem estar em ordem e separados por um espaço') 
async def get_grade(ctx, login, password):
    try:
        if str(ctx.channel) != "Direct Message with Unknown User":
            await ctx.message.delete()
        notas = utils.get_grades(escola, login, password, toStr=False)
        utils.drawText(notas)
        
        # cria embed para enviar
        embed = discord.Embed(
            title = "Tabela de notas",
            description= "Podem haver erros ou mudanças nas notas",
            color = 0x0000FF)
        file = discord.File('notas.png', filename = 'image.png')
        embed.set_image(url='attachment://image.png')
        
        await ctx.author.send(f'aqui estão suas notas até o momento:\n\n')
        await ctx.author.send(file=file, embed=embed)
        
    # caso não tenha permição para mensagens diretas
    except discord.errors.Forbidden:
        await ctx.send('Não posso enviar menssagens no seu privrado!\ncaso queira receber habilite a opção para receber mensagens de qualquer pessoa.')
    # para erro desconhecido
    except Exception as erro:
        print(f"erro novo\n\n{erro}\n\n")

# verificar atualizações no site(falta fazer)
@tasks.loop(seconds = 5) 
async def remenber():
    channel = bot.get_channel(1055487703472406538)
    
    await channel.send('verificando')


TOKEN = config('TOKEN')
bot.run(TOKEN)
