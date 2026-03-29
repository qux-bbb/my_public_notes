# 现场排查取证溯源简单笔记

keywords: 进程id 进程路径 应急响应

尽量断网排查，避免受攻击者干扰，也避免攻击者删除痕迹跑路。

确认受影响机器的现象，用途，操作系统版本，是否有安装安全软件(看告警日志、隔离区)，是否有安全设备如防火墙、态势感知、EDR的告警，以确认排查方向。

## Windows一些技巧
把隐藏文件设置显示，已知后缀设置显示

`netstat -ano` 查看网络连接是否有异常，如有异常，用 `wmic process where processid=<PID> get executablepath` 查找对应程序路径  
(断网之后有可能就没了网络连接，但不断网又有风险，如果真要用这个方法，可以试试PsExec远程执行命令)

windows的 事件查看器（主要看登陆日志）
```r
# Windows日志->安全
4624 登录成功  # 对于win7，远程登陆的LogonType是10，进程名是C:\Windows\System32\winlogon.exe，可以看到连接ip地址和端口
              # 对于win10，远程登录的LogonType(可能是2/3/5/7)和进程名不确定，可以看到连接ip地址，看不到端口
4625 登录失败

# Windows日志->应用程序
18456 SQL Server 数据库登录失败  # 登陆成功不记录
15457 SQL Server 数据库配置变更  # 如 配置选项 'show advanced options' 已从 0 更改为 1。 | 配置选项 'xp_cmdshell' 已从 0 更改为 1
```

Autoruns，看自启动项，很好用

SysInspector，类似火绒剑，可以按风险等级过滤，很好用

如果怀疑恶意程序可能是用户自己不小心操作的，可以排查以下项：  
1. 浏览器下载记录
2. 一般下载文件夹: %USERPROFILE%\Downloads
3. 微信下载文件夹: %USERPROFILE%\Documents\WeChat Files


## 一些情况
### 被勒索
收集勒索信名称和内容，被加密文件的后缀名，大致确定加密开始和结束时间。

判断勒索家族和能否解密的网站: https://www.nomoreransom.org/

可以通过输入信息或上传文件判断是哪种勒索家族，可以查看是否能够解密。

入侵路径一般是暴力破解、漏洞利用。

### 安全设备发现外连恶意域名、IP
如果安全设备能关联到相关进程，可以查看进程路径，有可能定位到恶意进程。

如果关联不到，可以试试PsExec远程执行命令，查看进程路径。

没办法的话试试排查自启动项。

[windows---自启动的几种方法](../../windows/自启动的几种方法/readme.md)  
[linux---自启动方法](../linux---自启动方法/readme.md)

### 发现鼠标自己动、微信自动发送消息
主要排查自启动项，是否有异常项。


## 参考链接
- Windows主机入侵痕迹排查办法：https://www.freebuf.com/articles/system/255107.html
- 中毒应急处置流程1.0：https://bbs.pediy.com/thread-259725.htm
- 应急响应实战笔记 https://bypass007.github.io/Emergency-Response-Notes/
- 应急响应之Linux入侵排查 https://www.freebuf.com/vuls/255852.html
- 应急响应之Windows入侵排查 https://www.freebuf.com/vuls/255600.html

bypass007整理的内容非常全面
