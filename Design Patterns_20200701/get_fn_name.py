# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Daily_use -> get_fn_name
@IDE    ：PyCharm
@Author ：zhangzhen
@Date   ：2020/8/24 16:45
@Desc   ：
=================================================='''
import sys
def get_function_name():
    print('获取函数名称')
    fn_name=sys._getframe().f_code.co_name
    print("函数名称 : {} 数据类型 : {}".format(fn_name,type(fn_name)))





if __name__=="__main__":
    print(get_function_name())

















