import discord
from discord.ext import commands

from owoify import owoify
import requests
import datetime

import os

token = os.environ["OWO_TOKEN"]

bot = commands.Bot(command_prefix="$")

@bot.command(name="bones")
async def bones(ctx):
    date = datetime.datetime.now()
    bones_day_result = requests.get(f"https://bones-backend.herokuapp.com/bones/{date.month}-{date.day}-{date.year}")
    bones_day_json = bones_day_result.json()
    if "message" in bones_day_json:
        await ctx.send(f"It might be a bones day!")
    else:
        if bones_day_json["value"] == "b":
            await ctx.send(f"It's a bones day! :bone:")
        else:
            await ctx.send(f"It's not a bones day! :sob:")

@bot.command(name="owoify")
async def command_owoify(ctx, *args):
    mess = ctx.message
    ref = mess.reference
    if ref:
        replied_message = None
        if ref.cached_message:
            replied_message = ref.cached_message
        else:
            replied_message = await ctx.fetch_message(ref.message_id)
        print(replied_message.content)
        await ctx.send(owoify(replied_message.content))
    else:
        await ctx.send(owoify(" ".join(args)))


@bot.command(name="uwuify")
async def command_uwuify(ctx, *args):
    mess = ctx.message
    ref = mess.reference
    if ref:
        replied_message = None
        if ref.cached_message:
            replied_message = ref.cached_message
        else:
            replied_message = await ctx.fetch_message(ref.message_id)
        print(replied_message.content)
        await ctx.send(owoify(replied_message.content, "uwu"))
    else:
        await ctx.send(owoify(" ".join(args), "uwu"))


@bot.command(name="uvuify")
async def command_uvuify(ctx, *args):
    mess = ctx.message
    ref = mess.reference
    if ref:
        replied_message = None
        if ref.cached_message:
            replied_message = ref.cached_message
        else:
            replied_message = await ctx.fetch_message(ref.message_id)
        print(replied_message.content)
        await ctx.send(owoify(replied_message.content, "uvu"))
    else:
        await ctx.send(owoify(" ".join(args), "uvu"))


bot.run(token)
