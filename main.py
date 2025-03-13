import discord
from discord.ext import commands
import psycopg2
from random import randint
from dotenv import load_dotenv
import os

load_dotenv()

TOKEN = os.getenv("TOKEN")

try:
    conexao = psycopg2.connect(
        host='localhost',
        port=5432,
        dbname='postgres',
        user='postgres',
        password='macaco',
        
    )
    
    print("Conexão estabelecida com sucesso!")

except Exception as e:
    print("Erro ao conectar ao banco de dados:", e)



def check(msg, ctx):
    return msg.author == ctx.author and msg.channel == ctx.channel

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix = '$', intents = intents)


@bot.event
async def on_ready():
    print(f"{bot.user.name} está online!")


@bot.command()
async def roll(ctx, quantidade: int = 1, lados: int = 20, operacao: str = None, bonus: int = 0):
    resultados = []

    for n in range(quantidade):
        rolamentos = randint(1, lados)
        resultados.append(rolamentos)

    total = sum(resultados)

    if operacao == '+':
        total += bonus
    elif operacao == '-':
        total -= bonus
    elif operacao in '*':
        total *= bonus
    elif operacao in '/':
        total /= bonus
    
    operacao_str = f' {operacao} {bonus}' if operacao in ('+', '-') else ''

    await ctx.send(f'**` {total} `** ⟵ {resultados} {quantidade}d{lados}{operacao_str}')


@bot.command()
async def status(ctx):
    dumbell = '<:dumbell:1349403661729796216>'
    usuario = ctx.author

    embed = discord.Embed(
        title = 'ㅤㅤㅤㅤㅤㅤㅤㅤ⌈ STATUS ⌋ㅤㅤㅤㅤㅤㅤㅤㅤ',
        description = '',
        colour=discord.Colour.from_str("#483D8B")   
    )
    embed.set_author(name = '')

    embed.add_field (name = 'INFORMAÇÕES', value = '', inline = False)
    embed.add_field (name = 'Rank Ninja:', value = 'Gennin', inline = True)
    embed.add_field (name = 'Especialização:', value = 'Restringido', inline = True)
    embed.add_field (name = 'Título:', value = 'Random', inline = True)

    embed.add_field (name = '', value = '', inline = False)
    embed.add_field(name = '', value = '', inline = False)

    embed.add_field(name = 'CARACTERÍSTICAS', value = '', inline = False)
    embed.add_field(name = '', value = '**Hit Points:** 23', inline = True)
    embed.add_field(name = '', value = '**Chakra Points:** 4', inline = True)
    embed.add_field(name = '', value = '**Level:** 10', inline = True)

    embed.add_field(name = '', value = '', inline = False)
    embed.add_field(name = '', value = '', inline = False)

    embed.add_field(name = 'ATRIBUTOS', value = '', inline = False)
    embed.add_field(name = '', value = f'{dumbell} **FOR:** 0',inline=True)
    embed.add_field(name = '', value = ':athletic_shoe: **DEX:** 0', inline=True)
    embed.add_field(name = '', value = ':shield: **CON:** 0', inline=True)
    embed.add_field(name = '', value = '', inline = False)
    embed.add_field(name = '', value = ':brain: **INT:** 0', inline = True )
    embed.add_field(name = '', value = ':eye: **SAB:** 0', inline = True)
    embed.add_field(name = '', value = ':speaking_head: **CAR:** 0', inline = True)

    embed.set_footer(text=f'Pontos Restantes: 12 \nStatus de {usuario}')
    await ctx.send(embed = embed)

bot.run(TOKEN)