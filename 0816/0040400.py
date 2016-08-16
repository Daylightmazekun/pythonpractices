'''
Created on 2016年8月16日

@author: mazekun    
'''
import operator
import re


if __name__ == "__main__":
    myfile = open("test.txt", 'r')
    words = re.findall(r"[\w']+", myfile.read())#匹配至少一个数字或字母组成的字符串
    words_dictionary = {}
    for word in words:
        if word not in words_dictionary:
            words_dictionary[word] = 0
            for item in words:
                if item == word:
                    words_dictionary[word] += 1
    sort_words_dictionary = sorted(words_dictionary.items(), key = operator.itemgetter(1), reverse = True)
    print(sort_words_dictionary)