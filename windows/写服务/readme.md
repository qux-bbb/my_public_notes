# 写服务

## 1 简介
Windows 上的 服务 可以在系统启动时由用户通过“服务”控制面板小程序或使用服务功能的应用程序自动启动。即使没有用户登录到系统，服务也可以执行。  

官方关于服务的文档：  
https://docs.microsoft.com/zh-cn/windows/win32/services/services  

SCM, Service Control Manager, 服务控制管理器  


## 2 官方示例抄写
看官方文档抄一个简单的服务吧。  
使用IDE：VS2019  

### 2.1 构建sample.dll
参照链接：https://docs.microsoft.com/zh-cn/windows/win32/services/sample-mc  

sample.dll可以提供日志输出，该dll生成无需IDE。  

sample.mc内容见：[files/sources/sample.mc](files/sources/sample.mc)  

需要找到mc.exe，rc.exe，link.exe，我想构建的是64位系统下的x86程序，所以选了这3个：  
```
"D:\Windows Kits\10\bin\10.0.19041.0\x86\mc.exe"
"D:\Windows Kits\10\bin\10.0.19041.0\x86\rc.exe"
"D:\Program Files (x86)\Microsoft Visual Studio\2019\Community\VC\Tools\MSVC\14.28.29333\bin\Hostx64\x86\link.exe"
```
官方提供原始命令为：  
```
mc -U sample.mc
rc -r sample.rc
link -dll -noentry -out:sample.dll sample.res
```
把mc、rc、link换成上面具体的路径，执行完命令，就得到sample.dll了    

### 2.2 构建Svc.exe
参照链接：  
头文件：https://docs.microsoft.com/en-us/windows/win32/services/writing-a-service-program-s-main-function  
cpp文件：https://docs.microsoft.com/zh-cn/windows/win32/services/svc-cpp  

Svc.exe是一个简单的服务示例，这里使用VS2019构建。  

Sample.h内容见：[files/sources/Sample.h](files/sources/Sample.h)  
Svc.cpp内容见：[files/sources/Svc.cpp](files/sources/Svc.cpp)  

将Sample.h和Svc.cpp内容准备好，然后解决方案配置为：Release x86，生成解决方案即可  
Svc.exe可以在类似这样的路径下找到：D:\files\vs2019\sources\Svc\Release  

### 2.3 构建SvcConfig.exe
参照链接：https://docs.microsoft.com/zh-cn/windows/win32/services/svcconfig-cpp  

SvcConfig.exe是一个服务配置程序，这里使用VS2019构建。  

SvcConfig.cpp内容见：[files/sources/SvcConfig.cpp](files/sources/SvcConfig.cpp)  

将SvcConfig.cpp内容准备好，然后解决方案配置为：Release x86，生成解决方案即可  
SvcConfig.exe可以在类似这样的路径下找到：D:\files\vs2019\sources\SvcConfig\Release  

### 2.4 构建SvcControl.exe
参照链接：https://docs.microsoft.com/zh-cn/windows/win32/services/svccontrol-cpp  

SvcControl.exe是一个服务控制程序，这里使用VS2019构建。  

SvcControl.cpp内容见：[files/sources/SvcControl.cpp](files/sources/SvcControl.cpp)  

将SvcControl.cpp内容准备好，然后解决方案配置为：Release x86，生成解决方案即可  
SvcControl.exe可以在类似这样的路径下找到：D:\files\vs2019\sources\SvcControl\Release  

### 2.5 部署并测试
参照链接：https://docs.microsoft.com/zh-cn/windows/win32/services/the-complete-service-sample  

将上述步骤生成的sample.dll、Svc.exe、SvcConfig.exe、SvcControl.exe放在同一文件夹下，这里放在了：C:\Users\hello\Desktop  

首先配置Sample.dll相关的注册表项：  
for_sample.reg如下，双击执行即可：  
```reg
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Services\EventLog\Application\SvcName]

"TypesSupported"=dword:00000007
"EventMessageFile"="‪C:\\Users\\hello\\Desktop\\sample.dll"
```

然后Win+R，输入`services.msc`，打开服务窗口用于观察（每执行一条命令，就F5刷新观察变化，当服务安装后，可单击选中服务然后按F5，这样刷新比较快）  

接着管理员权限打开命令行窗口，做如下操作测试：  
安装服务：  
```
svc install
```
启动服务：  
```
svccontrol start SvcName
```
更新服务描述：  
```
svcconfig describe SvcName
```
查看服务配置：  
```
svcconfig query SvcName
```
修改服务DACL：  
```
svccontrol dacl SvcName
```
禁用服务：  
```
svcconfig disable SvcName
```
启用服务（非启动）：  
```
svcconfig enable SvcName
```
停止服务：  
```
svccontrol stop SvcName
```


## 3 让Svc.exe写文件
官方示例中的Svc.exe没有实质的动作，我们给它加一个写文件的操作，有点真实的感觉  
Svc_modified.cpp内容见：[files/sources/Svc_modified.cpp](files/sources/Svc_modified.cpp)  


## 4 调试服务
服务的主体程序不能像普通程序那样直接调试，官方给了一些调试方法，可参照链接：  
https://docs.microsoft.com/zh-cn/windows/win32/services/debugging-a-service  
总结为：  
1. 使用调试器附加运行中的服务进程（适用于重复运行且运行不影响后续调试的情况）
2. 使用DebugBreak来调用调试器（适用于自己写程序的情况）
3. 通过注册表项设置镜像劫持（看起来简单且效果最好，但在Windows Vista之后已不可用）
4. 使用Event Tracing记录信息（适用于自己写程序的情况）

对逆向来说，一种可行的方法：  
把关键位置改成无限循环（EB FE），然后windbg去附加。附加后在无限循环处下断点，断下后改回原来的内容，继续调试即可。  


## 未解决问题
&&&&&&& 看《恶意代码分析实战》说可以让服务不在任务管理器中作为一个进程显示出来，还不知道怎么实现。  