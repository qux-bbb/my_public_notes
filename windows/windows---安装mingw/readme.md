# windows---安装mingw

MinGW，Minimalist GNU for Windows，是用于原生 Microsoft Windows 应用程序的简约开发环境。  

下载：  
https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/installer/mingw-w64-install.exe/download  
下载的文件名是： mingw-w64-install.exe  

我选择安装到 `D:\mingw-w64` 文件夹下  

其他我的选项：  
```
Version: 8.1.0
Architecture: x86_64
Threads: win32
Exception: seh
Build revision: 0
```

最后可以把 bin 文件夹路径添加到 path，我的路径是：  
```
D:\mingw-w64\x86_64-8.1.0-win32-seh-rt_v6-rev0\mingw64\bin
```


参考：  
https://code.visualstudio.com/docs/cpp/config-mingw  


2020/6/12  
