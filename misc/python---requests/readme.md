# python---requests

## 0x00 扯
一些关于requests的使用，基本上把官方说明文档的简单用法搬了过来，
官方说明文档的地址，[点击跳转](http://docs.python-requests.org/zh_CN/latest/user/quickstart.html)

## 0x01 基本get，post
最常用的应该就是get和post方法了吧
```python
import requests
# get
res = requests.get('http://www.baidu.com')
print(res.content)

#post
res = requests.post('http://www.baidu.com')
print(res.content)
```

## 0x02 发数据的 get，post
get方法发数据有一种比较简单的方法，因为它的参数会添加到url里，所以我们可以直接构造这样的url，比如搜索 hello
`requests.get('https://www.baidu.com/s?ie=utf-8&wd=hello')`
下面来看看正式的方法
```python
import requests

# get
payload = {'ie':'utf-8','wd':'hello'}
res = requests.get('http://www.baidu.com/s',params = payload)
print(res.content)

# post 大概样子是这样，例子结果可能不对
payload = {'ie':'utf-8','wd':'hello'}
res = requests.post('http://www.baidu.com/s', data = payload)
print(res.content)
```

## 0x03 头部处理
有时候需要获取头部信息或者添加头部信息，来个例子
```python
import requests

# 获取头部信息
res = requests.get('http://www.baidu.com')
print(res.headers)
print(res.headers['ETag'])

# 修改头部信息并发送
headers = {'Content-Length':'3000'}
res = requests.get('http://www.baidu.com',headers = headers)
print(res.content)
```  

## 0x04 获取响应码状态
响应状态在判断进行什么操作的时候很重要
```python
import requests

res = requests.get('http://www.baidu.com')
print(res.status_code)
```  

## 0x05 查看和发送cookie
cookie可以拿来干很多的事情呀
```python
import requests

# 查看cookie
res = requests.get('http://www.baidu.com')
print(res.cookies)
print(res.cookies['BDORZ'])

# 发送cookie
cookies = {'name':'hello','pass':'password'}
res = requests.get('http://www.baidu.com',cookies=cookies)
print(res.cookies)
```
## 0x06 会话对象session
有的时候我们需要在一个页面获取信息，之后再发给这个页面一些响应的信息  
如果按照上面的方法，只是相当于重新发起了一次请求，不能达到我们的目的 
这个时候我们需要用到session这个东西，就是建立一个会话来保持一些参数
```python
import requests

url = 'http://www.baidu.com'
# 建立会话
s = requests.session()
# 发起请求
res = s.get(url)
# 获取信息
data = {'status':res.status_code}
# 再次请求
res2 = s.post(url,data)
print(res2.content)
```

## 0x07 timeout
requests默认是阻塞型请求，所以设置timeout可以跳过一些无响应或者响应慢的情况  ,下面设置超时5秒
```python
import requests
# timeout
res = requests.get('http://www.baidu.com', timeout=5)
```

## 0x08 POST文件
```python
import requests

url = 'http://httpbin.org/post'
files = {'file': open('report.xls', 'rb')}
r = requests.post(url, files=files)
print(r.text)
```

## 0x09 使用代理
使用代理，这里把http和https的请求都通过http://127.0.0.1:10809发送  
```python
import requests

proxy = 'http://127.0.0.1:10809'
proxies={
    'http': proxy,
    'https': proxy,
}

res = requests.get('http://www.baidu.com', proxies=proxies)
```


## 0x10 尾
官方文档和搜索引擎还是比较好的学习方式  
