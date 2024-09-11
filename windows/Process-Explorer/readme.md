# Process Explorer

keywords: 窗口定位进程 spyxx  

Process Explorer 是一个功能更强的任务管理器，在SysinternalsSuite套件中。  

在win7x64上可能会报错：  
```r
Not able to run on this version of Windows:
Missing function: winsta!WinStationConnectW
```

安装2个补丁就好了：  
KB3033929: https://www.microsoft.com/en-us/download/confirmation.aspx?id=46148  
KB2758857: https://www.microsoft.com/en-US/download/confirmation.aspx?id=35936  

最右边的黑色小圆盘图标可以用来定位窗口所属进程，和spy++功能类似。  


参考链接: https://github.com/fireeye/flare-vm/issues/246  


2021/9/21  
