# python---统计连续相同日期数量的正确思路

多想想人自己是怎么做判断的，这样就很少错误了  

```python
# coding:utf8

from openpyxl import load_workbook

wb_r = load_workbook('records_20200725-20200825.xlsx')
sheet = wb_r['raw']

current_date = sheet['A2'].value
current_num = 0
i = 2
while True:
    if current_date == sheet['A%d' % i].value:
        current_num += 1
        i += 1
    else:
        print(current_date, current_num)
        if not sheet['A%d' % i].value:
            break
        else:
            current_date = sheet['A%d' % i].value
            current_num = 1
            i += 1

```


2020/8/17  
