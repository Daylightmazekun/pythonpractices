'''
Created on 2016年8月16日

@author: mazekun
'''
import collections
import re


def count_word(file_name):
    
    f = open(file_name)
    line = f.readline()
    word_counter = collections.Counter()
    
    while line:
        words = re.findall("\w+", line.lower())
        word_counter.update(words)
        line = f.readline()
    f.close()
    return word_counter
if __name__ == "__main__":
    print(count_word("test.txt"))