# 经纬度---16进制字符串转10进制数字

可能有的杂项题会遇到，脚本放在这儿，万一以后有用  

```python
#!/usr/bin/python
# -*-coding:utf-8 -*-

from ctypes import *

def convert(s):
    i = int(s, 16)                   # convert from hex to a Python int
    cp = pointer(c_int(i))           # make this into a c integer
    fp = cast(cp, POINTER(c_float))  # cast the int pointer to a float pointer
    return fp.contents.value         # dereference the pointer, get the float

print convert("41973333")    # returns 1.88999996185302734375E1

print convert("41995C29")    # returns 1.91700000762939453125E1

print convert("470FC614")    # returns 3.6806078125E4
```


2016/7/22  
