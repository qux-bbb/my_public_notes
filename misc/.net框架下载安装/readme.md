# .net框架下载安装

keywords: .net4.0 dotnet4.0  

很多时候.net程序运行出错是因为没有合适的.net框架。  

从这里选择版本下载安装：  
https://dotnet.microsoft.com/zh-cn/download/dotnet-framework  

最好下载脱机安装程序，提示缺少4.0版本时最好安装4.8版本的。  

如果出现这样的错误：  
```r
已处理证书链,但是在不受信任提供程序信任的根证书中终止
```
根据该链接: http://www.8u8v.com/a/post/netanzhuang.html, 下载安装补丁解决  
```r
先打上一个Windows6.1-KB2813430的补丁，然后再安装net-framework4.8即可成功。
32位系统补丁下载地址：
https://www.microsoft.com/zh-CN/download/details.aspx?id=39110
64位系统补丁下载地址：
https://www.microsoft.com/zh-CN/download/details.aspx?id=39115

这个方法对net-framework4.6.2版本~4.8版本都有效。
```


2022/9/14  
