# -*- coding:utf-8 -*-
import csv

# 获取ｊｓｏｎ数据
import json

# with open('aa.json', 'r',encoding='UTF-8') as f:
#     rows = json.load(f)
file = open("aa.json", 'r', encoding='utf-8')
aas = []
for line in file.readlines():
    dic = json.loads(line)
    aas.append(dic)

print(len(aas))
# 创建文件对象
f = open('data.csv', 'w',encoding='UTF-8')

# 通过文件创建csv对象
csv_write = csv.writer(f)

# writerow: 按行写入，　writerows: 是批量写入
# 写入数据 取列表的第一行字典，用字典的ｋｅｙ值做为头行数据
csv_write.writerow(aas[0].keys())

# 循环里面的字典，将value作为数据写入进去
for dic in aas:
    csv_write.writerow(dic.values())

# 关闭打开的文件
f.close()
