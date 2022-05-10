# ListRDPConnections

https://github.com/Heart-Sky/ListRDPConnections  

读取本机对外RDP连接记录和其他主机对该主机的连接记录。  

其他主机对该主机的连接记录，原理是读取事件查看器里的日志：  
```r
应用程序和服务日志->Microsoft->Windows->TerminalServices-LocalSessionManager->Operational
EventID: 21 登录成功
EventID: 25 重新连接
21和25作为成功日志

应用程序和服务日志->Microsoft->Windows->TerminalServices-RemoteConnectionManager->Operational
EventID: 1149 网络连接
除去21和25相应日志，作为失败日志
```


2022/5/10  
