# python---dns查询示例

安装模块：  
```r
pip install dnspython
```

官方文档: https://dnspython.readthedocs.io  

示例：  
```python
# coding:utf8

import dns.resolver

# 不指定DNS服务器
answer = dns.resolver.resolve('watson.microsoft.com', 'A')
print('The answer are:')
for rr in answer:
    print(rr.address)

# 指定DNS服务器
resolver = dns.resolver.Resolver(configure=False)
resolver.nameservers = ['114.114.114.114']
answer = resolver.resolve('watson.microsoft.com', 'A')
print('The answer are:')
for rr in answer:
    print(rr.address)
```


2019/1/8  
