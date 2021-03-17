# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Daily_use -> python_methods_20201127
@IDE    ：PyCharm
@Author ：zhangzhen
@Date   ：2020/11/27 10:23
@Desc   ：python中的实例方法/类方法/静态方法
=================================================='''
'''
类:类是抽象的,在使用的时候通常会找到这个类的一个具体的存在,使用这个具体的存在,一个类可以找到多个对象
对象:某一个具体事务的存在,在现实世界中可以是看到饿到摸得着的,可以直接使用
类与对象的关系:类就是创建对象的模板
类的构成:
a:类的名称:类名
b:类的属性:一组数据
c:类的方法:允许对进行操作的方法(行为)

对象:当创建对象时,就是用一个模子来制造一个实物
对象来引用创建的类

类属性,实例属性
类属性:类对象所有的属性,它被所有类对象的实例对象所拥有,在内存中存在一个副本
实例属性:实例对象所拥有的属性,则是以self.开头(实例也可以访问类变量)






类与对象的关系:
1.实例方法,对象方法
实例方法或者叫对象语法,指的是类中定义的普通方法
只有实例化对象之后才使用的方法,该方法的第一个形参接收的一定是对象本身


'''


# class Person:#类名称
#     age=20 #类的属性
#     def hello(self): #类方法
#         print("hello")
        #self:对象本身




'''
2.静态方法
a:格式:在方法上添加@staticmethod
b:参数:静态方法可以有参数也可以无参数
c:应用场景:一般用于和类对象以及实例对象无关的代码
d:使用方式:类名.类方法(或者对象名.类方法名)

'''

# class Game:
#
#     @staticmethod
#     def menu():
#         print('------')
#         print('开始[1]')
#         print('暂停[2]')
#         print('退出[3]')
#
#
# Game.menu()




'''
3.类方法
无需实例化,可以通过类直接调用的方法,但是方法的第一个参数接收的一定是类本身
a:在方法上面添加@classmethod
b:方法的参数为cls也可以是其他名称,但是一般默认为cls
c:cls指向类对象
d:应用场景:当一个方法中只涉及到静态属性的时候可以使用类方法(类方法用来修改类属性)
e:使用可以是对象名.类方法名 或者类名.类方法名

    


'''


# class Person:
#     type = "人类"
#
#     @classmethod
#     def test(cls):
#         print(cls)
#         print(cls.type)
#
# Person.test()
'''
举例：使用类方法对商品进行统一打折
'''



class Goods:
    __discount = 1

    def __init__(self, name, price):
        self.name = name
        self.price = price

    @classmethod
    def change_discount(cls, new_discount):
        cls.__discount = new_discount

    @property
    def finally_price(self):
        return self.price * self.__discount


banana = Goods('香蕉', 10)
apple = Goods('苹果', 16)
Goods.change_discount(0.8)
print(banana.finally_price)
print(apple.finally_price)

Goods.change_discount(0.5)
print(banana.finally_price)
print(apple.finally_price)



'''
总结:
1.类方法的第一个参数是类对象cls,那么通过cls引用的必定是类对象的属性和方法;
2.实例方法的第一个参数是实例对象self,那么通过self引用的可能是类属性,也有可能是实例属性(这个需要具体分析),不过存在相同名称的类属性和实力属性的情况下,
实例属性优先级更高
3.静态方法中不需要额外定义参数,因此在静态方法中引用类属性的话,必须通过类对象来引用





'''

