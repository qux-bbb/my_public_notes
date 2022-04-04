# 事件查看器

Windows的事件查看器可以查看各种日志，对应的可执行程序是 eventvwr.exe  

可以筛选一个时间段内的日志  

可以通过事件ID筛选某种类型的日志，一些事件ID如下：  
```r
# Windows日志->安全
4624 登录成功  # 对于win7，远程登陆的LogonType是10，进程名是C:\Windows\System32\winlogon.exe，可以看到连接ip地址和端口
              # 对于win10，远程登录的LogonType(可能是2/3/5/7)和进程名不确定，可以看到连接ip地址，看不到端口
4625 登录失败

# Windows日志->系统
6005 开机
6006 关机
```

完整的事件ID描述列表：  
https://www.ultimatewindowssecurity.com/securitylog/encyclopedia  

可以把日志导出为各种格式，支持的有: evtx/xml/txt/csv  


2021/7/9  
