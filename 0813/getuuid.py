'''
Created on 2016年8月13日

@author: mazekun
'''
import uuid


f = open('./key.txt', 'w')
for i in range(200):
    f.write(str(uuid.uuid4()) + '\n')
f.close()
