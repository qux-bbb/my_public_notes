# windbg---pykd

https://githomelab.ru/pykd/pykd-ext  

用 pykd 扩展就可以使用 python 来自动化 windbg 了  

加载：  
```r
.load pykd
```

执行脚本：  
```r
!py py_path
```

所有 api：  
https://githomelab.ru/pykd/pykd/-/wikis/API%20Reference  

一个简单的 python 例子，当参数是特定值时才停下来  
```python
# coding:utf8

from pykd import *


dbgCommand('bp KERNELBASE!CreateFileW')

while True:
    go()
    about_create_file_path = dbgCommand('du rcx')
    if 'smbv3_plg' in about_create_file_path:
        break
```


2020/7/16  
