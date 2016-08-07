'''
Created on 2016年8月7日

@author: mazkun
'''
import os

from lxml import etree
from lxml.builder import unicode
import xlrd, json, os


def changexls():
    data = xlrd.open_workbook("student.xls")
    table = data.sheets()[0]
    nrows = table.nrows
    #print(nrows)
    Dict = {}
    for i in range(nrows):
        Arr = table.row_values(i)
        Dict[Arr[0]] = Arr[1:]
    root = etree.Element('root')
   
    child1 = etree.SubElement(root, "student")
    child2 = etree.SubElement(root, "nimeiyoukancuo")
    comm = etree.Comment(u"""学生信息表  "id" : [名字， 数学， 语文， 英语]""")
    child1.append(comm)
    #child1.text = unicode(json.dumps(Dict).decode("utf-8"))
    child2.append(comm)
    child1.text = json.dumps(Dict)
    tree = etree.ElementTree(root)

    tree.write("student.xml", pretty_print=True, xml_declaration=True, encoding='utf-8')
    




if __name__ == '__main__':
    changexls()