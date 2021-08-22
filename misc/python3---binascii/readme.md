# python3---binascii

binascii模块可以把数据在二进制和 ASCII 之间转换，还有计算crc32的功能  

我现在只会16进制字符串和ascii字符串互转  

```python
# coding:utf8

import binascii

b = binascii.hexlify(b'hello')
c = binascii.unhexlify(b)
print(b)
print(c)
```

输出：  
```
b'68656c6c6f'
b'hello'
```


2020/5/18  
