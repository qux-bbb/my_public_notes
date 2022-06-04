# python---pywin32-使用windows的API做一些事情

安装:  
```r
pip install pywin32
```

example1: 输出所有可用可见窗口标题  
```python
from win32gui import *
titles = set()
def foo(hwnd,mouse):
	#去掉下面这句就所有都输出了，但是我不需要那么多
	if IsWindow(hwnd) and IsWindowEnabled(hwnd) and IsWindowVisible(hwnd):
		titles.add(GetWindowText(hwnd))

EnumWindows(foo, 0)
lt = [t for t in titles if t]
lt.sort()
for t in lt:
	print t.decode('GB2312')
```

example2: windows弹窗  
```python
import win32api
import win32con
win32api.MessageBox(None,"Hello,pywin32!","pywin32",win32con.MB_OK)
```


2019/7/25  
