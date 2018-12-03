#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# import lib

# import self file
from mysqloperate import Mysql

'''
Project: myexercise
File: mysqldbuse.py
Author: Reed
Date: 2018/11/20 22:47
目标：将随机生成的二百多个优惠码存入mysql数据库。
思路：1.生成优惠码
     2.将生成的优惠码存入MySQL
'''


def main():
    mysql = Mysql()
    mysql.add_record()


if __name__ == '__main__':
    main()

