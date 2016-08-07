'''
Created on 2016年8月7日

@author: mazk
'''
from collections import OrderedDict
import json

from lxml import etree
import xlrd  # xls读取信息包？


def xls2xml(filename):
    with xlrd.open_workbook(filename) as wb:
        ws = wb.sheet_by_name("student")
    table = OrderedDict()
    for i in range(ws.nrows):
        key = int(ws.row_values(i)[0])
        value = str(ws.row_values(i)[1:])
        table[key] = value
    with open("student.xml", "w") as f:
        root = etree.Element("root")
        e_root = etree.ElementTree(root)
        e_student = etree.SubElement(root, "students")
        e_student.text = '\n'+str(json.dumps(table, indent=4, ensure_ascii=False))+'\n'
        e_student.append(etree.Comment('\n  students infomation \n   "id":[名字， 数学， 语文， 英语]\n'))
        filenewname = "student.xml"
        f.write('<?xml version="1.0" encoding="utf-8"?>'+etree.tounicode(e_root.getroot()))
        
        
        

if __name__ == '__main__':
    xls2xml('student.xls')