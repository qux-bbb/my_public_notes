# python---重新加载模块

将a.py和b.py放在同一文件夹下  
在文件夹下执行a.py  
修改b.py中的name, a.py执行输出的结果会发生变化  

b.py  
```python
# coding:utf8
name = 'jack'
```

a.py  
```python
# coding :utf8

import time
from imp import reload

import b

while True:
    reload(b)
    print(b.name)
    time.sleep(2)
```


2020/1/19  
