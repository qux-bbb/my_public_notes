# POST文件数据包示例

```r
POST /index.php/home/index/upload HTTP/1.1
Host: 11c89f80-0902-4136-8d6d-c01dd77b631f.node3.buuoj.cn
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:70.0) Gecko/20100101 Firefox/70.0
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8
Accept-Language: zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2
Accept-Encoding: gzip, deflate
Accept-Encoding: gzip, deflate
Content-Type: multipart/form-data; boundary=---------------------------241410948962
Connection: close
Upgrade-Insecure-Requests: 1
Content-Length: 441

-----------------------------241410948962
Content-Disposition: form-data; name="file"; filename="a.py"
Content-Type: text/plain

hello
-----------------------------241410948962
Content-Disposition: form-data; name="file2"; filename="a.php"
Content-Type: text/plain

<?php phpinfo(); ?>
-----------------------------241410948962--
Content-Disposition: form-data; name="submit"

Submit
-----------------------------241410948962--
```

头的字段值不要加双引号  
头的字段值不要加双引号   
头的字段值不要加双引号  


2019/11/3  
