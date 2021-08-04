# MEMORY.DMP

Windows在蓝屏崩溃时，可以生成MEMORY.DMP  
默认路径为: `%SystemRoot%\MEMORY.DMP`，一般是 `C:\Windows\MEMORY.DMP`  

可以设置dump文件的类型：  
1. 无(表示不生成)
2. 小内存转储(256 KB)
3. 核心内存转储
4. 完全内存转储

第4种默认不显示，需要使用Notmyfault工具这样设置: `notmyfault.exe /setdumptype full`  

使用Notmyfault工具产生蓝屏错误: `notmyfault.exe /crash`  

&&&&&&& 如果使用Notmyfault工具产生蓝屏，生成memory.dmp，在使用Volatility进行取证(pslist)或使用Windbg查看崩溃信息时，可以看到明显的notmyfault痕迹。应该有其它方式造成崩溃，需要补充  


2021/8/4  
