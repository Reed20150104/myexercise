#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# import lib
import os

'''
Project: myexercise
File: statisticalCode.py
Comment: 
Author: Reed https://www.cnblogs.com/hupeng1234/p/6680230.html
Date: 2019/1/16 22:35

'''

def getAllFiles(filePath):
    fileArr = []
    for root,dir,files in os.walk(filePath):
        for file in files:
            fileArr.append(os.path.join(root,file))
    # files = os.listdir(filePath)
    # for file in files:
    #     file_dir = os.path.join(filePath,file)
    #     if os.path.isdir(file_dir):
    #         getAllFiles(file_dir)
    #     else:
    #         fileArr.append(os.path.join(filePath,file_dir))
    #         print(os.path.join(filePath,file_dir))

    return fileArr

def staticalCode(filePath):
    DICTSTATICAL = {}
    FILE_ARRAY = []
    CODE_NUMBER= 0   #代码行数
    COMMENT_NUMBER = 0 #注释行数
    BLANK_NUMBER = 0  #空白行数
    IS_COMMENT = False  #默认非注释行
    FILE_ARRAY = getAllFiles(filePath)
    print(len(FILE_ARRAY))
    for file in FILE_ARRAY:
        if file.endswith('.py'):
            with open(file, 'r', encoding='utf-8') as pyfile:
                for index, line in enumerate(pyfile, start=1):
                    line = line.strip()

                    if not IS_COMMENT:
                        if line.startswith("'''") or line.startswith('"""'):
                            IS_COMMENT = True
                            START_COMMENT_INDEX = index

                        elif line.startswith('#'):
                            COMMENT_NUMBER += 1
                        elif line == '':
                            BLANK_NUMBER += 1
                        else:
                            CODE_NUMBER += 1

                    else:
                        if line.endswith("'''") or line.endswith('"""'):
                            IS_COMMENT = False
                            COMMENT_NUMBER += index - START_COMMENT_INDEX + 1
                        else:
                            pass
        else:
            pass


    DICTSTATICAL = {'CODE_NUMBER': CODE_NUMBER,'COMMENT_NUMBER':COMMENT_NUMBER, 'BLANK_NUMBER':BLANK_NUMBER}
    return DICTSTATICAL

def main():
    TOTAL_ALL={}
    MYCODEDIR=''
    TOTAL_ALL = staticalCode(MYCODEDIR)
    print(TOTAL_ALL)


if __name__ == '__main__':
    main()