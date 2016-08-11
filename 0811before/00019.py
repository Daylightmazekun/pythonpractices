'''
Created on 2016年8月8日

@author: mazekun
'''
import codecs

from lxml import etree
import xlrd


def xls_xml(filename):
    data = []
    excel = xlrd.open_workbook(filename)
    table = excel.sheet_by_name('numbers')
    for i in range(table.nrows):
        data.append(table.row_values(i))
    output = codecs.open('numbers.xml', 'w', 'utf-8')
    root = etree.Element('root')
    numbers_xml = etree.ElementTree(root)
    numbers = etree.SubElement(root, 'numbers')
    print(type(numbers))
    numbers.append(etree.Comment("数字信息"))
    numbers.text = str(data)
    output.write(etree.tounicode(numbers_xml.getroot()))
    output.close()




if __name__ == '__main__':
    xls_xml('numbers.xls')