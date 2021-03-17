# -*- coding: UTF-8 -*-
'''=================================================
@Project -> File   ：python_openpyxl -> 06-pyExcel_cell-style
@IDE    ：PyCharm
@Author ：zhangzhen
@Date   ：2020/5/15 10:19
@Desc   ：设置单元格字体风格

=================================================='''
from openpyxl import Workbook
from openpyxl.styles import Font, colors, Alignment
excel_address = "./test1.xlsx"

wb=Workbook()
wb.create_sheet("Mysheet1", 0)
'''
horizontal [ˌhɒrɪˈzɒntl] 水平的
vertical[ˈvɜːtɪkl] 垂直的

'''
sht = wb["Mysheet1"]
'''

设置字体类型
字体颜色
字体是否带下划线
是否为斜体
'''
sht["A1"] = "测试"
font_set = Font(name='Arial', size=24, italic=True, color=colors.BLUE, bold=True, underline='doubleAccounting')
sht['A1'].font = font_set

'''
字体水平居中,垂直居中
'''
sht["A5"] = "测试"
sht['A5'].alignment = Alignment(horizontal='center', vertical='center')

'''
字体水平向左,垂直向下
'''
sht["A6"] = "测试"
sht['A6'].alignment = Alignment(horizontal='left', vertical='bottom')
'''
字体水平向右,垂直向上
'''
sht["A7"] = "测试"
sht['A7'].alignment = Alignment(horizontal='right', vertical='top')

'''
存入数据自动回车换行
'''
sht["A9"] = "测试测试测试测试测试测试"
sht['A9'].alignment = Alignment(horizontal='left', vertical='top', wrap_text=True)
'''
存入数据不需要回车换行
'''
sht["A10"] = "测试测试测试测试测试测试"
sht['A10'].alignment = Alignment(horizontal='left', vertical='top', wrap_text=False)

wb.save(excel_address)
