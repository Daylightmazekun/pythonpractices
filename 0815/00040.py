'''
Created on 2016年8月15日

@author: mazekun
'''
from collections import Counter


if __name__ == "__main__":
    with open("test.txt", "r")as f:
        c = Counter()
        for line in f:
            words = line.split()
            c += Counter(words)
        for words in c.most_common():
            print(words)