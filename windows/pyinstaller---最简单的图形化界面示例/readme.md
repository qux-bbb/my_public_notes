# pyinstaller---最简单的图形化界面示例

最简单的莫过于弹窗了  

脚本如下：  
```python
# coding:utf8

import win32api
import win32con

win32api.MessageBox(None,"Hello,pywin32!","pywin32",win32con.MB_OK)
```

命令如下：  
```r
pyinstaller test.py -w --noupx
```


2020/9/2  
