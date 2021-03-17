# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：python_openpyxl -> 05-pyExcel_del-sheet
@IDE    ：PyCharm
@Author ：zhangzhen
@Date   ：2020/5/15 10:12
@Desc   ：Excel删除sheet
=================================================='''
from openpyxl import load_workbook
wb = load_workbook('./ATtest.xlsx')
# 方式一
try:
    wb.remove('aaaaa')
except:
    print('bug')
# 方式二
del wb['Sheet1']
wb.save('./ATtest.xlsx')
'''
使用两种方法时建议使用try/except
原因:当sheet名不存在时会报错
'''