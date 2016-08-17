'''
Created on 2016年8月17日

@author: mazekun
'''
import os
import re


def word_count(file_path):
    word_dict = {}
    with open(file_path) as txt:
        for line in txt:
            words = re.findall(r'\w+', line.strip())
            print(words)
            for word in words:
                word = word.lower()
                word_dict[word] = word_dict.get(word, 0) + 1#字典get方法在此出 用于检索word在字典中的个数，如果有就在基数上加一，如果没有 就继续循环
    return word_dict





if __name__ == "__main__":
    result = word_count(os.path.join(os.path.dirname(os.path.abspath(__file__)), "test.txt"))
    print(result)