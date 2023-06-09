# python2---url编码解码示例

```python
# coding:utf8

import urllib

a = 'http://hello.com?a=1&c=中 国'

quote_str = urllib.quote(a)
print(quote_str)
# http%3A//hello.com%3Fa%3D1%26c%3D%3F%20%3F

unquote_str = urllib.unquote(quote_str)
print unquote_str

```


2019/9/2  
