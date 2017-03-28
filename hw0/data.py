#!/bin/usr/python
import sys
file = open("a.dat") '''打开当前路径下的a.dat文件'''
n = int(sys.argv[1]) '''获取行数'''
lines = file.readlines()[n]
column = []
column += lines.split() '''将行的内容切割，存入column'''
column = list(map(float, column)) '''将内容转换为int'''
print(sorted(column))
file.close()
