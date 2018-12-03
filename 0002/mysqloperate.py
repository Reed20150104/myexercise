#!/usr/bin/env python
# -*- encoding: utf-8 -*-

# import lib
import pymysql


'''
Project: myexercise
File: mysqloperate.py
Author: Reed
Date: 2018/11/20 23:02
MySQL数据库操作类
'''

class Mysql(object):
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                password='xxxx',
                db='testdb',
                charset='utf8'
            )
        except Exception as e:
            print("无法连接mysql")
            print(e)
        else:
            print('连接成功')
            self.cur = self.conn.cursor()


    def create_table(self):
        sql = 'create table if Not EXISTS promotion_code(id int primary key auto_increment, promotioncode VARCHAR(10))'
        res = self.cur.execute(sql)
        if res:
            self.conn.commit()
        else:
            self.conn.rollback()
        print(res)

    def close(self):
        self.cur.close()
        self.conn.close()

    def add_record(self, code):
        sql = "insert into promotion_code(promotioncode) values('%s')" % (code)
        print("i am here:"+code)
        res = self.cur.execute(sql)
        if res:
            self.conn.commit()
        else:
            self.conn.rollback()

    def delete_record(self):
        sql = 'delete from testdb where id = 1'
        res = self.cur.execute(sql)
        if res:
            self.conn.commit()
        else:
            self.conn.rollback()

    def modify_record(self):
        sql = 'update testdb set name="Jack" where id = 1'
        res = self.cur.execute(sql)
        if res:
            self.conn.commit()
        else:
            self.conn.rollback()

    def show_record(self):
        sql = 'select * from testdb'
        self.cur.execute(sql)
        res = self.cur.fetchall()
        for i in res:
            print(i)
