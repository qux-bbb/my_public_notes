# python---Ttk-GUI示例

```python
# coding:utf8

from Tkinter import Tk, Spinbox
from ttk import Style, Label, Button, Combobox

top = Tk()
Style().configure('TButton', foreground='white', background='red')

Label(top, text='Animals (in pairs; min: pair, max: dozen)').pack()
Label(top, text='Number:').pack()

Spinbox(top, from_=2, to=12, increment=2, font='Helvetica -14 bold').pack()

Label(top, text='Type:').pack()

Combobox(top, values=('dog', 'cat', 'hamster', 'python')).pack()

Button(top, text='QUIT', command=top.quit, style='TButton').pack()

top.mainloop()

```


2018/10/19  
