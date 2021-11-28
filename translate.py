import discord

from discord.ext import commands

import googletrans
from googletrans import Translator


# command_prefix can be set to anything you want
bot = commands.Bot(command_prefix="!")


@bot.event
async def on_ready():
    print("Bot is ready")


@bot.command()
async def translate(ctx, lang, *, args):
    t = Translator()
    a = t.translate(args, dest=lang)
    await ctx.send(a.text)

# the string inside is the token from the bot
bot.run("token")
