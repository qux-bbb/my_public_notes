# edb

keywords: linux 调试器  

edb is a cross platform AArch32/x86/x86-64 debugger. It was inspired by Ollydbg, but aims to function on AArch32, x86, and x86-64 as well as multiple OS's. Linux is the only officially supported platform at the moment, but FreeBSD, OpenBSD, OSX and Windows ports are underway with varying degrees of functionality.  

github地址: https://github.com/eteran/edb-debugger  

安装：  
```r
sudo apt install edb-debugger
```

ubuntu22下，`save file` 会卡死，可以这样启动规避：  
```r
XDG_CURRENT_DESKTOP=kde edb
```
相关链接: https://github.com/eteran/edb-debugger/issues/809  

不是太好用，Cutter更好用一些  


2021/4/12  
2021/4/20 增加安装方式  
