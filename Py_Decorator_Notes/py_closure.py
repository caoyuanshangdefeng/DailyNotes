# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：python_openpyxl -> py_closure
@IDE    ：PyCharm
@Author ：zhangzhen
@Date   ：2020/6/9 9:38
@Desc   ：python的闭包
=================================================='''
'''
理解Python装饰器(Decorator)
想要理解Python中的装饰器，先理解闭包（closure）

闭包

在计算机科学中，闭包（英语：Closure），又称词法闭包（Lexical Closure）或函数闭包（function closures），是引用了自由变量的函数。这个被引用的自由变量将和这个函数一同存在，即使已经离开了创造它的环境也不例外。

'''


# print_msg是外围函数
def print_msg():
    msg = "I'm closure"

    # printer是嵌套函数
    def printer():
        print(msg)
    return printer


# 这里获得的就是一个闭包
# closure = print_msg()
# 输出 I'm closure
# closure()


'''
msg是一个局部变量，在print_msg函数执行之后应该就不会存在了。但是嵌套函数引用了这个变量，将这个局部变量封闭在了嵌套函数中，这样就形成了一个闭包。
'''

import functools
def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print(222,'call %s():' % func.__name__)
        print(333,'args = {}'.format(*args))
        return func(*args, **kwargs)

    return wrapper


@log
def test(p):
    print(111,test.__name__ + " param: " + p)


# test("I'm a param")

# 输出值:
# 222 call test():
# 333 args = I'm a param
# 111 test param: I'm a param

'''
装饰器在使用时，用了@语法，让人有些困扰。其实，装饰器只是个方法，与下面的调用方式没有区别：

def test(p):
    print(test.__name__ + " param: " + p)

wrapper = log(test)
wrapper("I'm a param")

@语法只是将函数传入装饰器函数，并无神奇之处。

值得注意的是@functools.wraps(func)，这是python提供的装饰器。它能把原函数的元信息拷贝到装饰器里面的 func 函数中。函数的元信息包括docstring、name、参数列表等等。可以尝试去除@functools.wraps(func)，你会发现test.__name__的输出变成了wrapper。

'''


'''
带参数的装饰器
装饰器允许传入参数，一个携带了参数的装饰器将有三层函数，如下所示：



'''
import functools


def log_with_param(text):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('call %s():' % func.__name__)
            print('args = {}'.format(*args))
            print('log_param = {}'.format(text))
            return func(*args, **kwargs)

        return wrapper

    return decorator


@log_with_param("param")
def test_with_param(p):
    print(test_with_param.__name__)




# print( test_with_param('我来了'))

'''
# 传入装饰器的参数，并接收返回的decorator函数
decorator = log_with_param("param")
# 传入test_with_param函数
wrapper = decorator(test_with_param)
# 调用装饰器函数
wrapper("I'm a param")

'''

#带有参数的装饰器
import time

def deco(func):
    def wrapper(a,b):
        startTime = time.time()
        a=a+2
        b=b+2
        func(a,b)
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("time is %d ms" %msecs)
    return wrapper


@deco
def func(a,b):
    print("hello，here is a func for add :")
    time.sleep(1)
    print("result is %d" %(a+b))

# if __name__ == '__main__':
#     f = func
#     f(3,4)
    #func()



#带有不定参数的装饰器
import time

def deco(func):
    def wrapper(*args, **kwargs):
        startTime = time.time()
        func(*args, **kwargs)
        endTime = time.time()
        msecs = (endTime - startTime)*1000
        print("time is %d ms" %msecs)
    return wrapper


@deco
def func(a,b):
    print("hello，here is a func for add :")
    time.sleep(1)
    print("result is %d" %(a+b))

@deco
def func2(a,b,c):
    print("hello，here is a func for add :")
    time.sleep(1)
    print("result is %d" %(a+b+c))


if __name__ == '__main__':
    f = func
    func2(3,4,5)
    f(3,4)
    #func()






