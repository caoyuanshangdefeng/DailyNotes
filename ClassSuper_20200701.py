# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Daily_use -> ClassSuper_20200701
@IDE    ：PyCharm
@Author ：zhangzhen
@Date   ：2020/7/1 8:59
@Desc   ：
=================================================='''
'''
# Python引入了super()机制
class FooParent:
  def bar(self, message):
    print(message)
class FooChild(FooParent):
  def bar(self, message):
    FooParent.bar(self, message)
# print(FooChild().bar("Hello, Python."))


# 这样做有一些缺点，比如说如果修改了父类名称，那么在子类中会涉及多处修改，另外，Python是允许多继承的语言，如上所示的方法在多继承时就需要重复写多次，显得累赘。
# 为了解决这些问题，Python引入了super()机制，例子代码如下：



class FooParent:
    def bar(self, message):
        print(message)


class FooChild(FooParent):
    def bar(self, message):
        super(FooChild, self).bar(message)

# print(FooChild().bar("Hello, Python."))


'''


# super 的初始化

class Person:
    def __init__(self, name="person"):
        self.name = name
        print('Person的name',self.name)


class Puple(Person):
    pass

class Puple_Init(Person):
    def __init__(self, age):
        self.age = age
        super().__init__(self.age)


class Puple_Super(Person):
    def __init__(self,name,age):
        self.age=age
        super().__init__(name)


pp=Puple()

pp_i=Puple_Init(10)
pp_s=Puple_Super('zhangxiaodu',12)
