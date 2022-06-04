# python---urlparse

解析和拼接url  

python2
```python
# coding:utf8

import urlparse

print urlparse.urlparse('https://good.org/hello/question.html?happy=world#123')
# ParseResult(scheme='https', netloc='good.org', path='/hello/question.html', params='', query='happy=world', fragment='123')

print urlparse.urlunparse(('https', 'good.org', '/hello/question.html', '', 'happy=world', '123'))
# 'https://good.org/hello/question.html?happy=world#123'

# 拼接url超级有用，不用自己去考虑各种特殊情况了
print urlparse.urljoin('http://www.python.org/doc/FAQ.html', 'current/lib/lib.htm')
# http://www.python.org/doc/current/lib/lib.htm
```

python3  
```python
from urllib import parse

print(parse.urlparse('https://good.org/hello/question.html?happy=world#123'))
# ParseResult(scheme='https', netloc='good.org', path='/hello/question.html', params='', query='happy=world', fragment='123')

print(parse.urlunparse(('https', 'good.org', '/hello/question.html', '', 'happy=world', '123')))
# 'https://good.org/hello/question.html?happy=world#123'

# 拼接url超级有用，不用自己去考虑各种特殊情况了
print(parse.urljoin('http://www.python.org/doc/FAQ.html', 'current/lib/lib.htm'))
# http://www.python.org/doc/current/lib/lib.htm
```

2018/11/13  
