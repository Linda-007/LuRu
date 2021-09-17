import requests
import json
from time import sleep
import time
from ftplib import FTP
import os
class daoruanjian():
    def ftp_up(self, filename):
        ftp = FTP()
        # ftp.set_debuglevel(2)
        ftp.connect('123.60.74.77', 21)
        # 连接
        ftp.login('kv', 'Kv123')
        ftp.set_pasv(False)
        # ftp .cwd('Public/TaiYang/online/')
        # ftp.cwd('Public/TaiYang/online2/')
        ftp.cwd('Public/TaiYang/online3/')
        # 选择操作目录
        bufsize = 1024
        # 设置缓冲块大小
        file_handler = open(filename, "rb")
        # 以读模式在本地打开文件
        ftp.storbinary('STOR %s' % os.path.basename(filename), file_handler, bufsize)
        # 上传文件
        # ftp.set_debuglevel(0)
        file_handler.close()
        ftp.quit()
        print("文件上传成功！")

    a = "202120400022009"
    def post_get(self,applyNo,applySource):
        url="http://123.60.74.77:8080/demo/api/auto-data-entry/FtpFileTYController/handle"
        headers={"Content-Type":"application/x-www-form-urlencoded"}
        body ={
                "applyList":[
                    {
                             "isImage":1,
                             "sendDate":"2021-09-02 15:05:05",
                             "applyNo":applyNo,
                             "expressCompany":"",
                             "deliverNo":"",
                             "organId":2,
                             "applySource":applySource,
                             "sendNum":1,
                             "regType":2,
                             "applicant":"trt"}]}
        res=requests.post(url=url,json=body,headers=headers)
        print(res.json())