#!/usr/bin/env python
# -*- coding:utf-8 -*-

import random

'''
 此文件为文件结构说明，包括python解释器说明，文档编码方式，文件功能说明，主函数入口。
 python文件功能说明在此处
 Task 1 生成随机优惠码
 思路：1.先申明一个数组，数组中包含了数字，大小写字母组合
      2.使用随机数生成器生成第一步中的数组索引
      3.打印出指定个数的优惠码
'''

def generatePromotionCode(numberOfCode,length):
    stringOfNumberAndalphabet = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    print(stringOfNumberAndalphabet[61])
    print(len(stringOfNumberAndalphabet))
    #生成指定数目的优惠码
    for num in range(0, numberOfCode):
        print(getRandomCode(stringOfNumberAndalphabet, length))



def getRandomCode(array, lenOfArray):
    codeArray = ''
    for index in range(0, lenOfArray):
        codeArray += array[random.randint(0,61)]

    return codeArray



def main():
    numberOfPromotionCode = 200 #定义优惠码的个数
    lengthOfCodeArray = 10  #定义优惠码数组长度，生成指定长度的优惠码
    generatePromotionCode(numberOfPromotionCode,lengthOfCodeArray)

if __name__ == '__main__':
    main()
