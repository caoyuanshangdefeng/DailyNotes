# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Daily_use -> UDPCommunication
@IDE    ：PyCharm
@Author ：zhangzhen
@Date   ：2020/8/22 14:29
@Desc   ：
=================================================='''
import socket
import time

def UDP_Server_Interaction(host,port):
    addr = (host, port)
    server_conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    print('server_conn res:{}'.format(server_conn))
    check_time = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
    send_data = 'CheckDataCommunication-{}'.format(check_time)
    UDP_send = server_conn.sendto(send_data.encode(), addr)
    print('UDP_send_res : {}'.format(UDP_send))

    UDP_response, addr = server_conn.recvfrom(2048)
    print('UDP_response : {}'.format(UDP_response))
    server_conn.close()

    if UDP_response.decode() == send_data:
        print('UDP Communication normal')
        return 'PASS'
    else:
        return 'UDP server connect fail'
    # try:
    #     server_conn = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #     print('server_conn res:{}'.format(server_conn))
    #     check_time = time.strftime('%Y-%m-%d_%H_%M_%S', time.localtime(time.time()))
    #     send_data = 'CheckDataCommunication-{}'.format(check_time)
    #     UDP_send =server_conn.sendto(send_data.encode(), addr)
    #     print('UDP_send_res : {}'.format(UDP_send))
    #
    #     UDP_response, addr = server_conn.recvfrom(2048)
    #     print('UDP_response : {}'.format(UDP_response))
    #     server_conn.close()
    #
    #     if UDP_response.decode()==send_data:
    #         print('UDP Communication normal')
    #         return 'PASS'
    #     else:
    #         return 'UDP server connect fail'
    #
    # except:
    #     return 'UDP server connect fail'

if __name__=="__main__":
    host = '0.0.0.0'
    port = 7050
    print(UDP_Server_Interaction(host, port))


