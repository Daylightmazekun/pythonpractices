'''
Created on 2016年8月13日

@author: mazekun
'''
import uuid

import pymysql


def generate_key():
    key_list = []
    for i in range(200):
        uuiddddd = uuid.uuid3(uuid.NAMESPACE_DNS, str(uuid.uuid1()))
        key_list.append(str(uuiddddd).replace('-', ''))
    return key_list
def write_to_mysql(key_list):
    print(key_list)
    conn = pymysql.connect(user = "root", passwd = "root", host = "localhost", db = "temp" )
    cursor = conn.cursor()
    cursor.execute("drop table if exists ukey")
    sql = """create table ukey(key_value char(40) not null)"""
    cursor.execute(sql)
    try:
        for i in range(200):
            cursor.execute('insert into ukey values("%s")'% key_list[i]) 
        print("ggggggg")
        conn.commit()
    except:
        print(pymysql.err)
    
    cursor.close()
    conn.close()
        








if __name__ == '__main__':
    write_to_mysql(generate_key())