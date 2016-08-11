'''
Created on 2016年8月11日

@author: mazkun
'''
import uuid


def gen(num, len):
    L = []
    for i in range(num):
        ran = str(uuid.uuid4()).replace('-', '')[:len]
        #uuid4 用来产生随机数
        if not ran in L:
            L.append(ran)
    return L



if __name__ == '__main__':
    for item in gen(200, 16):
        print(item)