# 开发调试驱动helloworld

https://learn.microsoft.com/zh-cn/windows-hardware/drivers  


## 配置开发环境
https://learn.microsoft.com/zh-cn/windows-hardware/drivers/download-the-wdk  
按照步骤依次安装Visual Studio Community、SDK、WDK  

这里的windbg界面更现代一点  
https://learn.microsoft.com/en-us/windows-hardware/drivers/debugger/  
遇到"解析应用包时出错"可参考该链接解决  
https://github.com/microsoftfeedback/WinDbg-Feedback/issues/159  


## 编译驱动
最简单代码如下：  
```c
#include <ntddk.h>

VOID UnloadDriver(PDRIVER_OBJECT DriverObject) {
    DbgPrint("Hello World Driver Unloaded\n");
}

NTSTATUS DriverEntry(PDRIVER_OBJECT DriverObject, PUNICODE_STRING RegistryPath) {
    DriverObject->DriverUnload = UnloadDriver;
    DbgPrint("Hello World Driver Loaded\n");
    return STATUS_SUCCESS;
}
```

打开Visual Studio，创建新项目，可以搜索"Empty WDM Driver"，WDM是Windows Driver Model的意思  
解决方案窗口的项目名上，鼠标右键，添加->新建项，创建文件Test.c，把上面的代码粘进去  
架构选择"x64"，菜单项选择 生成 -> 生成解决方案，会报如下错误：  
```r
严重性	代码	说明	项目	文件	行	禁止显示状态	详细信息
错误	1297	Device driver does not install on any devices, use primitive driver if this is intended.	MyDriver1	C:\Users\alice\source\repos\MyDriver1\MyDriver1\MyDriver1.inf	1		
```
在解决方案窗口找到 Driver Files -> MyDriver1.inf, 删除该文件重新编译即可  
解决方法来自: https://www.youtube.com/watch?v=Nc-uh8O989I&list=PLZ4EgN7ZCzJx2DRXTRUXRrB2njWnx1kA2&index=3  

另一个报错：  
```r
严重性	代码	说明	项目	文件	行	禁止显示状态	详细信息
错误	C2220	以下警告被视为错误	TestGenerate	C:\Users\alice\source\repos\MyDriver1\MyDriver1\Test.c	3		
警告	C4100	“RegistryPath”: 未引用的形参	MyDriver1	C:\Users\alice\source\repos\MyDriver1\MyDriver1\Test.c	7		
警告	C4100	“DriverObject”: 未引用的形参	MyDriver1	C:\Users\alice\source\repos\MyDriver1\MyDriver1\Test.c	3		
```
解决方法：  
项目 -> MyDriver1 项目 -> 配置属性 -> C/C++ -> 常规 -> 将警告视为错误，选择"否"  


## 配置调试环境
使用真机加虚拟机的模式，真机通过串口连接虚拟机。  

物理机上windbg设置  
```r
管理员权限启动
文件 -> Attach to kernel，切换到"COM"选项卡
勾选"Pipe"、"Reconnect"
Resets设为 0
Baud Rate设为 115200
Port设为 \\.\pipe\my_com "my_com"可以随便取，后面保持一致即可
点击右下"OK"，这样之后windbg就会输出两行内容等待连接
    Opened \\.\pipe\my_com
    Waiting to reconnect...
```

虚拟机设置  
```r
关机状态
控制->设置->串口->端口1
勾选"启用串口"
端口模式选择"主机管道"
取消勾选"连接至现有通道或套接字"
路径/地址填"\\.\pipe\my_com"

开机
cmd管理员模式下执行两条命令，这里的debugport对应上面的"端口1"：
bcdedit /debug on
bcdedit /dbgsettings serial debugport:1 baudrate:115200

重启，如果调试器连接成功，虚机右下角会出现"测试模式"，调试器内会输出"Connected to"之类的信息
```

win11虚机安全引导报错和解决方法  
```r
win11执行"bcdedit /debug on"报错：
尝试修改调试程序设置时出错。
该值受安全引导策略保护，无法进行修改或删除。

解决方法：
设置->Windows更新->更多选项->高级选项->其他选项->恢复->恢复选项->高级启动，点击"立即重新启动"
疑难解答->高级选项->UEFI固件设置，点击"重启"
Device Manager -> Secure Boot Configuration -> Attempt Secure Boot, 取消勾选，按F10保存
ESC两次选择Continue，回车即可
```

下载解压OSRLOADER供注册启动驱动使用  
https://www.osronline.com/article.cfm%5earticle=157.htm  
我用的是 WNET/AMD64/FRE 文件夹下的程序  


## 调试
### 查看调试输出
在虚机里设置如下注册表项(可以保存到.reg文件双击执行)并重启系统：  
```r
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Debug Print Filter]
"DEFAULT"=dword:0000000f
```

使用OSRLOADER注册并启动、停止驱动，可以在windbg里看到相应输出日志：  
```r
Hello World Driver Loaded
Hello World Driver Unloaded
```

参考链接: https://www.jianshu.com/p/74b6bb4bd2ed  


### 入口断点
在启动驱动前，暂停调试  

#### 如果有pdb文件
增加符号：  
文件 -> Settings -> Debugging settings -> Debugging paths -> Symbol path -> Browse... 选择pdb所在文件夹路径  
然后可以这样下断点：  
```r
# bu: breakpoint unresolved
bu MyDriver1!DriverEntry
```
继续调试，启动驱动即可断在DriverEntry  

#### 如果没有pdb文件
设置启动驱动时暂停：  
```r
# Set Exception Break Enabled, load
sxe ld MyDriver1
```
暂停后，查看目标驱动的基址：  
```r
# List Loaded Modules, module name
lm m MyDriver1
# 假设基址是 fffff807`0a400000, 注意每次启动可能不同
# 通过IDA或Ghidra等工具确定DriverEntry偏移为0x1000，则可以下断点
# breakpoints
bp fffff807`0a400000+1000
```
继续调试，即可断在DriverEntry  

来源: 文心一言  


## 参考链接补充
1. https://www.youtube.com/watch?v=XUlbYRFFYf0&list=PLZ4EgN7ZCzJx2DRXTRUXRrB2njWnx1kA2
2. https://www.youtube.com/watch?v=T5VtaP-wtkk&list=PLZ4EgN7ZCzJyUT-FmgHsW4e9BxfP-VMuo
3. chatgpt


---
2024/1/18  
