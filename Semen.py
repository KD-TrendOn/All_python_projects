import discord
import time
from discord.ext import commands
bot = commands.Bot(command_prefix='=')
TOKEN = "ODg5NTY4MDczMDAxMDc0NzMw.YUjI0w.0I1s63VNP0Q1b9SBf_H_9WvVBeg"


@bot.command(pass_context=True)
async def sanya(ctx):
    await ctx.send('@Ahtungツ#3161 ахахахах ты ботяра')
bot.run(TOKEN)