# 任务计划

keywords: 计划任务  

任务计划，可以定时执行一些命令，启动程序  

Win+R，输入 `taskschd.msc` 回车，即可查看所有任务计划  

win10下，在这两个注册表项下存有相关信息：  
```r
计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree
计算机\HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tasks
```

任务计划还可以使用schtasks命令操作，允许管理员创建、删除、查询、更改、运行和中止本地或远程系统上的计划任务。  
举个例子：  
```bat
:: 创建任务计划"My App"，执行myapp.exe，从03/01/2002开始执行第一次，后续每5个小时执行一次
schtasks /create /sc hourly /mo 5 /sd 03/01/2002 /tn My App /tr c:\apps\myapp.exe
```
更多用法可以在命令行执行 `schtasks /?` 查看  
或者参考该链接: https://docs.microsoft.com/en-us/windows-server/administration/windows-commands/schtasks  

隐藏任务计划  
打开该注册表项下具体任务计划的注册表项，修改Index为0，删除SD，可以隐藏计划任务  
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows NT\CurrentVersion\Schedule\TaskCache\Tree  
详见: https://cloud.tencent.com/developer/article/2377196  
