# wireshark---简单使用

官网: https://www.wireshark.org/  

wireshark是一个很好用的流量捕获和解析工具。这里写一些简单用法。  


## 搜索
点击 `放大镜` 图标，可以进行各种搜索  
可以查的内容有：分组列表、分组详情、分组字节流  
可以搜的方式有：过滤器、十六进制值、字符串、正则表达式  


## 一些过滤规则
关于协议  
```
http  # http协议
tcp   # tcp协议
tcp contains flag  # 过滤出tcp协议中包含 flag 的部分
```

关于端口    
```
tcp.port == 80     # 源端口或者目的端口
tcp.srcport == 80  # 源端口
tcp.dstport == 80  # 目的端口
```

关于ip  
```
ip.addr == 192.168.0.37  # 源ip或者目的ip
ip.src == 192.168.0.37   # 源ip
ip.dst == 192.168.0.37   # 目的ip
```

关于http请求数据方式  
```
http.request.method == "GET"
http.request.method == "POST"
```

还可以用 and 或者 or 把把几条规则联系起来  


## 导出文件
如果流量包里有文件存在的话，可以这样导出: 文件->导出对象->http  
导出对象有几种选项：DICOM、HTTP、SMB、TFTP，一般用HTTP导出  


## 追踪流
追踪流可以更直观地查看一些交互流量  
选中一行，右键->追踪流->TCP流  
追踪流有几种选项：TCP、UDP、SSL、HTTP，一般用TCP、UDP、HTTP  


## 捕获时只保存特定流量
在选择网卡处有过滤器，可以下拉选择，举2个例子：  
1. 只捕获端口80的流量: `port 80`
2. 只捕获1.2.3.4 ip的流量: `host 1.2.3.4`


2017/9/2  
