# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：python_openpyxl -> python_decorator_20200421
@IDE    ：PyCharm
@Author ：zhangzhen
@Date   ：2020/4/21 18:57
@Desc   ：python_decorator
=================================================='''


# import time
#
# def count_time(func):
#     print(func)
#     def int_time(*args, **kwargs):
#
#         start_time = time.time()  # 程序开始时间
#         func()
#         over_time = time.time()   # 程序结束时间
#         total_time = over_time - start_time
#         print('程序共计%s秒' % total_time)
#         return total_time
#     return int_time
#
# @count_time
# def demo():
#     print('>>>>开始计算函数运行时间')
#     x = 0
#     for i in range(1000000):
#         x=i//13
#     print(x)
#
# if __name__ == '__main__':
#     print('运行时间:',demo())
# import logging
#
# def use_logging(func):
#     print(func)
#     def wrapper():
#
#         # logging.warn("%s is running" % func.__name__)
#         return func()  # 把 foo 当做参数传递进来时，执行func()就相当于执行foo()
#
#     return wrapper
#
#
# def foo():
#     print('i am foo')
#
#
# foo = use_logging(foo)  # 因为装饰器 use_logging(foo) 返回的是函数对象 wrapper，这条语句相当于
# # foo = wrapper
# foo()  # 执行foo()就相当于执行 wrapper()

#
# def f1(func):
#     print(func,"AAA")
#     print ("F1")
#
# def f2(func):
#     print(func,"BBB")
#     print ("F2")
#
# @f1
# @f2
# def f3():
#     print ("F3")
