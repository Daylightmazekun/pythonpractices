'''
Created on 2016年8月13日

@author: mazekun
'''
import os
import random

import pymysql


f = open(os.getcwd()+'\\2', 'w')
for i in range(200):
    words = [chr(a) for a in range(65, 91)] + [chr(a) for a in range(97, 122)] + [str(a) for a in range(0, 11)]
    slices = random.sample(words,10)
    #temp = str(slices)
    temp = "".join(slices)+'\n'
    #print temp
    f.write(temp)
f.close()

f = open(os.getcwd()+'\\2', 'r')
wordline = f.readlines()
try:
    conn = pymysql.connect(user = "root", passwd = "root", host = "localhost", db = "temp")
    cursortest = conn.cursor()
    cursortest.execute("drop table if exists uuiddd")
    sql = """create table uuiddd(key_value char(40) not null)"""
    cursortest.execute(sql)
    count = cursortest.executemany('insert into uuiddd values(%s)',wordline)
    conn.commit()
    cursortest.close()
    conn.close()
except pymysql.Error as e:
    print(e)