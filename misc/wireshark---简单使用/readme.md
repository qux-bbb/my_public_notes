# wireshark---简单使用

keywords: pcapng  

官网: https://www.wireshark.org/  

wireshark是一个很好用的流量捕获和解析工具。这里写一些简单用法。  


## 搜索
点击 `放大镜` 图标，可以进行各种搜索  
可以查的内容有：分组列表、分组详情、分组字节流  
可以搜的方式有：过滤器、十六进制值、字符串、正则表达式  


## 一些过滤规则
关于协议  
```r
http  # http协议
tcp   # tcp协议
tcp contains flag  # 过滤出tcp协议中包含 flag 的部分
```

关于端口  
```r
tcp.port == 80     # 源端口或者目的端口
tcp.srcport == 80  # 源端口
tcp.dstport == 80  # 目的端口
```

关于ip  
```r
ip.addr == 192.168.0.37  # 源ip或者目的ip
ip.src == 192.168.0.37   # 源ip
ip.dst == 192.168.0.37   # 目的ip
```

关于http请求数据方式  
```r
http.request.method == "GET"
http.request.method == "POST"
```

还可以用 and 或者 or 把几条规则联系起来  


## 导出文件
如果流量包里有文件存在的话，可以这样导出: 文件->导出对象->http  
导出对象有几种选项：DICOM、HTTP、SMB、TFTP，一般用HTTP导出  

文件过大时(约4M)无法识别导出，可以通过保存原始数据，用HxD手动提取的方式获取文件：  
1. 追踪流，"Show data as"选择"原始数据"，另存为，这样就可以保存原始数据
2. 使用HxD打开保存的文件，根据Content-Length等字段确定文件大小和起始位置，右键选择范围，复制粘贴到新文件即可

或者使用chaosreader(perl脚本)，可以提取文件，效果很好，但没有关联文件名  
https://www.brendangregg.com/chaosreader.html  
最好在单独的文件夹内操作，会生成大量文件，浏览器打开index.html查看  

或者使用NetworkMiner，提取文件效果很好  
https://www.netresec.com/?page=NetworkMiner  
提取完成后，切换到"Files"选项窗口，选择一行右键"Open folder"，即可查看提取的文件  


## 追踪流
追踪流可以更直观地查看一些交互流量  
选中一行，右键->追踪流->TCP流  
追踪流有几种选项：TCP、UDP、SSL、HTTP，一般用TCP、UDP、HTTP  


## 捕获时只保存特定流量
在选择网卡处有过滤器，可以下拉选择，举2个例子：  
1. 只捕获端口80的流量: `port 80`
2. 只捕获1.2.3.4 ip的流量: `host 1.2.3.4`


## 各种示例流量包
https://wiki.wireshark.org/SampleCaptures  


## wireshark找不到网卡
win10的系统，打开wireshark之后只有3个USB接口，各种尝试无果  
最后才知道是权限问题，只要管理员权限启动就好了，可能感谢lb吧  


## Wireshark解析浏览器的https流量
可以通过设置本地环境变量和Wireshark的解析方式，解密浏览器的加密流量。  
仅适用浏览器流量，可以是chrome和firefox，IE不行  

1. 在本地系统环境变量中添加`SSLKEYLOGFILE`项，值可设为`D:\key.log`
2. Wireshark中选择 `编辑>首选项>Protocols>SSL>(Pre)-Master-Secret log filename`项，填写刚刚设的值(即`D:\key.log`)
3. 重新启动浏览器，Wireshark就可以解析捕获到的SSL加密流量(同时会生成`debug.log`和`debug.file`文件，不用关注，之后删掉即可)。

如果没有SSL协议，那就是TLS协议  
不能将 SSLKEYLOGFILE 的值设置为 `C:\key.log` ，因为权限问题不能写入，可以是 `C:\Users\hello\Desktop\key.log`  

原链接：http://bobao.360.cn/learning/detail/249.html  


---
2017/9/2  
