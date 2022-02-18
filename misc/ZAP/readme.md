# ZAP

keywords: https流量  

官网: https://www.zaproxy.org/  

OWASP Zed Attack Proxy(ZAP), 网络应用扫描器，类似burp  

Fuzz功能相当于burp的Intruder  
安装之前需要先装jdk  


## HUD
HUD: Head Up Display  
百度百科:  
```
抬头显示简称HUD，又被叫做平行显示系统，是指以驾驶员为中心、盲操作、多功能仪表盘。
它的作用，就是把时速、导航等重要的行车信息，投影到驾驶员前面的风挡玻璃上，让驾驶员尽量做到不低头、不转头就能看到时速、导航等重要的驾驶信息。
```

配好代理之后, 打开浏览器自动弹出教程, 用火狐能正常显示  

挺有意思的  


## 中文是问号块的问题  
换个字体，电脑默认的字体是微软雅黑（Microsoft Yahei），换成这个就挺好的，当然也可以自己换成其他的  


## https网站证书问题
先导出zap生成的证书：  
Tools -> Options -> Dynamic SSL Certificates -> Save  

通过浏览器, 将证书安装到可信根证书列表  
谷歌浏览器的设置位置: 设置->高级->管理证书  

参考链接: http://www.lybbn.cn/data/datas.php?yw=171  


## 导出特定的请求响应
在左下角的"历史"标签，选择一个或多个记录，  
然后上方菜单："报告"->"将信息导出到文件中..."，即可成功保存  

记录可以通过请求方法、url关键字等进行简单的筛选，无法通过请求响应内容筛选。  


---
2020/1/19  
