# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Daily_use -> python_attr_20200701
@IDE    ：PyCharm
@Author ：zhangzhen
@Date   ：2020/7/1 10:07
@Desc   ：Python的hasattr() getattr() setattr() 函数使用方法详解
=================================================='''


# hasattr(object, name)
# 判断一个对象里面是否有name属性或者name方法，返回BOOL值，有name特性返回True， 否则返回False。
# 需要注意的是name要用括号括起来

'''

class test():
    name="xiaohua"
    def run(self):
            return "HelloWord"

t=test()
print(hasattr(t, "name")) #判断对象有name属性,返回True
print(hasattr(t, "run") ) #判断对象有run方法,返回True

'''

# getattr(object, name[,default])
# 获取对象object的属性或者方法，如果存在打印出来，如果不存在，打印出默认值，默认值可选。
# 需要注意的是，如果是返回的对象的方法，返回的是方法的内存地址，如果需要运行这个方法，
# 可以在后面添加一对括号。


# '''
class test():
    name="zhangxiaodu"
    def run(self,a):
        name_run='111111111'
        print(a)

        return "HelloWord"

t = test()

print(getattr(t, "name")) #获取name属性，存在就打印出来。 返回zhangxiaodu
# print(getattr(t, "run"))  #获取run方法，存在就打印出方法的内存地址。 <bound method test.run of <__main__.test object at 0x0000021956D0CAC8>>
# print(getattr(t, "run")(11)) #获取run方法，后面加括号可以将这个方法运行。
#
# print(getattr(t, "age",''))  #获取一个不存在的属性。
# print(getattr(t, "age"))会报错
# Traceback (most recent call last):
#   File "E:/Daily_use/Design Patterns_20200701/python_attr_20200701.py", line 50, in <module>
#     print(getattr(t, "age"))  #获取一个不存在的属性。
# AttributeError: 'test' object has no attribute 'age'

# print(getattr(t, "age","属性不存在"))  #若属性不存在，返回一个默认值。

# '''

# setattr(object, name, values)
# 给对象的属性赋值，若属性不存在，先创建再赋值。

# class test():
#     name="zhangxiaodu"
#     def run(self):
#             return "HelloWord"
#
# t = test()
# print(hasattr(t, "age")) #判断age属性是否存在
# print(setattr(t, "age", 18)) #为属相赋值，并没有返回值
# print(hasattr(t, "age")) #判断age属性是否存在
print(getattr(t, "run",name_run))