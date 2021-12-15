# coding=utf-8
import json
import time
import requests

url = "https://service.tppension.cntaiping.com/tppservice/es/transportMarketInfo"
# http://uattest.tppension.cntaiping.com/tppservice/es/transportMarketInfo

header = {"Content-Type": "application/json", }

# a = "202120400022009"  # 微信案件申请号 2021204000256321001  2021204000256320  1166097|24064
# size = "84728942|94208"  # 压缩包大小 | excel大小  6425|33
a = input("请输入申请号：")
size = input("请输入文件大小：")
date = input("请输入回传日期：")  #日期格式20211214
num = input("请输入案件数量：")
data = {"caseNo": "",
        "sendTime": str(time.strftime("%Y-%m-%d %H:%M:%S")),
        "fileName": a + ".zip|WH2021004_8701_"+date+"_"+num +"_" + a + ".xls",
        "fileType": "zip|xls",
        "fileSize": size,
        "dataSource": "SYKJ",
        "applyNo": a}

re = requests.post(url=url, data=json.dumps(data), headers=header)

f1 = open("result.txt", "a+")    #回传结果
f2 = open("chuancan.txt", "a+")   #传入参数


print(re.json(), file=f1)
print(data, file=f2)
if __name__ == '__main__':
    print("回传成功，请查看结果文档")


