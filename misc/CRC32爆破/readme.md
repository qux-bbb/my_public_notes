# CRC32爆破

有时候需要用CRC32值对应的原始内容，因为CRC32较短，可以在短时间内爆破出一些可能的值。  

## 内容小于6个字节
小于6个字节可以直接用脚本爆破，太长的话，脚本就太慢了  
```python
# coding:utf8
# python3

'''
文件名 内容长度 crc32值
3.txt 5 0x289585AF
2.txt 4 0xEED7E184
1.txt 5 0x9AEACC13
'''

from binascii import crc32
from itertools import product

dic = 'abcdefghijklmnopqrstuvwxyz0123456789_'


def crack(content_len, wanted):
    print('start cracking...')
    tuple_iter = product(dic, repeat=content_len)
    for char_tuple in tuple_iter:
        char_str = ''.join(char_tuple)
        crc32_value = crc32(char_str.encode())
        if crc32_value == wanted:
            print(char_str, hex(crc32_value))


if __name__ == '__main__':
    crack(5, 0x9AEACC13)
    crack(4, 0xEED7E184)
    crack(5, 0x289585AF)

'''
level6_isready
'''
```
如果要提高效率的话，需要使用多线程或多进程  


## 内容等于6个字节
有一个项目可以很快得出CRC32对应的若干个6位长度字符串：  
https://github.com/theonlypwner/crc32  

简单使用方法：  
```bash
py -3 crc32.py reverse 0x123456
```

供测试数据：  
```
name len crc32 content
1.txt 6 0xCC86365B forum_
2.txt 6 0xBCEE7ED5 91ctf_
3.txt 6 0xCCCA7E74 com_66
```


2020/9/10  
