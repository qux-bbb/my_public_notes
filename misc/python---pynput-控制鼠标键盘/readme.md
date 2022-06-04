# python---pynput-控制鼠标键盘

github地址: https://github.com/moses-palmer/pynput  
官方文档: https://pynput.readthedocs.io/  

安装:  
```r
pip install pynput
```

example1:  
```python
# coding:utf8

import time
from pynput import mouse, keyboard

m = mouse.Controller()
k = keyboard.Controller()

k.press(keyboard.Key.ctrl)
k.press("n")
k.release("n")
k.release(keyboard.Key.ctrl)

time.sleep(1)

m.click(mouse.Button.left, 1)
k.type("Hello, World!")
```

example2:  
```python
# coding:utf8

import time
from pynput import keyboard

k = keyboard.Controller()

k.press(keyboard.Key.cmd)
k.press('r')
k.release('r')
k.release(keyboard.Key.cmd)
time.sleep(1)
k.type('notepad')
time.sleep(1)
k.press(keyboard.Key.enter)
time.sleep(1)
k.type('Hello World!')
```


2022/6/4  
