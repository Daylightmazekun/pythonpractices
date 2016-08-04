'''
Created on 2016年8月4日

@author: mazekun
'''
import json

import xlwt


def load_data():
    f = open('./student.txt', 'r')
    return json.load(f)
def write_data_to_xls(data):
    xls = xlwt.Workbook()
    sheet = xls.add_sheet('student')
    for i in range(len(data)):
        sheet.write(i, 0, i+1)
        json_data = data[str(i+1)]
        for j in range(len(data)):#sheet.write相当于在xls中的坐标内容写信息
            sheet.write(i, j+1, json_data[j])

if __name__ == '__main__':
    data = load_data('student.txt')
    write_data_to_xls(data)