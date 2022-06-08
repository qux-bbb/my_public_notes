# python---re

python的re模块简单使用  
re.findall, re.compile, re.match和re.search  

## `re.findall`
这个是最好用的，查找所有符合条件的，返回list，或None  
```python
import re

str1 = 'gdfd,good'
results = re.findall(r'g..d', str1)
print(results)
```

## `re.compile`
编译一个正则表达式，用这个在多次调用正则时可能会快一些，把上面的例子改成使用这样的形式  
```python
import re

reobj = re.compile(r'g..d')
str1 = 'gdfd,good'
results = reobj.findall(str1)
print(results)
```

## `re.match & re.search`
match和search都是匹配一次，match必须从开头匹配  

match示例
```python
import re

str1 = 'gdfd,good'
m = re.match(r'gdfd', str1)
if m:
    print(m.group(0))
else:
    print('Not found')
m = re.match(r'good', str1)
if m:
    print(m.group(0))
else:
    print('Not found')
```
结果:  
```r
gdfd
Not found
```

search示例  
```python
import re

str1 = 'gdfd,good'
s = re.search(r'gdfd', str1)
if s:
    print(s.group(0))
else:
    print('Not found')
s = re.search(r'good', str1)
if s:
    print(s.group(0))
else:
    print('Not found')
```
结果:  
```r
gdfd
good
```


## `对group的解释`
group()和group(0)等价，是正则字符串匹配的所有内容  
group(1)指捕获的第一个结果(第一个括号匹配的内容)，之后类推  



## 一些正则
有分组但不捕获  
```r
(?:hello)
```

一个名字为the_name的分组  
```r
(?P<the_name>hello)
```

使用已命名的分组  
```r
(?P<named_group>cool) (?P=named_group)
```

简单的ip域名匹配  
```python
ip_re = rb'(?P<ip>(?:\d{1,3}\.){3}\d{1,3})'
domain_re = rb'(?P<domain>(?:[-a-zA-Z0-9]+\.)+[a-zA-Z]+)'
```

更多正则和测试可以用这个网站，超级好用: https://regex101.com/  


## `匹配bytes-like object`
有时候需要匹配二进制数据，需要在正则表达式前加 `b`  
```python
# coding:utf8

# TypeError: cannot use a string pattern on a bytes-like object

import re

the_re = rb'Hello'
the_bytes = b' Hello fasdf'
result = re.findall(the_re, the_bytes)
print(result)
```


## `参考链接`
1. https://www.runoob.com/python/python-reg-expressions.html  
2. https://docs.python.org/zh-cn/3/library/re.html  


---
2018/11/12  
