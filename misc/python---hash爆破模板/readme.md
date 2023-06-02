# python---hash爆破模板

针对长度较短且字符范围较小的情况，如果太大，试试用hashcat  

```python
# coding:utf8

from hashlib import md5
from itertools import product
dic = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

def crack():
    for i in xrange(5):
        all_suffix = list(product(dic, repeat=i))
        for suffix_sin in all_suffix:
            suffix = ''.join(suffix_sin)
            md = md5(suffix)
            digest = md.hexdigest()
            if digest.isdigit():
                print(suffix,digest)


if __name__ == '__main__':
    crack()
```


2020/8/23  
