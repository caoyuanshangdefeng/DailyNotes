# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：Daily_use -> get_class_all_fn
@IDE    ：PyCharm
@Author ：zhangzhen
@Date   ：2020/8/24 16:56
@Desc   ：
=================================================='''


class Menu:

    def __init__(self):
        pass

    def updateProject(self):
        test_name='updateProject'
        pass

    def restartProject(self):
        test_name = 'restartProject'
        pass

    def restartTomcat(self):
        test_name = 'restartTomcat'
        pass

    def stopTomcat(self):
        test_name = 'stopTomcat'
        pass

    def startTomcat(self):
        test_name = 'startTomcat'
        pass

    def methods(self):
        print(dir(self))
        return(list(filter(lambda m: not m.startswith("__") and not m.endswith("__") and callable(getattr(self, m)), dir(self))))

if __name__ == '__main__':
    print(Menu().methods())
