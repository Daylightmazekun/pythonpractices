'''
Created on 2016年8月2日

@author: mazekun
将student.txt文本文档里的信息存储道excel表格里
'''
import json

import xlsxwriter


def json2xls():
    wb = xlsxwriter.Workbook('strdent.xls')
    ws = wb.add_worksheet('student')
    
    with open('./student.txt')as f:
        data = json.load(f)
        for i in range(len(data)):
            ws.write(i, 0, i+1)
            json_data = data[str(i+1)]
            for j in range(len(json_data)):
                ws.write(i, j+1, json_data[j])
    wb.close()



if __name__ == "__main__":
    json2xls()