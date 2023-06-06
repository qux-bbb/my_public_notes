# web头部几个参数

```
POST http://1.2.3.4:1234/ HTTP/1.1
Host: 1.2.3.4:1234
User-Agent: Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3
Accept-Encoding: gzip, deflate
DNT: 1
Referer: http://www.iie.ac.cn 
Cookie: tetris-highscores=adsf%3A612
Connection: keep-alive
Content-Type: application/x-www-form-urlencoded
Content-Length: 45
x-forwarded-for:10.10.20.1

password=hello
--------------------------------------------------------------------------------
以此为例：
Referer  是表示访问此网址之前的网址，也就是来自哪里
X-forwarded-for  判断访问ip
--------------------------------------------------------------------------------
另外一个例子
Origin: http://www.suctf.com
referer: http://www.suctf.com
X-Forwarded-For: 202.98.24.124

origin用来表示请求最初来自哪里
```


2016/7/31  
