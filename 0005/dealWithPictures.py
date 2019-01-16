#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# import lib
import os
from PIL import Image


'''
Project: myexercise
File: dealWithPictures.py
Comment: This python file is used to deal with picture size.
Author: Reed   https://www.cnblogs.com/dangzhengtao/p/9620272.html  https://www.jb51.net/article/138966.htm
Date: 2019/1/9 23:20

'''


def changePictureSize(filePath,width,height,distPath):
    for root, dirs, files in os.walk(filePath):
        for file in files:
            image = Image.open(os.path.join(filePath, file))
            image_width = image.width
            image_height = image.height

            if image_width <= width and image_height <= height:
                print(file, " is OK")
                return
            if 1.0 * image_width / width > 1.0 * image_height / height:
                scale = 1.0 * image_width / width
                new_image = image.resize((int(image_width / scale), int(image_height / scale)))
            else:
                scale = 1.0 * image_height / height
                new_image = image.resize((int)(image_width / scale), int(image_height / scale), Image.ANTIALIAS)

            if not os.path.exists(distPath):
                os.makedirs(distPath)

            new_image.save(os.path.join(distPath, 'new--' + file))
            new_image.close()
            image.close()




def main():
    FILEPATH='E:\\BaiduDownloads\\191_1222'  #图片文件路径
    DIST_PATH = 'E:\\pictureResult'  #存放图片路径
    ext = ['jpg','png','jpeg']   #需要处理的图片文件类型
    PHONE_WIDTH = 640
    PHONE_HEIGHT = 1136
    changePictureSize(FILEPATH, 640, 1136, DIST_PATH)


if __name__ == '__main__':
    main()
