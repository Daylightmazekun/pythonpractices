'''
Created on 2016年8月16日

@author: mazekun
'''
import re
def get_num():
    num = 0
    f = open('test.txt', 'r')
    for line in f.readlines():
        num += len(re.findall(r'[a-zA-Z0-9\']+', line))
    f.close()
    return num
if __name__ == "__main__":
    print(get_num())