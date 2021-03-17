# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：py_Auto -> getip
@IDE    ：PyCharm
@Author ：zhangzhen
@Date   ：2020/6/8 19:33
@Desc   ：
=================================================='''
import socket

def get_host_ip():
    """
    查询本机ip地址
    :return:
    """
    try:
        s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        s.connect(('8.8.8.8',80))
        ip=s.getsockname()[0]
    finally:
        s.close()

    return ip

