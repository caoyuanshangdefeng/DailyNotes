# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Daily_use -> LL
@IDE    ：PyCharm
@Author ：zhangzhen
@Date   ：2021/2/23 9:27
@Desc   :经纬度换算
=================================================='''


import struct
# python2
# struct.unpack('!f', '41B3F048'.decode('hex'))[0]
# python3
# GPS: Lat 4236E752 Long 41AA9498
# Lat_val=struct.unpack('!f', bytes.fromhex('4236E752'))[0]
# Long_val=struct.unpack('!f', bytes.fromhex('41AA9498'))[0]
# print('Lat_val : {},Long_val : {}'.format(Lat_val,Long_val))
#Lat_val : 45.72589874267578,Long_val : 21.322555541992188




# def multiplier(factor):
#     def multiplyByFactor(number):
#         print(2222)
#         return number*factor
#     return multiplyByFactor
# res=multiplier(2)
# print(res)

# def debug(func):
#     def wrapper():
#         print(222222)
#         # print('a:',a)
#         print('[DEBUG]: enter {}()'.format(func.__name__))
#         return func()
#     return wrapper
#
# @debug
# def say_hello():
#     print('hello!')
# say_hello()

# def warp(obj):
#     print('warpper')
#     return obj
#
#
# @warp  # 等价于 foo = warp(foo)
# def foo():
#     print('hello decorator!')
#
#
# foo()  # => hello decorator!


# def outer(func):  # 函数装饰器
#     def inner():
#         print('inner')
#         func()
#         return 'inner over'
#
#     return inner
#
#
# @outer  # foo = outer(foo)
# def foo():
#     print('hello foo')
#
# print(foo())  # => hello foo





















