#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# import lib

'''
Project: myexercise
File: starFilter.py
Author: Reed
Date: 2019/3/24 21:55
'''



def filterSensitiveWord(filePath):
    word = []
    with open(filePath,'rb') as pyFile:
        for w in pyFile.readlines():
            word.append(w.decode('utf-8'))
    return word

def getFilteredString(filePath, inputString):
    sensitiveWord = []
    sensitiveWord = filterSensitiveWord(filePath)
    for word in sensitiveWord:
        word = word.strip()
        if inputString.find(word) > -1:
            inputString = inputString.replace(word,len(word)*'*')


    return inputString

if __name__ == '__main__':
    str = input('Enter your words: ')
    FILEPATH='../0011/filtered_words.txt'
    print(getFilteredString(FILEPATH, str))
