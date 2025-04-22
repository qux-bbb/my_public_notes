# ZAP

keywords: https流量 https明文 https解密 端口转发  

官网: https://www.zaproxy.org/  
github地址: https://github.com/zaproxy/zaproxy  

OWASP Zed Attack Proxy(ZAP), 网络应用扫描器，类似burp  

安装之前需要先装jdk: https://adoptium.net/zh-CN/temurin/releases/  

工具 -> 选项 -> Selenium, 配置Chrome.exe和Firefox的路径之后，可以直接在ZAP中打开配置好代理的浏览器，不需要考虑代理和证书的问题了

Fuzz功能相当于burp的Intruder  


## HUD
HUD: Head Up Display  
百度百科:  
```
抬头显示简称HUD，又被叫做平行显示系统，是指以驾驶员为中心、盲操作、多功能仪表盘。
它的作用，就是把时速、导航等重要的行车信息，投影到驾驶员前面的风挡玻璃上，让驾驶员尽量做到不低头、不转头就能看到时速、导航等重要的驾驶信息。
```


## linux安装使用
下载解压jdk tar.gz到合适位置：  
https://adoptium.net/temurin/releases/  
编辑 `/etc/profile` 末尾添加 `export PATH=$PATH:/root/jdk-17.0.8+7/bin`  
执行 `source /etc/profile` 使当前环境生效  

下载安装ZAP：  
https://www.zaproxy.org/download/  
```bash
chmod +x ZAP*.sh
./ZAP*.sh
```

启动ZAP：  
```bash
zap.sh
```


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


## 端口流量转发
ZAP不支持端口流量转发，暂时只知道能用Burpsuite  


## 使用代理
2.12.0之前：  
连接 -> Use Proxy Chain, 勾选"Use an outgoing proxy server"，填写地址端口即可  

2.12.0及以后：  
网络 -> 连接, HTTP代理 或 SOCKS代理，启用并填写地址端口即可  

相关链接：  
https://groups.google.com/g/zaproxy-users/c/7d1z7nDANHw  
https://www.zaproxy.org/docs/desktop/releases/2.12.0/  


---
2020/1/19  
