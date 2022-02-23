# coding=utf-8
import random
import os
import zipfile
import paramiko

# ysj案件上传脚本
class ysjImport():
    imagePath='C:\\Users\\kv\\Desktop\\2'
    ftp_host = '192.168.10.136'
    ftp_user = 'sftpuser'
    ftp_pwd = 'Kv123456'
    ftp_path = '/files/CP01/claim/outimages/'
    #开发环境
    # ftp_host = 'ftp-claim-develop-cron.insuresmart.com.cn'
    # ftp_user = 'ftp_claim_develop_external_knvs'
    # ftp_pwd = 'cjWOpC@tM@E7RME2'
    # ftp_path = '/CP01/claim/outimages/'



    ##sftp上传
    def put_file(self,local_file,file_name):
        t = paramiko.Transport((self.ftp_host, 22))
        t.connect(username=self.ftp_user, password=self.ftp_pwd)
        sftp = paramiko.SFTPClient.from_transport(t)
        print('上传:', local_file)
        sftp.put(local_file, os.path.join(self.ftp_path, file_name))
        t.close()#关闭连接

    ##zipAndOkFile
    def zipNewName(self, path):
        path = path
        f = os.listdir(path)
        for i in f:
            datastr = str(i)
            filePath=path+i;
            #解压
            if datastr.find(".zip") > 0:
                zip_file = zipfile.ZipFile(filePath)
                zip_list = zip_file.namelist() # 得到压缩包里所有文件
                for f in zip_list:
                    zip_file.extract(f, path) # 循环解压文件到指定目录
                # 关闭文件，必须有，释放内存
                zip_file.close()
                os.remove(filePath)
            if datastr.find(".ok") > 0:
                os.remove(filePath)
        f = os.listdir(path)
        for i in f:
            filePath=path+i;
            if os.path.isdir(filePath):
                varstr = str(random.random())
                varstr = varstr[2:10]
                newname = '2022204' + varstr
                newFileName =path + newname;
                os.rename(filePath,newFileName )
                print(i + ">>>>>>>改名为>>>>>>" + newname);
                self.zip_file(newFileName,newname);
                self.rmfile(newFileName)
            else:
                os.rmdir(filePath)
    #压缩并生成ok文件
    def zip_file(self,src_dir,nn):
        zip_name = src_dir +'.zip'
        z = zipfile.ZipFile(zip_name,'w',zipfile.ZIP_DEFLATED)

        for path, dirnames, filenames in os.walk(src_dir):
            for filename in filenames:
                z.write(os.path.join(path, filename),os.path.join(nn, filename))
        z.close()
        okfile=src_dir+'.ok'
        with open(okfile,"a+") as f:
            f.write(str(123))
            f.write('\r\n')
            f.close()
    #删除文件
    def rmfile(self,filePath):
        if os.path.isdir(filePath):
            f = os.listdir(filePath)
            for i in f:
                newfilePath=filePath+"/"+i;
                self.rmfile(newfilePath)
            os.rmdir(filePath)
        else:
            os.remove(filePath)

    def startProcess(self):
        uploadPath =self.imagePath;
        print(uploadPath);
        uploadPath = uploadPath + "/"
        self.zipNewName(uploadPath)
        f = os.listdir(uploadPath)
        for i in f:
            datastr = str(i)
            filePath=uploadPath+i;
            #上传zip文件
            if datastr.find(".zip") > 0:
                self.put_file(filePath,datastr)
        for i in f:
            datastr = str(i)
            filePath = uploadPath + i;
            #上传ok文件
            if datastr.find(".ok") > 0:
                self.put_file(filePath,datastr)
            print('上传完成:', datastr)


if __name__ == "__main__":
    ysjImport().startProcess()