#!/usr/bin/env python  
# encoding: utf-8  
# author: Glad Ma Zekun

'''
For now it just copise a file
'''

import sys.os

program, original, copy = sys.argv

#os.system(sys.argv[1])
fin = open(original)
fout = open(copy, "w")

fout.write(fin.read())

fin.close()
fout.close()