'''
Created on 2016年8月17日

@author: mazekun
'''
import re


if __name__ == "__main__":
    with open('input.txt', 'r') as f:
        data = f.read()
    words = re.compile(r'[a-zA-Z]+') 
    dic = {}
    print(words.findall(data))
    for x in words.findall(data):
        if x not in dic:
            dic[x] = 1
        else:
            dic[x] += 1
L = []
for k,value in dic.items():
    L.append((k, value))
L.sort(key = lambda t:t[0])
for x in L:
    print(x[0], x[1])  