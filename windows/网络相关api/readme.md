# 网络相关api

ws2_32.dll 中的一些函数  
```
socket  创建一个套接字
bind    将一个套接字绑定到特定端口，应该在 accept 之前调用
listen  预示着一个套接字将进入监听，等待入站连接 
accept  向一个远程套接字打开一个连接，并接受连接
connect 向一个远程套接字打开一个连接，远程套接字必须在等待连接
recv    从远程套接字接收数据
send    发送数据到远程套接字
```

注意： WSAStartup 函数要在其他网络函数之前被调用，以便为这些网络库分配资源。所以在 WSAStartup下断点，断下后，网络入口应该就不远了。  

可能的连接服务器函数调用顺序  
```
socket -> connect [-> send -> recv]
```
可能的监听入站函数调用顺序  
```
socket -> bind -> listen -> accept [-> send -> recv]
```

WinINet API实现了应用层协议，这是更高一级的网络 API  
Wininet.dll 中的一些函数  
```
InternetOpen        初始化一个到互联网的连接
InternetOpenUrl     访问一个 URL
InternetReadFile    从一个来自互联网的下载文件中读取数据
```


来自：《恶意代码分析实战》  


2021/5/10  
