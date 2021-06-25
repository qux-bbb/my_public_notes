# CRC32爆破

有时候需要用CRC32值对应的原始内容，因为CRC32较短，可以在短时间内爆破出一些可能的值。  

一个简单的脚本（慎用，可能卡死）：  
```python
# coding:utf8
# python3

'''
文件名 内容长度 crc32值
3.txt 5 0x289585AF 
2.txt 4 0xEED7E184
1.txt 5 0x9AEACC13
'''

import binascii
from itertools import product

dic = 'abcdefghijklmnopqrstuvwxyz0123456789_'


def crack(content_len, wanted):
    print('start cracking...')
    all_suffix = list(product(dic, repeat=content_len))
    for suffix_sin in all_suffix:
        suffix = ''.join(suffix_sin)
        crc32_value = binascii.crc32(suffix.encode())
        if crc32_value == wanted:
            print(suffix, hex(crc32_value))


if __name__ == '__main__':
    crack(5, 0x9AEACC13)
    crack(4, 0xEED7E184)
    crack(5, 0x289585AF)

'''
level6_isready
'''
```

有一个项目可以很快得出CRC32对应的若干个6位长度字符串：  
https://github.com/theonlypwner/crc32  
简单使用方法：  
```bash
py -3 crc32.py reverse 0x123456
```


2020/9/10  
