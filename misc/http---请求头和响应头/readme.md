# http---请求头和响应头

全写确实太多了，写一下捕获到的

## 请求头部分  
* 请求方式，比如GET、POST,后面是请求链接
* Host: 指定请求的服务器的域名和端口号
* Connection: 表示是否需要持久连接。（HTTP 1.1默认进行持久连接）
* Upgrade-Insecure-Rquests：1
* User-Agent：浏览器、系统
* Accept：指定客户端能够接收的内容类型
* Referer：先前网页的地址，当前请求网页紧随其后,即来路
* Accept-Encoding：指定浏览器可以支持的web服务器返回内容压缩编码类型
* Accept-Language：浏览器可接受的语言
* Cookie：HTTP请求发送时，会把保存在该请求域名下的所有cookie值一起发送给web服务器  

举例：
```r
GET http://www.cnblogs.com/oxgen/p/HttpDownloader.html HTTP/1.1
Host: www.cnblogs.com
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.90 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Referer: https://www.baidu.com/link?url=hbaJh_zBO0Dw6t2Nv3QWwVPmjy9gmfRX254ln5Y6cGh7ea3XRqJPUcEdBzwJ2YzTTbu7xPg6Rn_ZsU2dNvpnAq&wd=&eqid=9311acd600002a0d0000000359ba09bf
Accept-Encoding: gzip, deflate
Accept-Language: zh-CN,zh;q=0.8
Cookie: bdshare_firstime=1488599026456; pgv_pvi=6243264512;Hm_lvt_674430fbddd66a488580ec86aba288f7=1505191380; CNZZDATA4343144=cnzz_eid%3D1897421969-1488369310-null%26ntime%3D1505191387
If-Modified-Since: Thu, 14 Sep 2017 08:57:09 GMT

```

## 响应头部分  
* HTTP版本、响应号
* Date: 原始服务器消息发出的时间
* Content-Type: 返回内容的MIME类型
* Connection: 表示是否需要持久连接。（HTTP 1.1默认进行持久连接）
* Vary: 告诉下游代理是使用缓存响应还是从原始服务器请求
* Cache-Control: 告诉所有的缓存机制是否可以缓存及哪种类型
* Expires: 响应过期的日期和时间
* Last-Modified: 请求资源的最后修改时间
* X-UA-Compatible: 采用何种IE版本渲染画面
* X-Frame-Options: 防止网页被Frame
* Content-Length: 请求的内容长度

举例：
```r
HTTP/1.1 200 OK
Date: Thu, 14 Sep 2017 08:59:48 GMT
Content-Type: text/html; charset=utf-8
Connection: keep-alive
Vary: Accept-Encoding
Cache-Control: private, max-age=10
Expires: Thu, 14 Sep 2017 08:59:58 GMT
Last-Modified: Thu, 14 Sep 2017 08:59:48 GMT
X-UA-Compatible: IE=10
X-Frame-Options: SAMEORIGIN
Content-Length: 26593

```


---
2017/9/14  
