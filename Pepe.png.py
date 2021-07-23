import discord
from discord.utils import get, find
from discord.ext import commands
import datetime
from PIL import Image, ImageDraw, ImageEnhance, ImageFont
from bs4 import BeautifulSoup
import requests
from random import *

settings = {
    'token': 'token',
    'bot': 'Pepe.png',
    'id': 0000000,
    'prefix': '|'
}
client = discord.Client()
client.intents = all
bot = commands.Bot(command_prefix = settings['prefix'])
bot.remove_command('help')

def rangevar(var, low, high):
    if var < low:
        var = low
    if var > high:
        var = high
    return var

def search(str, symb):
    a = 0
    for i in str:
        if i == symb:
            a += 1
    return a

#BOT COMMAND FUNCTIONS

def saverandom():
    response = requests.get('http://lorempixel.com/' + str(randint(100, 1500)) + '/' + str(randint(100, 1500)) + '/')
    with open('cum.png', 'wb') as f:
        f.write(response.content)

async def saveimg(ctx):
    image = ctx.message.attachments[0]
    await image.save('cum.png')

def bwf():
    image = Image.open('cum.png')
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    for x in range(width):
        for y in range(height):
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            sr = (r + g + b) // 3
            draw.point((x, y), (sr, sr, sr))
    image.save('cum.png')

def invertf():
    image = Image.open('cum.png')
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    for x in range(width):
        for y in range(height):
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            draw.point((x, y), (255 - r, 255 - g, 255 - b))
    image.save('cum.png')

def brightf():
    image = Image.open('cum.png')
    enhancer = ImageEnhance.Brightness(image)
    im_output = enhancer.enhance(1.4)
    im_output.save('cum.png')

def darkf():
    image = Image.open('cum.png')
    enhancer = ImageEnhance.Brightness(image)
    im_output = enhancer.enhance(0.6)
    im_output.save('cum.png')

async def noisef(ctx):
    if len(ctx.message.content[7::]) > 0:
        n = float(ctx.message.content[7::])
    else:
        n = 50
    image = Image.open('cum.png')
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    for x in range(width):
        for y in range(height):
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            draw.point((x, y), (rangevar(r + randint(-n, n), 0, 255), rangevar(g + randint(-n, n), 0, 255), rangevar(b + randint(-n, n), 0, 255)))
    image.save('cum.png')

async def contrastf(ctx):
    if len(ctx.message.content[10::]) > 0:
        n = float(ctx.message.content[10::])
    else:
        n = 1.5
    image = Image.open('cum.png')
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(n)
    image.save('cum.png')

def deepfryf():
    image = Image.open('cum.png')
    enhancer = ImageEnhance.Contrast(image)
    image = enhancer.enhance(1.8)
    draw = ImageDraw.Draw(image)
    width = image.size[0]
    height = image.size[1]
    pix = image.load()
    for x in range(width):
        for y in range(height):
            r = pix[x, y][0]
            g = pix[x, y][1]
            b = pix[x, y][2]
            draw.point((x, y), (rangevar(r + randint(-100, 100), 0, 255), rangevar(g + randint(-100, 100), 0, 255), rangevar(b + randint(-100, 100), 0, 255)))
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(1.4)
    image.save('cum.png')

async def memef(ctx):
    if len(ctx.message.content[6::]) > 0:
        if search(ctx.message.content, "|") >= 2:
            toptext = str(ctx.message.content[6:ctx.message.content[6::].find("|") + 5:]).upper()
            bottomtext = str(ctx.message.content[9 + len(toptext)::]).upper()
        else:
            toptext = str(ctx.message.content[6::]).upper()
            bottomtext = ""
    else:
        toptext = " "
        bottomtext = " "
    image = Image.open('cum.png')
    largertext = len(toptext) if len(toptext) > len(bottomtext) else len (bottomtext)
    width, height = image.size
    font = ImageFont.truetype("impact.ttf", size = int(round(110 * (width / 1100) * (20 / largertext if largertext > 18 else 1), 0)))
    draw = ImageDraw.Draw(image)
    w1, h1 = draw.textsize(toptext,  font = font)
    w2, h2 = draw.textsize(bottomtext, font = font)
    x1 = (width - w1) / 2
    y1 = round(height / 120, 0)
    x2 = (width - w2) / 2
    y2 = height - h2 - 4 * round(height / 120, 0)
    draw.text((x1 - 1, y1 - 1), str(toptext), font = font, fill = "black")
    draw.text((x1 + 1, y1 - 1), str(toptext), font = font, fill = "black")
    draw.text((x1 - 1, y1 + 1), str(toptext), font = font, fill = "black")
    draw.text((x1 + 1, y1 + 1), str(toptext), font = font, fill = "black")
    draw.text((x1, y1), str(toptext), font = font)
    draw.text((x2 - 1, y2 - 1), str(bottomtext), font = font, fill = "black")
    draw.text((x2 + 1, y2 - 1), str(bottomtext), font = font, fill = "black")
    draw.text((x2 - 1, y2 + 1), str(bottomtext), font = font, fill = "black")
    draw.text((x2 + 1, y2 + 1), str(bottomtext), font = font, fill = "black")
    draw.text((x2, y2), str(bottomtext), font = font)
    image.save('cum.png')

async def dfmemef(ctx):
    if len(ctx.message.content[8::]) > 0:
        if search(ctx.message.content, "|") >= 2:
            toptext = str(ctx.message.content[8:ctx.message.content[8::].find("|") + 7:]).upper()
            bottomtext = str(ctx.message.content[11 + len(toptext)::]).upper()
        else:
            toptext = str(ctx.message.content[8::]).upper()
            bottomtext = ""
    else:
        toptext = " "
        bottomtext = " "
    image = Image.open('cum.png')
    largertext = len(toptext) if len(toptext) > len(bottomtext) else len(bottomtext)
    width, height = image.size
    font = ImageFont.truetype("impact.ttf", size = int(round(110 * (width / 1100) * (20 / largertext if largertext > 18 else 1), 0)))
    draw = ImageDraw.Draw(image)
    w1, h1 = draw.textsize(toptext, font = font)
    w2, h2 = draw.textsize(bottomtext, font = font)
    x1 = (width - w1)/2
    y1 = round(height/120, 0)
    x2 = (width - w2)/2
    y2 = height - h2 - 4 * round(height/120, 0)
    draw.text((x1 - 1, y1 - 1), str(toptext), font = font, fill = "black")
    draw.text((x1 + 1, y1 - 1), str(toptext), font = font, fill = "black")
    draw.text((x1 - 1, y1 + 1), str(toptext), font = font, fill = "black")
    draw.text((x1 + 1, y1 + 1), str(toptext), font = font, fill = "black")
    draw.text((x1, y1), str(toptext), font = font)
    draw.text((x2 - 1, y2 - 1), str(bottomtext), font = font, fill = "black")
    draw.text((x2 + 1, y2 - 1), str(bottomtext), font = font, fill = "black")
    draw.text((x2 - 1, y2 + 1), str(bottomtext), font = font, fill = "black")
    draw.text((x2 + 1, y2 + 1), str(bottomtext), font = font, fill = "black")
    draw.text((x2, y2), str(bottomtext), font = font)
    image.save('cum.png')
    deepfryf()

async def lobsterf(ctx):
    if len(ctx.message.content[8::]) > 0:
        bottomtext = str(ctx.message.content[8::])
    else:
        bottomtext = " "
    image = Image.open('cum.png')
    width, height = image.size
    font = ImageFont.truetype("lobster.ttf", size = int(round(100 * (width / 1100), 0)))
    draw = ImageDraw.Draw(image)
    w2, h2 = draw.textsize(bottomtext, font = font)
    x2 = (width - w2)/2
    y2 = height - font.size - 4 * round(height/120, 0)
    draw.text((x2, y2), str(bottomtext), font = font)
    image.save('cum.png')

async def sendimg(ctx):
    await ctx.send(file = discord.File('cum.png'))

#BOT COMMANDS

@bot.command()
async def hello(ctx):

    try:
        member = ctx.message.author
        await ctx.send(f'Hello, {member.mention}!')

    except:
        await ctx.send("**Unexpected bot error.**")

@bot.command()
async def bw(ctx):

    try:
        await saveimg(ctx)
        bwf()
        await sendimg(ctx)

    except:
        await ctx.send("**Unexpected bot error.**")

@bot.command()
async def invert(ctx):

    try:
        await saveimg(ctx)
        invertf()
        await sendimg(ctx)

    except:
        await ctx.send("**Unexpected bot error.**")

@bot.command()
async def bright(ctx):

    try:
        await saveimg(ctx)
        brightf()
        await sendimg(ctx)

    except:
        await ctx.send("**Unexpected bot error.**")

@bot.command()
async def dark(ctx):

    try:
        await saveimg(ctx)
        darkf()
        await sendimg(ctx)

    except:
        await ctx.send("**Unexpected bot error.**")

@bot.command()
async def noise(ctx):

    try:
        await saveimg(ctx)
        await noisef(ctx)
        await sendimg(ctx)

    except:
        await ctx.send("**Unexpected bot error.**")

@bot.command()
async def contrast(ctx):

    try:
        await saveimg(ctx)
        await contrastf(ctx)
        await sendimg(ctx)

    except:
        await ctx.send("**Unexpected bot error.**")

@bot.command()
async def deepfry(ctx):

    try:
        await saveimg(ctx)
        deepfryf()
        await sendimg(ctx)

    except:
        await ctx.send("**Unexpected bot error.**")

@bot.command()
async def meme(ctx):

    try:
        await saveimg(ctx)
        await memef(ctx)
        await sendimg(ctx)

    except:
        await ctx.send("**Unexpected bot error.**")

@bot.command()
async def dfmeme(ctx):

    try:
        await saveimg(ctx)
        await dfmemef(ctx)
        await sendimg(ctx)

    except:
        await ctx.send("**Unexpected bot error.**")

@bot.command()
async def lobster(ctx):

    try:
        await saveimg(ctx)
        await lobsterf(ctx)
        await sendimg(ctx)

    except:
        await ctx.send("**Unexpected bot error.**")

@bot.command()
async def random(ctx):

    try:
        saverandom()
        await ctx.send(file = discord.File('cum.png'))

    except:
        await ctx.send("**Unexpected bot error.**")

@bot.command()
async def help(ctx):

    try:

        author = ctx.message.author

        img = discord.File("Help.png")

        embed = discord.Embed(colour = discord.Colour.orange())
        embed.set_author(name = 'Help')
        embed.add_field(name = "|bw", value = "Black and white image", inline = False)
        embed.add_field(name = "|invert", value = "Inverted color image", inline = False)
        embed.add_field(name = "|bright", value = "Make the image bright", inline = False)
        embed.add_field(name = "|dark", value = "Make the image dark", inline = False)
        embed.add_field(name = "|noise", value = "Distorts the image", inline = False)
        embed.add_field(name = "|contrast", value = "Gives the image more contrast", inline = False)
        embed.add_field(name = "|contrast", value = "Gives the image more contrast", inline = False)
        embed.add_field(name = "|meme TEXT | TEXT2", value = "Makes a meme with an image", inline = False)
        embed.add_field(name = "|dfmeme TEXT | TEXT2", value = "Makes a deep fried meme with an image", inline = False)
        embed.add_field(name = "|lobster TEXT", value = "Makes a lobster meme with an image", inline = False)


        await ctx.send("**Sent you a DM!**")
        await ctx.message.author.send(embed = embed)

    except:
        await ctx.send("**Unexpected bot error.**")

bot.run(settings['token'])
client.run(settings['token'])
