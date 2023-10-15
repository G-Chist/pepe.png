# -*- coding: utf-8 -*-
import telebot
import config
from random import randint
from PIL import Image, ImageDraw, ImageEnhance, ImageFont

bot = telebot.TeleBot(config.token)

memecounter = 0

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

@bot.message_handler(content_types=['photo', 'text'])
def thebot(message):

    if message.text == "|help":
        bot.send_message(message.chat.id, "|bw + image - black and white image\n|deepfry + image - deep fried image\n|meme toptext | bottomtext + image - a meme\n chat id: " + str(message.chat.id))

    else:

        try:
            fileID = message.photo[-1].file_id
            file_info = bot.get_file(fileID)
            downloaded_file = bot.download_file(file_info.file_path)
            global memecounter
            memecounter = memecounter + 1 if memecounter < 7 else 0
            with open(str(memecounter) + ".png", 'wb') as new_file:
                new_file.write(downloaded_file)

            if message.caption == "|send":
                bot.send_photo(message.chat.id, photo=open(str(memecounter) + ".png", 'rb'))

            if message.caption == "|bw":
                image = Image.open(str(memecounter) + '.png')
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
                image.save(str(memecounter) + '.png')
                bot.send_photo(message.chat.id, photo=open(str(memecounter) + ".png", 'rb'))

            if message.caption == "|deepfry":
                image = Image.open(str(memecounter) + '.png')
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
                image.save(str(memecounter) + '.png')
                bot.send_photo(message.chat.id, photo=open(str(memecounter) + ".png", 'rb'))
            else:
                pass

            if message.caption[:5:] == "|meme":
                if len(message.caption[6::]) > 0:
                    if search(message.caption, "|") >= 2:
                        toptext = str(message.caption[6:message.caption[6::].find("|") + 5:]).upper()
                        bottomtext = str(message.caption[9 + len(toptext)::]).upper()
                    else:
                        toptext = str(message.caption[6::]).upper()
                        bottomtext = ""
                else:
                    toptext = " "
                    bottomtext = " "
                image = Image.open(str(memecounter) + '.png')
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
                image.save(str(memecounter) + '.png')
                bot.send_photo(message.chat.id, photo=open(str(memecounter) + ".png", 'rb'))

            if message.caption[:8:] == "|obamize":
                image = Image.open(str(memecounter) + '.png')
                width = image.size[0]
                height = image.size[1]
                sizenew = (round(round(width * (750 / height)) / 50) * 50, 750)
                image = image.resize(sizenew)
                draw = ImageDraw.Draw(image)
                image.save(str(memecounter) + '.png')
                width = image.size[0]
                imgsmall = image.resize((int(width /  50), 15))
                image = imgsmall.resize(sizenew)
                image.save(str(memecounter) + '.png')
                for i in range(int(width / 50)):
                    for j in range(15):
                        image.paste(Image.open('obama' + str(memecounter) + '.png'), (i * 50, j * 50))
                image.save('obamium' + str(memecounter) + '.png')
                image = Image.open(str(memecounter) + '.png')
                image1 = Image.open('obamium' + str(memecounter) + '.png')
                w, h = image.size
                for x in range(w):
                    for y in range(h):
                        pix_coord = (x, y)
                        r, g, b = image.getpixel(pix_coord)
                        r1, g1, b1 = image1.getpixel(pix_coord)
                        new_col = (int(0.74 * r + 0.25 * r1), int(0.75 * g + 0.25 * g1), int(0.75 * b + 0.25 * b1))
                        image.putpixel(pix_coord, new_col)
                image.save('obamium' + str(memecounter) + '.png')
                bot.send_photo(message.chat.id, photo = open('obamium' + str(memecounter) + ".png", 'rb'))

        except Exception as e:
            #with open("/home/pepepng/error-log.txt", "a") as file1:
                #file1.write(str(e) + "\n")
            pass

if __name__ == '__main__':
    try:
       bot.polling(none_stop=True)
    except Exception as e:
        with open("/home/pepepng/error-log.txt", "a") as file1:
            file1.write(str(e) + "\n")
