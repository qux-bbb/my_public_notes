## 0x01 HTTP Proxy Overview
介绍http代理的逻辑  


## 0x02 HTTP Proxy Setup
介绍ZAP的简单使用方法  
配置本地代理端口：  
工具-->选项-->Local Proxies，将Port设为8090  


## 0x03 HTTP Proxy Setup: The Browser
配置浏览器的代理，port也是8090  


## 0x04 Confirm it’s working
如果配置正确，在ZAP的下方"历史"栏会有WebGoat的流量  


## 0x05 Exclude WebGoat internal requests
排除webgoat内部请求  
这部分会将一些不需要捕获到的流量放行  

在ZAP下方的"历史"栏，选中一条记录，右键-->Exclude from-->Proxy，这样就会生成一条"放行记录"，经过代理不会再被拦截，直接被忽略，这里需要注意的是"放行记录"可以写成正则的形式  

添加的2条放行规则如下：  
```
http://127.0.0.1:8080/WebGoat/.*.lesson.lesson
http://127.0.0.1:8080/WebGoat/service/.*
```


## 0x06 Use the intercept
拦截请求并修改  
拦截就是上方有一个绿色的小按钮，按下变成红色就开启拦截了，修改完成后点击继续(向右的蓝色三角符号)  

需要修改的部分：  
1. POST改为GET  
2. 在header中添加`x-request-intercepted:true`  
3. 修改changeMe的值，这里的修改因为请求方法变成了GET，所以不是直接修改值就好了，应该把原来的删除，将changeMe拼接到url中，拼接之后第一行是这种形式：`GET http://127.0.0.1:8080/WebGoat/HttpProxies/intercept-request?changeMe=Requests are tampered easily HTTP/1.1`  


## 0x07 Use the "Edit and resend" functionality in ZAP
在ZAP下方的"历史"栏，选中一条记录，右键-->重发送...  
修改完成之后点击发送即可，还可以调整视图，感觉左边请求、右边发送的视图最舒服  