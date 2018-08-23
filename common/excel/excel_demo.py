
 
from xlwt import *

file = Workbook(encoding = 'utf-8')
table = file.add_sheet('sheet_one')
table.write(0,0,'hello')
table.write(1,1,'world')

# 单元格宽度
'''
xlwt中列宽的值表示方法：默认字体0的1/256为衡量单位。
xlwt创建时使用的默认宽度为2960，既11个字符0的宽度
所以我们在设置列宽时可以用如下方法：
width = 256 * 20    256为衡量单位，20表示20个字符宽度
'''
first_col=table.col(0)       #xlwt中是行和列都是从0开始计算的
first_col.width=256*20  

file.save('excelDemo.xls')



'''
style = xlwt.XFStyle()
font = xlwt.Font()
font.name = 'Tahoma'
font.bold = True
font.italic = True
font.underline = True
style.font = font
sheet.write(0, 0, 'some bold Times text', style)

再提升一下Big：合并单元格

sheet1.write_merge(0,1,0,1,"sum")
'''