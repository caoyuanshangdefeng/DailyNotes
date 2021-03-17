# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Daily_use -> SingletonPattern_20200701
@IDE    ：PyCharm
@Author ：zhangzhen
@Date   ：2020/7/1 9:48
@Desc   ：
=================================================='''
# 单例模式

class Singleton:
    def __new__(cls, *args, **kwargs):  # 用于在__init__之前，给整个对象初始化
        if not hasattr(cls, "_instance"):  # 如果这个类没有_instance属性
            cls._instance = super(Singleton, cls).__new__(cls)  # 则调用父类(Object)的__new__方法创建
        return cls._instance

class MyClass(Singleton):
    def __init__(self, a):
        print('a的值',a)
        self.a = a
        print(self.a)

"""本句执行时，先执行Singleton类的__new__方法，发现没有_instance属性，则调用父类__new__方法
创建一个实例，返回MyClass._instance，接着执行MyClass类的__init__方法，赋值self.a = 10"""
a = MyClass(10)

"""本句执行时，先执行Singleton类的__new__方法，发现有_instance属性，直接返回MyClass._instance，
接着执行MyClass类的__init__方法，赋值self.a = 20，把上面的10覆盖掉了"""
b = MyClass(20)

print(a.a)  # 20
print('11111')
print(b)  # 20
print(id(a),id(b))  #
