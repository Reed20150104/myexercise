#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# import lib
from bs4 import BeautifulSoup
import requests

'''
Project: myexercise
File: finddoc.py
Author: Reed
COMMENT: 找出html文件中正文部分
Date: 2019/2/14 23:10

'''


def searchBodyUrl(path):
    page = requests.get(path)
    page.encoding='utf-8'
    soup = BeautifulSoup(str(page.text), 'html.parser')

    urls = soup.findAll('a')
    for url in urls:
        try:
           print(url['href'])
        except KeyError:
            pass

    try:
        article = soup.select('.article')[0].text
        print(article)
    except IndexError:
        pass

if __name__ == '__main__':
    searchBodyUrl('https://news.sina.com.cn/c/xl/2019-02-24/doc-ihrfqzka8774799.shtml')


