openpyxl可以操作xlsx表格  
官方文档: http://openpyxl.readthedocs.io/en/stable/index.html  

```python
# coding:utf8

from openpyxl import load_workbook, Workbook

error_report_ids = [512, 386, 5206, 3595, 5389, 18, 4117, 22, 1819, 1315, 4009, 2348, 4910, 1460, 5301, 951, 700, 2237, 1214, 201, 1719, 4044, 4045, 1366, 5473, 5474, 2789, 2150, 1938, 1903, 1782]

wb_r = load_workbook('hd.xlsx')
sheet = wb_r['hd']

wb_w = Workbook()
ws1 = wb_w.active
ws1.append(['md5', 'RiskLevel', 'RiskName', 'task_id', 'cuckoo_score'])

for i in range(2, len(sheet['A'])+1):
    if sheet['F%d'%i].value == 'error':
        continue
    cuckoo_score = float(sheet['E%d'%i].value)
    if cuckoo_score >= 5:
        continue
    ws1.append([sheet['A%d'%i].value, sheet['B%d'%i].value, sheet['C%d'%i].value, sheet['D%d'%i].value, sheet['E%d'%i].value])

wb_w.save('hd_true.xlsx')

```

获取最大行列  
```python

wb = load_workbook('hd.xlsx')
ws = wb['hd']

print(ws.max_row)  # 行
print(ws.max_column)  # 列

```

设置单元格格式，比较麻烦  
```python

# coding:utf8

from openpyxl import load_workbook
from openpyxl.styles import Font, Side, Border, Alignment

font = Font(name='Calibri', size=11, color='FF000000')
sd = Side(style='thin', color="000000")
border = Border(left=sd, top=sd, right=sd, bottom=sd)

# wrap_text 自动换行
align = Alignment(horizontal='left', vertical='center', wrap_text=True)

def set_cell_style(cell):
    cell.font = font
    cell.border = border
    cell.alignment  = align
    return


sheet_path = 'C:/Users/hello/Desktop/ascii.xlsx'
wb = load_workbook(sheet_path)


ws = wb['hello']

for i in range(1, ws.max_row+1):
    for j in range(1, ws.max_column+1):
        set_cell_style(ws.cell(i, j))

wb.save(sheet_path)
```


参考：https://www.cnblogs.com/R-bear/p/7029621.html  
