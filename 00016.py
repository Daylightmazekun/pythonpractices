'''
Created on 2016年8月5日

@author: mazekun
'''
import json

import xlwt.Workbook


def txt2xls():
    with open('numbers.txt','r',encoding='utf-8')as f:
        data = f.read()
    datasecond = json.loads(data)
    book = xlwt.Workbook(encoding="utf-8")
    sheet = book.add_sheet('numbers')
    for i in range(len(datasecond)):
        for j in range(len(datasecond[i])):
            sheet.write(i, j, datasecond[i][j])
    book.save("studentss.xls")
if __name__ == '__main__':
    txt2xls()
    
    