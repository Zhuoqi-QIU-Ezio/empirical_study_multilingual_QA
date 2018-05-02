#!/usr/bin/python
# -*- coding: UTF-8 -*-

# 打开文件
fo = open("Tags.xml", "rb")
print("文件名为: ", fo.name)
line = fo.readline()
#print(line)

# if '\\x' in line:
#     print(line)

print("读取第一行 %s" % (line.decode('utf-8')))
line = fo.readline()
a = 0
while line:
    line = fo.readline()
    line_str = line.decode('utf-8')
    line = "json"
    if 'а'.encode('utf-8') or 'о'.encode('utf-8') or 'у'.encode('utf-8')or 'ы'.encode('utf-8')or 'э'.encode('utf-8')or 'я'.encode('utf-8') or 'ё'.encode('utf-8') or 'ю'.encode('utf-8') or 'и'.encode('utf-8') or 'е'.encode('utf-8') in line:
        print(line)
        print(line_str)
    break
    a = a+1

    if a == 100:
        break
#print(a)