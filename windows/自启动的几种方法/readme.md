# 自启动的几种方法

在windows下，可以通过一些方式实现程序自启动  
使用SysinternalsSuite套件中的Autoruns.exe可以查看所有自启动项，这里列举其中一些  

## StartUp文件夹
### winxp
```r
C:\Documents and Settings\Administrator\「开始」菜单\程序\启动
```

### win7 win10
用户级自启动文件夹，可以使用Win+R输入`shell:Startup`打开
```r
C:\Users\<User>\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup
```
也可以使用该路径: `%appdata%\Microsoft\Windows\Start Menu\Programs\Startup`

系统级自启动文件夹，可以使用Win+R输入`shell:Common Startup`打开
```r
C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup
```

## 各种注册表项自启动  
下面是常见的注册表项，大概操作就是右键新建REG_SZ类型的键，名字随便取，值设为程序的绝对路径就好了
```r
HKEY_CURRENT_USER\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Run
HKEY_LOCAL_MACHINE\SOFTWARE\Wow6432Node\Microsoft\Windows\CurrentVersion\Run
```

## 任务计划程序
win+R，输入: `taskschd.msc`, 回车可以打开任务计划程序，可以设置可执行程序的启动时间和频率  
设置的任务计划会以文件的形式存到`C:\Windows\System32\Tasks`文件夹下，文件名为任务计划名称  
`schtasks.exe`是命令行程序，可以查看、创建、删除任务计划等  

## 自启动服务
win+R，输入: `services.msc`, 回车可以打开服务列表，在这里可以设置已有任务的运行状态和启动类型  
`sc.exe`是用来与服务控制管理器和服务进行通信的命令行程序，可以查看、创建、删除服务  

## 可能的注意点
如果实在找不到自启动项了，可能是持续被其它机器攻击  
