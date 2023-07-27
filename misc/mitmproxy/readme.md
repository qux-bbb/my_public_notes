# mitmproxy

keywords: https明文 https解密  

mitmproxy是一个开源交互式HTTPS代理，由于使用了python3.9，不支持win7。  

官网: https://mitmproxy.org  

安装后，配置系统代理为: http://localhost:8080  
启动mitmweb.exe，访问 http://mitm.it , 下载CA证书安装到根证书目录  
这样就可以查看https流量了  

如果出现这样的错误: `Certificate verify failed: unable to get local issuer certificate`  
可以在启动时添加参数: `mitmweb.exe --ssl-insecure`  
或者在 Options 下，勾选 "Don't verify server certificates"，一样的效果  

win10可以设置全局代理，所以mitmproxy、zap、burp都可以解析应用程序的https请求，但win7无法设置全局代理。  


参考链接: https://github.com/mitmproxy/mitmproxy/issues/1608  


2022/1/27  
