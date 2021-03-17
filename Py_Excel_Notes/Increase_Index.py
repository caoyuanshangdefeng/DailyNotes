# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：py_Excel -> 递增
@IDE    ：PyCharm
@Author ：zhangzhen
@Date   ：2020/6/18 16:47
@Desc   ：
=================================================='''


def createCounter():
    f = [0]

    def increase():
        f[0] = f[0] + 1
        return f[0]

    return increase


createA = createCounter()
print(createA())
createA = createCounter()
print(createA())
print(createA())
