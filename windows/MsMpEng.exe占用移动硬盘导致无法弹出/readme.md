# MsMpEng.exe占用移动硬盘导致无法弹出

keywords: win10 移动硬盘无法弹出  

就是这个东西  
`\Device\HarddiskVolume3\ProgramData\Microsoft\Windows Defender\Platform\4.18.2011.6-0\MsMpEng.exe`   
 
 事件查看器里的消息是：  
 ```r
 进程 ID 为 5096 的应用程序 \Device\HarddiskVolume3\ProgramData\Microsoft\Windows Defender\Platform\4.18.2011.6-0\MsMpEng.exe 已停止删除或弹出设备 USB\VID_1058&PID_2626\575851324537304637345045。
 ```
 
 详细信息是：  
 ```r
+ System 
  - Provider 
    [ Name]  Microsoft-Windows-Kernel-PnP 
    ...
 - EventData 
  ProcessId 5096 
  ProcessNameLength 97 
  ProcessName \Device\HarddiskVolume3\ProgramData\Microsoft\Windows Defender\Platform\4.18.2011.6-0\MsMpEng.exe 
  DeviceInstanceLength 46 
  DeviceInstance USB\VID_1058&PID_2626\575851324537304637345045 
 ```
 
是通过"来源"列的 Kernel-PnP 类型找到的  
 
上面的意思就是说 MsMpEng.exe 在扫描我们的移动硬盘，它是 windows defender的一部分，感觉它设计有问题，不知道什么原因。  
别人给出的解决方法是装一个别的安全软件，然后上面那个进程就会自动关掉了，这个时候用安全软件带的弹出硬盘就没问题了。  
我装了火绒。  


参考链接：https://www.zhihu.com/question/396194052  


---
2020/12/8  
