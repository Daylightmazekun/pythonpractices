'''
Created on 2016年8月8日

@author: mazekun
'''
import codecs

from lxml import etree
import xlrd


def xls_xml(filename):
    data = {}
    
    excel = xlrd.open_workbook(filename)
    table = excel.sheet_by_name('city')
    for i in range(table.nrows):
        data[table.row_values(i)[0]] = str(table.row_values(i)[1:])
    output = codecs.open('citys.xml', 'w', 'utf-8')
    root = etree.Element('root')
    citys_xml = etree.ElementTree(root)
    citys = etree.SubElement(root, 'citys')
    
    citys.append(etree.Comment("城市信息"))
    citys.text = data
    output.write(etree.tounicode(citys_xml.getroot()))
    


if __name__ == '__main__':
    xls_xml('city.xls')
