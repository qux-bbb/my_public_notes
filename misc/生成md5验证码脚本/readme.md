# 生成md5验证码脚本

```python
from hashlib import md5
from itertools import product

dic = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
def get_code(md5_start):
    i = 0
    while True:
        all_suffix = list(product(dic, repeat=i))
        for suffix_sin in all_suffix:
            suffix = ''.join(suffix_sin)
            md = md5(suffix)
            digest = md.hexdigest()
            if digest.startswith(md5_start):
                return suffix
        i += 1
    return False

```


2019/8/4  
