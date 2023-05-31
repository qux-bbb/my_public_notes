# python---win32com-excel

安装模块  
```sh
pip install pywin32
```

```python
# coding:utf8

from Tkinter import Tk
from time import sleep
from tkMessageBox import showwarning
import win32com.client as win32

warn = lambda app: showwarning(app, 'Exit?')
RANGE = range(3, 8)

def excel():
    app = 'Excel'
    xl = win32.gencache.EnsureDispatch('%s.Application' % app)
    ss = xl.Workbooks.Add()
    sh = ss.ActiveSheet
    xl.Visible = True
    sleep(5)

    sh.Cells(1, 1).Value = 'Python-to-%s Demo' % app
    sleep(1)
    for i in RANGE:
        sh.Cells(i ,1).Value = 'Line %d' % i
        sleep(1)
    sh.Cells(i+2, 1).Value = "Th-th-th-that's all folks!"

    warn(app)
    ss.Close(False)
    xl.Application.Quit()


if __name__ == '__main__':
    Tk().withdraw()
    excel()

```


2018/11/6  
