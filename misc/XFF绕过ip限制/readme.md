# XFF绕过ip限制

有些网站可能会检测X-Forwarded-For的值，如果不符合预期就不允许访问，这里记一下相关的字段，值应该写 127.0.0.1 就好了  

```
X-Forwarded-For
X-Client-IP
X-Real-IP
X-Originating-IP
X-Remote-IP
X-Remote-Addr
CDN-Src-IP
```


2020/11/20  
