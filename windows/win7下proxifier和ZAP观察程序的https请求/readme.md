# win7下proxifier和ZAP观察程序的https请求

win7不支持全局代理，  
如果一个应用程序通过https通信，而且自身没有代理设置，可以通过proxifier和zap配合，观察https流量  

ZAP生成证书：  
Tools -> Options -> Dynamic SSL Certificates -> Save  
双击文件，按步骤将证书安装到可信根证书列表  

## 观察hello.exe的https流量
proxifier设置：  
Profile -> Proxy Servers...  
添加 127.0.0.1:8080, Protocol选HTTPS  

Profile -> Proxification Rules...  
添加规则，Application为"hello.exe", Action为"Proxy HTTPS 127.0.0.1"  
注意Default规则的Action为"Direct"，这样ZAP转发的流量不会被proxifier再次处理  

Profile -> Name Resolution...   
勾选"Proxifier DNS settings"下的"Resolve hostnames through proxy"  

这样就可以在ZAP中看到hello.exe相关的https流量了  

## 观察系统所有的https流量
和观察单个应用程序的区别就是Rules的设置  

先删除自己添加的规则，然后  
Profile -> Proxification Rules...  
将Default规则的Action设置为"Proxy HTTPS 127.0.0.1"  
针对ZAP添加例外规则，Application为"javaw.exe", Action为"Direct"  

这样就可以在ZAP中看除了ZAP之外所有程序的https流量了  

## 参考链接
https://www.mivm.cn/windows-capture-https-packet  


---
2022/2/21  
