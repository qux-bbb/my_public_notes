# 事件查看器

日志位置：  
```r
%SystemRoot%\System32\Winevt\Logs\
```

Windows的事件查看器可以查看各种日志，对应的可执行程序是 eventvwr.exe。  
相应的命令行工具为 wevtutil.exe，功能较少，过滤不方便。  

可以筛选一个时间段内的日志  

可以把日志导出为各种格式，支持的有: evtx/xml/txt/csv  
导出的csv用excel查看很方便，可以各种筛选，行高可以调整成一行的高度，查看更方便。  
用EvtxECmd转换的csv日志会拆分出更多属性，可能更好看一些。  

可以通过事件ID筛选某种类型的日志，一些事件ID如下：  
```r
# 应用程序和服务日志->Microsoft->Windows->TerminalServices-LocalSessionManager->Operational
# 21和25作为成功日志
21 登录成功
25 重新连接成功

# 应用程序和服务日志->Microsoft->Windows->TerminalServices-RemoteConnectionManager->Operational
# 除去21和25相应日志，作为失败日志
1149 网络连接

# Windows日志->安全
4624 登录成功  # 对于win7，远程登陆的LogonType是10，进程名是C:\Windows\System32\winlogon.exe，可以看到连接ip地址和端口
              # 对于win10，远程登录的LogonType(可能是2/3/5/7)和进程名不确定，可以看到连接ip地址，看不到端口
4625 登录失败


# Windows日志->系统
6005 开机
6006 关机
```
https://ponderthebits.com/2018/02/windows-rdp-related-event-logs-identification-tracking-and-investigation/  
https://jpcertcc.github.io/ToolAnalysisResultSheet/details/mstsc.htm  


安全日志快速参考：  
```r
# User Account Changes
4720 Created
4726 Deleted

# Logon Session Events
# 4624和4627可以通过 Logon ID 关联
4624 Successful logon
4647 User initiated logooff
4625 Logon failure (See Logon Failure Codes)
4778 Remote desktop session reconnected
4779 Remote desktop session disconnected
4800 Workstation locked
4801 Workstation unlocked
4802 Screen saver invoked
4803 Screen saver dismissed

# Logon Types
2   Interactive
3   Network (i.e. mapped drive)
4   Batch (i.e. schedule task)
5   Service (service startup)
7   Unlock (i.e. unnattended workstation with password protected screen saver)
8   Network Cleartext (Most often indicates a logon to IIS with “basic authentication”)
10  Remote Desktop
11 Logon with cached credentials

# Logon Failure Codes
0xC0000064  User name does not exist
0xC000006A  User name is correct but the password is wrong
0xC0000234  User is currently locked out
0xC0000072  Account is currently disabled
0xC000006F  User tried to logon outside his day of week or time of day restrictions
0xC0000070  Workstation restriction
0xC00000193 Account expiration
0xC0000071  Expired password
0xC0000133  Clocks between DC and other computer too far out of sync
0xC0000224  User is required to change password at next logon
0xC0000225  Evidently a bug in Windows and not a risk
0xC000015b  The user has not been granted the requested logon type (aka logon right) at this machine
```
https://www.ultimatewindowssecurity.com/securitylog/quickref/default.aspx  
https://www.ultimatewindowssecurity.com/securitylog/quickref/downloads/quickref.zip  


完整的事件ID描述列表：  
https://www.ultimatewindowssecurity.com/securitylog/encyclopedia  


2021/7/9  
