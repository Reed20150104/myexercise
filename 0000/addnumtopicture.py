#!/usr/bin/env python
# -*- coding:utf-8 -*-

import PIL
from PIL import Image,ImageDraw,ImageFont


'''
将QQ或者微信头像加上信息数
'''

def addNumberToPic(img):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('/usr/share/fonts/truetype/Sarai/Sarai.ttf', size = 40)
    fillcolor = "#ff0000"
    width, height = img.size
    draw.text((width - 50, 0), '99', font=myfont, fill=fillcolor)
    img.save('result.jpg','jpeg')

if __name__ == '__main__':
    image = Image.open(r'/home/reed/Pictures/photo.jpg')
    image.show()
    addNumberToPic(image)
