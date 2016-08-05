'''
Created on 2016年8月5日

@author: mazekun
'''
import json
import xlwt.Workbook


def txt_to_xls(filepath):
    with open(filepath, 'r')as f:
        file_content = json.load(f)
        print(file_content)
        print(file_content[0])
        xls_workbook = xlwt.Workbook()
        xls_sheet = xls_workbook.add_sheet('numbers')
        style = xlwt.XFStyle()
        font = xlwt.Font()
        font.name = "黑体"
        for i in range(len(file_content)):
            for j in range(len(file_content)):
                xls_sheet.write(i, j, file_content[i][j])
                
        xls_workbook.save("nuMbersss.xls")

if __name__ == '__main__':
    txt_to_xls("numbers.txt")