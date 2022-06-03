# python---根据函数名调用函数

```python
# coding:utf8
# python3

import hashlib

the_str = 'hello world'

for method in ['md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']:
    hash_value = eval('hashlib.{}'.format(method))(the_str.encode()).hexdigest()
    print(hash_value)
```


2020/8/23  
