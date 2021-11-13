# 服务相关

Windows的服务程序可以在系统启动时自动运行，在后台完成耗时的或不需要用户关注过程的任务。具体解释可见以下官方链接：  
https://docs.microsoft.com/zh-cn/windows/win32/services/services  


查看所有服务:  
`Win+R`, `services.msc`, 回车即可  

手动命令行添加服务:  
```r
# 注意: 等号后面要有一个空格
sc create myserver binpath= "c:\windows\Sc\myserver.exe"
sc config myserver start= auto
sc start myserver
```

在可以查看所有服务的界面只能更改服务属性而不能删除服务，查看服务属性会看到`服务名称`和`显示名称`，要想删除服务，需要用到`服务名称`  

管理员权限打开cmd，删除服务：  
```
sc delete myserver
```

有一个方便的命令行GUI设置服务工具: nssm  
网站: http://nssm.cc/  

所有的服务都可以在`HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services`注册表项下找到，这意味着可以直接设置注册表项来添加服务，重启生效，举例如下：  
```r
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\services\SvcName]
"Type"=dword:00000010
"Start"=dword:00000002
"ErrorControl"=dword:00000001
"ImagePath"=hex(2):43,00,3a,00,5c,00,55,00,73,00,65,00,72,00,73,00,5c,00,71,00,\
  5c,00,44,00,65,00,73,00,6b,00,74,00,6f,00,70,00,5c,00,53,00,76,00,63,00,2e,\
  00,65,00,78,00,65,00,00,00
"DisplayName"="SvcName"
"WOW64"=dword:00000001
"ObjectName"="LocalSystem"
```

普通的可执行程序并不适合通过服务启动, 虽然不适合启动, 但恶意软件通过白加黑的方式仍然能够实现黑文件的启动  


api  
```r
StartServiceCtrlDispatcher()
SetServiceStatus()
```

设置服务启动超时时间  
```r
HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\ServicesPipeTimeout
DWORD
60*60*24*1000=86400000
```


参考:  
1. https://zhidao.baidu.com/question/1882836776116195108.html
2. https://stackoverflow.com/questions/3582108/create-windows-service-from-executable


