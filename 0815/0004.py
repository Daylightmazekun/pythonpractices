'''
Created on 2016年8月15日

@author: mazekun
'''
#Error code.....
from collections import Counter
import re


def create_list():
    datalist = []
    with open(filename, 'r')as f:
        for line in f:
            content = re.sub("\"|,|\.", "", line)
            datalist.extend(content.strip().split(" "))
        return datalist
def wc(filename):
    print (Counter(create_list(filename)))

if __name__ == "__main__":
    filename = "test.txt"
    wc(filename)
