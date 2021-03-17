# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Daily_use -> thread_demo
@IDE    ：PyCharm
@Author ：zhangzhen
@Date   ：2020/7/27 16:35
@Desc   ：
=================================================='''
import threading
import asyncio
import queue

# 需要重写来实现多线程调用
class Foo:
    def __init__(self):
        self.l = threading.Lock()
        self.l1 = threading.Lock()

        self.l.acquire()
        self.l1.acquire()
        pass

    def printA(self):
        self.l.acquire()
        print("A", threading.currentThread().getName())
        self.l1.release()


    def printB(self):
        print("B",threading.currentThread().getName())
        self.l.release()

    def printC(self):
        self.l1.acquire()
        print("C", threading.currentThread().getName())


if __name__ == '__main__':

    foo = Foo()

    async def test1():
        threading.Thread(target=foo.printA).start()

    async def test2():
        threading.Thread(target=foo.printB).start()

    async def test3():
        threading.Thread(target=foo.printC).start()

# 异步测试打印
    asyncio.run(test1())
    asyncio.run(test2())
    asyncio.run(test3())

