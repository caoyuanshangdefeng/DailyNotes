# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：python_openpyxl -> 03-pyExcel
@IDE    ：PyCharm
@Author ：zhangzhen
@Date   ：2020/5/15 9:39
@Desc   ：
=================================================='''
from openpyxl import load_workbook
wb = load_workbook('./ATtest.xlsx')
ws2 = wb['AT_SMS_SendOrder']  # 常用
ws2.sheet_properties.tabColor = "1072BA"
wb.save('./ATtest.xlsx')

'''
最后把所有的Fail统计到一个表中,sheet带颜色


'''