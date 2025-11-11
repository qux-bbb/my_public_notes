# Process Moniter

Process Moniter 是一个提供实时文件、注册表项、进程、网络监控的工具，在SysinternalsSuite套件中。  

相关程序为：  
```r
Procmon.exe  
Procmon64.exe  
```

windows自己对该工具的说明：  
```r
Process Monitor is an advanced monitoring tool for Windows that shows real-time file system, Registry and process/thread activity. It combines the features of two legacy Sysinternals utilities, Filemon and Regmon, and adds an extensive list of enhancements including rich and non-destructive filtering, comprehensive event properties such session IDs and user names, reliable process information, full thread stacks with integrated symbol support for each operation, simultaneous logging to a file, and much more. Its uniquely powerful features will make Process Monitor a core utility in your system troubleshooting and malware hunting toolkit.
```

可下载SysinternalsSuite套件  
https://docs.microsoft.com/zh-cn/sysinternals/downloads/sysinternals-suite  
也可单独下载procmon  
https://docs.microsoft.com/zh-cn/sysinternals/downloads/procmon  


---
win7下运行提示"unable to load process monitor device driver"  
新版本不支持win7了，可以在webarchive.org下载旧版本  
https://web.archive.org/web/20170804213208/https://download.sysinternals.com/files/ProcessMonitor.zip  
除了这个链接，还有各种版本，sysinternalssuite的其它工具旧版本也可以通过这种方式下载，在微软官网找到下载链接，去webarchive.org下载  

参考链接: https://docs.microsoft.com/en-us/answers/questions/760616/process-monitor-on-windows-7-sysinternals-system-r.html  


---
Operation可以设置这几个，再按需调整：
```r
WriteFile
SetRenameInformationFile
RegSetValue
Process Create
TCP Connect
UDP Connect
```


---
Options -> Font...  
可以修改字体大小，默认大小的字体截图不好看


---
2019/6/7  
2021/6/3  
