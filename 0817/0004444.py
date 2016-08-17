'''
Created on 2016年8月17日

@author: mazekun
'''
import collections
import re


if __name__ == "__main__":
    def cal(filename = 'in.txt'):
        f = open(filename, 'r')
        data = f.read()
        dic = collections.defaultdict(lambda :0)#如果字典中没有该值时记为0
        data = re.sub(r'[\W\d]', ' ', data)
        data = data.lower()
        datalist = data.split(' ')
        for item in datalist:
            dic[item] += 1
        del dic['']
        return dic
    try:
        print(sorted(cal().items()))
    except:
        print("no input file")
        