#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# import lib

'''
Project: myexercise
File: filtersensitiveword.py
Author: Reed
Date: 2019/3/24 21:30

'''

def filterwords(filePath):
    words = []
    with open(filePath, 'rb') as pyfile:
        for line in pyfile.readlines():
            words.append(line.decode('utf-8'))

    iw = input('enter your words: ')
    for w in range(len(words)):
        if iw.find(words[w].strip()) > -1:
            print('Freedom')
        else:
            print('Human Rights')

if __name__ == '__main__':
    FILE_PATH = "./filtered_words.txt"
    filterwords(FILE_PATH)
