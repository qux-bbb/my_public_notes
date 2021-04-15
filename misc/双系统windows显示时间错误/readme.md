# 双系统windows显示时间错误

如果电脑是windows和linux双系统，启动linux后，关机再启动windows，会发现时间差了好几个小时。  

Linux 认为硬件时钟中存储的时间是 UTC，而不是本地时间。  
Windows 认为硬件时钟上存储的时间是本地时间。  
这个差异导致两个系统时间解析和设置出现偏差。  


在linux下执行这条命令解决：  
```bash
timedatectl set-local-rtc 1
```

原链接: https://zhuanlan.zhihu.com/p/363140942  


2021/4/11  
