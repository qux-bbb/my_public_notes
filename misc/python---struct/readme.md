# python---struct

keywords: struct bytes python 数据互转  

https://docs.python.org/3/library/struct.html  

二进制数据和各种类型数据的转换  

因为不同平台默认大小端不同，所以如果是多个字节最好指定一下大小端  
```r
<   小端
>   大端
```

常用的长度符号表示，小写表示有符号，大写表示无符号  
```r
b   1   signed char
h   2   short
i   4   int
l   4   long
q   8   long long

B   1   unsigned char
H   2   unsigned short
I   4   unsigned int
L   4   unsigned long
Q   8   unsigned long long
```

文档里写得很详细了，这里可以复制一些简单的例子过来  

```python
import binascii
import struct

a = 0x12345678
b = struct.pack('<L', a)  # 小端，无符号长整形
print(binascii.hexlify(b))  # b'78563412'
c = struct.unpack('<L', b)[0]
print(hex(c))  # 0x12345678
```

```python
# < 小端
# L 无符号 4个字节
# B 无符号 1个字节
aa = struct.unpack('<LB', b'\x78\x56\x00\x00\x12')
print(aa)
print(hex(aa[0]), hex(aa[1]))
'''
(22136, 18)
0x5678 0x12
'''
```

```python
# h 有符号 2个字节
# l 有符号 4个字节
>>> from struct import *
>>> pack('hhl', 1, 2, 3)
b'\x00\x01\x00\x02\x00\x00\x00\x03'
>>> unpack('hhl', b'\x00\x01\x00\x02\x00\x00\x00\x03')
(1, 2, 3)
>>> calcsize('hhl')
8
```


2020/5/28  
