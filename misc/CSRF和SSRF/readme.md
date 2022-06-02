# CSRF和SSRF

## CSRF
Cross-site request forgery，跨站请求伪造，也被称为 one-click attack 或者 session riding，有时也会缩写为XSRF。  

大概意思就是使用真正用户认证过的信息去发起请求，这样就相当于真正的用户发起了这次请求，一些恶意目的就达到了，比如刷别人的余额买东西，让别人给自己转账。  

防御的话，python的一些库都有给表单添加CSRF-token的功能，这样就可以保证请求只有一次生效，因为token是一次性的，这次验证过了，下次必须用新的token才能发起正常请求。  


## SSRF
Server-Side Request Forgery，服务器端请求伪造。  

形成的原因大都是由于服务端提供了从其他服务器应用获取数据的功能，且没有对目标地址做过滤与限制，比如从指定URL地址获取网页文本内容，加载指定地址的图片，文档，等等。这样就有可能访问到内网的资源了。常用作外网访通过网站进入内网的手段。  

防御的话，就是做过滤与限制。  


## 参考链接
https://baike.baidu.com/item/%E8%B7%A8%E7%AB%99%E8%AF%B7%E6%B1%82%E4%BC%AA%E9%80%A0/13777878  
https://www.jianshu.com/p/d1d1c40f6d4c  
https://www.cnblogs.com/iors/p/9777571.html  


---
2020/11/20  
