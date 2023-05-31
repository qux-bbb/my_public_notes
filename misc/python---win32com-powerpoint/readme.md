# python---win32com-powerpoint

书上的例子有错误，详见：  
https://stackoverflow.com/questions/14538169/getitem-error-in-win32com-powerpoint-object-library  
要注意是从1开始，不是从0开始  

```python

# coding:utf8

from Tkinter import Tk
from time import sleep
from tkMessageBox import showwarning
import win32com.client as win32

warn = lambda app: showwarning(app, 'Exit?')
RANGE = range(3, 8)

def ppoint():
    app = 'PowerPoint'
    ppoint = win32.gencache.EnsureDispatch('%s.Application' % app)
    pres = ppoint.Presentations.Add()
    ppoint.Visible = True

    sl = pres.Slides.Add(1, win32.constants.ppLayoutText)
    sleep(10)

    sla = sl.Shapes(1).TextFrame.TextRange
    sla.Text = 'Python-to-%s Demo' % app
    sleep(1)
    slb = sl.Shapes(2).TextFrame.TextRange
    for i in RANGE:
        slb.InsertAfter('Line %d\r\n' % i)
        sleep(1)
    slb.InsertAfter("\r\nTh-th-th-that's all folks!")

    warn(app)
    pres.Close()
    ppoint.Quit()


if __name__ == '__main__':
    Tk().withdraw()
    ppoint()

```


2018/11/7  
