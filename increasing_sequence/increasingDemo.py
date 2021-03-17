# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：python_openpyxl -> increasingDemo
@IDE    ：PyCharm
@Author ：zhangzhen
@Date   ：2020/6/20 9:54
@Desc   ：
=================================================='''





step=0

def autoIncrement():

  global step,code

  pStart = 1

  pInterval = 1

  if (step == 0):

    step = pStart

  else:

    step = step + pInterval

  code='{}'.format(step)

  return code



# print(autoIncrement())
# print(autoIncrement())
# print(autoIncrement())
# print(autoIncrement())

# '''
# 计数器(每次调用均自增1) -- 生成器
# '''
# def increase():
#     n = 0
#     while True:
#         n = n+1
#         yield n
# it = increase()
#
# def counter():
#     return next(it)



# def sum(num1,num2):
#     if num1+num2 >5:
#         step = 0
#
#
# print(autoIncrement())
# print(autoIncrement())
# sum(1,1)
# print(autoIncrement())
# print(autoIncrement())



# for i in [chr(65 + i) for i in range(11)]:
#     print(i)
# import re


# sysinfoNow='1,0,0,17,255'
# sysinfoLst = re.findall(r'^[0-4]{1},[0-4]{1},0,[1]?[0-9]{1},1$', sysinfoNow)
# print(sysinfoLst)

#
# sysinfoLst = re.findall(r'^[0-1]{1},0,(?:0|255),[1]?[0-9]{1},(?:0|255)$', sysinfoNow)
#
# print(sysinfoLst)

print('aa'+'bb')

















