# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：ServerCommunication -> FTPdemo
@IDE    ：PyCharm
@Author ：zhangzhen
@Date   ：2020/8/24 8:40
@Desc   ：
=================================================='''
from ftplib import FTP
# import ConfigParser
import os
import time

class MyFTP:
    def __init__(self):
        '''ftp服务器主机IP，端口等配置'''
        
        self.ftp_host = '0.0.0.0'
        self.ftp_port = 7000
       
        self.ftp_user = 'test'
        self.ftp_passwd = 'test'
        self.ftp = FTP()


    # 连接到ftp服务器
    def connect(self):
        print('is connecting to ftp server %s on %s' % (self.ftp_host, self.ftp_port))
        self.ftp.connect(self.ftp_host, self.ftp_port)

    # 登陆到ftp服务器
    def login(self):
        print('ready to login ftp server')
        self.ftp.login(self.ftp_user, self.ftp_passwd)
        print('login ftp server successfully')
        print(self.ftp.getwelcome())

    # 友好的关闭连接
    def quit(self):
        try:
            self.ftp.quit()
            print('colose ftp connection successfully')
        except Exception as e:
            print('%s' % e)

    def upload_file(self, src_file_path):
        with open(src_file_path,'w') as f:
            check_time=time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
            self.inputCont='CheckDataCommunication-{}'.format(check_time)
            f.write(self.inputCont)

        with open(src_file_path, 'rb') as file_handler:
            self.ftp.storbinary('STOR %s' % src_file_path, file_handler)
            print('文件：%s 已经上传到ftp' % src_file_path)

    def download_file(self, local_path, remote_file_path):
        with open(local_path, 'wb') as file_handle:
            self.ftp.retrbinary('RETR %s' % remote_file_path, file_handle.write)


    def Check_data_interaction_res(self,check_res_path):
        with open(check_res_path, 'r') as f:
            server_response=f.readlines()
            if self.inputCont==server_response[0]:
                print('FTP Communication normal')
                return 'PASS'

    def Check_FTP_data_interaction(self):
        try:
            self.connect()
            self.login()
            self.upload_file('zhangzhen-_Detect.txt')
            self.download_file('./CheckTestFile.txt', 'zhangzhen-_Detect.txt')
            self.quit()
            return  self.Check_data_interaction_res('./CheckTestFile.txt')
        except:
            return 'FTP server connect fail'
if __name__ == '__main__':
    ftp = MyFTP()
    aaa=ftp.Check_FTP_data_interaction()
    print(aaa)




