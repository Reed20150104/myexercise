#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# import lib
import re


'''
Project: myexercise
File: wordcount.py
Author: Reed
Date: 2018/12/16 16:54

'''


'''
统计文本文件中的单词出现的次数，统计出出现次数前10的单词
思路：打开目标文件->切词并统计-->打印统计结果，逆序得到的元组，切片前10
todo list:
构造一个数组大小为10
初始装入10个单词，按出现次数降序排列，再用剩下的元素依次与数组中的元素进行
比较，第一次确定出现次数最大者，第二次确定次大者，如此10次即可获取前10
过滤停用词，找出关键词
'''

def wordCount(filePath):
    file = open(filePath,'r')
    content = file.read()
    wordAndNumber = wordSplitAndCount(content)

    # 这里对排序的规则进行了定义，x指元组，x[1]是值，x[0]是键
    wordList = sorted(wordAndNumber.items(),key=lambda x:x[1],reverse=True)
    resultToDict = {}
    resultOfWord = {}
    for key,value in wordList:
        resultToDict[key] = value

    resultOfWord = filterStopWords('./filterWord.txt',resultToDict)
    print(resultOfWord.items())
    for key,value in list(resultOfWord.items())[0:10]:
        print(key + ' '+str(value))

    file.close()


def wordSplitAndCount(content):
    dictOfWord = {}
    filterRegex = re.compile(r'[,!：\.;?\'"0-9-]')
    afterSpecialClean = filterRegex.sub(r'', content.lower())
    #afterStopWord = filterStopWords('./filterWord.txt',content)
    words = afterSpecialClean.split()
    for word in words:
        if word in dictOfWord:
            dictOfWord[word] +=1
        else:
            dictOfWord[word] = 1
    return dictOfWord

def filterStopWords(stopFile,wordList):
    stopWordFile = open(stopFile)
    stopWord = stopWordFile.read().split('\n')
    for item in list(wordList):
        if item.lower() in stopWord:
            del wordList[item]

    stopWordFile.close()
    return wordList

def main():
    FILEPATH='./test.txt'
    wordCount(FILEPATH)
    #printResult()


if __name__ == '__main__':
    main()