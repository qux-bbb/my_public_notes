# 关闭ASLR功能

ASLR, Address Space Layout Randomization, 地址空间布局随机化  
该功能可以让程序加载的基址随机化，提高攻击难度，分析程序时，可以通过一些方法关闭该功能。  

## 针对单个程序
程序的ASLR功能和一个标志位有关：  
IMAGE_NT_HEADERS -> IMAGE_OPTIONAL_HEADER -> DLL Characteristics -> IMAGE_DLLCHARACTERISTICS_DYNAMIC_BASE(40)标志  

将该标志置0即可删除ASLR功能，也就是修改40为00  

可使用工具：  
1. CFF Explorer, 取消勾选"DLL can move"即可
2. XPEViewer, 取消勾选"DYNAMIC_BASE"即可

不同工具只是叫法不一样，指的是一个东西  


## 针对整个系统
通过设置注册表关闭系统的ASLR功能，程序自身即使开启了ASLR功能也不会生效。  

设置如下注册表项并重启系统：  
```r
Windows Registry Editor Version 5.00
 
[HKEY_LOCAL_MACHINE\SYSTEM\CurrentControlSet\Control\Session Manager\Memory Management]
"MoveImages"=dword:00000000
```

原链接：https://www.52pojie.cn/thread-377450-1-1.html  


---
2019/6/19  
2021/6/15  
