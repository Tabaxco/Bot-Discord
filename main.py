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
        host='',
        port='',
        dbname='',
        user='',
        password='',
        
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
    
    operacao_str = f' {operacao} {bonus}' if operacao in ('+', '-') else ''

    await ctx.send(f'**`{total}`** ⟵ {resultados} {quantidade}d{lados}{operacao_str}')


bot.run(TOKEN)