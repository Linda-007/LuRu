# coding=utf-8
import json
import os
import shutil
import time
from time import sleep
import  pytest
import requests


def getFile(path):
    n = int(input('请输入需要的案件数：'))
    # path = str(input('请输入文件夹路径：'))
    list = os.listdir(path)
    t = []
    for i in list:
        caseId = i[2:-4]
        t.append(caseId)
    print('放入的案件列表如下\n' + str(t[0:n]))
    return t[0:n]


def getCase(path):
    head = {
        # "Content-Type": "application/json",
        "Content-Type": "application/x-www-form-urlencoded"

    }
    url = "http://123.60.74.77:8080/demo/api/auto-data-entry/FtpFileTYController/handle"  # 上线测试
    # url = "http://tytest.kgcure.com:8080/demo/api/auto-data-entry/FtpFileTYController/handle"  # 生产测试
    # url = "http://ty.kgcure.com:8080/demo/api/auto-data-entry/FtpFileTYController/handle"  # 生产
    # url = "http://192.168.10.97:8080/auto-data-entry/FtpFileTYController/handle"
    #url = "http://192.168.10.149:7104/FtpFileTYController/handle"

    list = getFile(path)
    for i in list:
        # applySource 1是柜面，若isimage是1为柜面常规，0则为柜面（柜面案件不进入检索）， 2是微信
        applyList = {"applyList": [
            {"isImage": 1, "sendDate": str(time.strftime("%Y-%m-%d %H:%M:%S")), "applyNo": str(i),
             "expressCompany": "", "deliverNo": "",
             "organId": 2, "applySource": 2, "sendNum": "", "regType": 2, "applicant": "trt"}]}
        data = str(applyList)

        print('\n开始拉取案件：' + str(i))
        re = requests.post(url=url, data=data, headers=head)
        print(json.dumps(re.json(), sort_keys=True, indent=2, separators=(', ', ': '), ensure_ascii=False))
        sleep(0.1)
        # path_1 = path + '\\S_' + i + '.zip'
        # path_2 = "C:\\Users\\kv\\Desktop\\" + "已使用案件"
        # path_2 = "C:\\Users\\kv\\Desktop\\" + "压测已使用"

        # path_2 = "C:\\Users\\kv\\Desktop\\甲方案件\\已使用"

        # shutil.move(path_1, path_2)


if __name__ == '__main__':
    path = str(input('请输入文件夹路径：'))
    getCase(path)
    # getFile()
