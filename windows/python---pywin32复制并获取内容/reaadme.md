# python---pywin32复制并获取内容

安装模块：  
```r
pip install pywin32
```

示例：  
```python
# coding:utf8

import time
from win32 import win32gui, win32api, win32clipboard
import win32con


classname = 'TXGuiFoundation'
titlename = '笨蛋'
hwnd = win32gui.FindWindow(classname, titlename)
win32gui.SetForegroundWindow(hwnd)


win32api.keybd_event(0x11,0,0,0)  # ctrl
win32api.keybd_event(0x41,0,0,0)  # 'a'
win32api.keybd_event(0x11,0,win32con.KEYEVENTF_KEYUP,0)  #释放按键
win32api.keybd_event(0x41,0,win32con.KEYEVENTF_KEYUP,0)  #释放按键

time.sleep(1)

win32api.keybd_event(0x11,0,0,0)  # ctrl
win32api.keybd_event(0x43,0,0,0)  # 'c'
win32api.keybd_event(0x11,0,win32con.KEYEVENTF_KEYUP,0)  #释放按键
win32api.keybd_event(0x43,0,win32con.KEYEVENTF_KEYUP,0)  #释放按键

time.sleep(1)

win32clipboard.OpenClipboard()
text = win32clipboard.GetClipboardData(win32con.CF_UNICODETEXT)
print(text)
win32clipboard.CloseClipboard()
```


参考:  
1. https://blog.csdn.net/xc_zhou/article/details/86247518  
2. https://docs.microsoft.com/en-us/previous-versions/windows/embedded/ms909643(v%3dmsdn.10)  


2020/5/4  
