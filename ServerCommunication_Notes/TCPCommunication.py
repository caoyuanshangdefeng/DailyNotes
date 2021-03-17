# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Daily_use -> TCPCommunication
@IDE    ：PyCharm
@Author ：zhangzhen
@Date   ：2020/8/22 14:12
@Desc   ：
=================================================='''


import socket
import time

def TCP_Server_Interaction(host,port):
    MaxBytes=1024*1024
    try:
        client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        client.settimeout(30)
        client.connect((host,port))
        check_time = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))

        inputData= 'CheckDataCommunication-{}'.format(check_time)   #等待输入数据
        sendBytes = client.send(inputData.encode())
        print('sendBytes : {}'.format(sendBytes))
        recvData = client.recv(MaxBytes)
        client.close()
        if recvData.decode()==inputData:
            print('TCP Communication normal')
            return 'PASS'
        else:
            return 'TCP server connect fail'

    except:
        return 'TCP server connect fail'


if __name__=="__main__":
    # host = '0.0.0.0'
    # port =3000
   
    TCP_Server_Interaction(host, port)

























