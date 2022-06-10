# 写驱动程序

## 简介
按照这个流程走：  
https://docs.microsoft.com/zh-cn/windows-hardware/drivers/gettingstarted/writing-your-first-driver  


## 安装工具
1. [Microsoft Visual Studio](https://go.microsoft.com/fwlink/p/?LinkId=698539)
2. [Windows SDK](https://developer.microsoft.com/windows/downloads/windows-10-sdk)
3. [Windows Driver Kit (WDK)](https://go.microsoft.com/fwlink/p/?LinkId=733614)

每个都下载安装最新版的即可，其它的按流程走好了  

可能会遇到 Spectre-缓解库 缺失问题，解决方法：  
```r
工具 -> 获取工具和功能
切换到"单个组件"，向下翻到已经勾选的  
"MSVC v142 - VS 2019 C++ x64/x86 生成工具(v14.28)"  
上面会有一个对应的  
"MSVC v142 - VS 2019 C++ x64/x86 Spectre 缓解库(v14.28)"  
勾选之后安装即可  

可能版本会有差异，是这个对应关系就可以  
```


## 一些缩写
UMDF, User Mode Driver Framework, 用户模式驱动程序框架  
KMDF, Kernel Mode Driver Framework, 内核模式驱动程序框架  
PnP, Plug and Play, 即插即用  


---
2020/11/30  
