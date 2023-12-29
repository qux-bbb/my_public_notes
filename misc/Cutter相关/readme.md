# Cutter相关

## 简介

官网: https://cutter.re/  
github地址: https://github.com/rizinorg/cutter/  

Cutter是一个基于Rizin的图形化逆向工程框架。  
反编译还不错，可以用r2dec和Ghidra，各有特色，调试体验不太好。  
可以通过拖拽窗口自定义视图。  

支持多平台: Windows/Linux/macOS  

集成的Console没有重定向功能，在linux上暂时可以借助dd命令保存部分内存数据：  
```r
pr 32 @ 0x00006c10 | dd of=/tmp/bytes_here
```


## x64dbgcutter
https://github.com/yossizap/x64dbgcutter  
x64dbgcutter插件可以在Cutter里导入导出x64dbg符号文件  

安装方法：  
1. Edit -> Preferences -> Plugins，然后可以在窗口上方看到插件路径，点击进入  
2. 下载 x64dbgcutter.py，放到插件路径的python目录下

使用方法：  
Windows -> Plugins，选择插件执行即可  


---
20201210  
