#!/usr/bin/env python
# -*- coding:utf-8 -*-

import PIL
from PIL import Image,ImageDraw,ImageFont
import os


'''
将QQ或者微信头像加上信息数
'''

def addNumberToPic(img, x, y):
    draw = ImageDraw.Draw(img)
    myfont = ImageFont.truetype('simsun.ttc', size = 40)
    fillcolor = "#ff0000"
    draw.text((x, y), '99', font=myfont, fill=fillcolor)
    img.save('result.jpg','jpeg')

def main():
    image = Image.open(r'./../images/eatwatermelon.jpg')
    image_width, image_height = image.size
    addNumberToPic(image, image_width - 50, 0)
    if (os.path.exists("result.jpg")):
        image1 = Image.open(r'./result.jpg')
        image1.show()


if __name__ == '__main__':
    main()
