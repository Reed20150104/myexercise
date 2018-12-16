#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# import lib
import redis

from generate import generatePromotionCode



'''
Project: myexercise
File: operateredis.py
Author: Reed
Date: 2018/12/3 21:22

'''

import redis

generateCode = generatePromotionCode(200, 10)
pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
print(len(generateCode))
r = redis.Redis(connection_pool=pool)
i = 0
for code in generateCode:
    print(i)
    r.set(str(i), code)
    i+=1