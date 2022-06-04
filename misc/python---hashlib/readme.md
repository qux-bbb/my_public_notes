# python---hashlib

hashlib是专门提供hash算法的库。  

```python
from hashlib import md5, sha1, sha256, sha512

a = b"a test string"
print(md5(a).hexdigest())
print(sha1(a).hexdigest())
print(sha256(a).hexdigest())
print(sha512(a).hexdigest())
```


原链接: http://outofmemory.cn/code-snippet/1191/Python-usage-hashlib-module-do-string-jiami  


2016/8/13  
