'''
Created on 2016年8月16日

@author: mazekun
'''
import re


def count(file_name):
    f = open(file_name, 'rb')
    s = f.read()
    words = re.findall(r'[a-zA-Z0-9]+',s)
    return len(words)



if __name__ == "__main__":
    num = count("test.txt")
    print(num)