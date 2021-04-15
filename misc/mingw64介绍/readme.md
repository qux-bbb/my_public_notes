# MinGW-w64介绍
## 简介
MinGW，Minimalist GNU for Windows，是用于原生 Microsoft Windows 应用程序的简约开发环境，没找到官网。  
MinGW-w64是支持生成64位程序的MinGW，官网: http://mingw-w64.org/doku.php  

sourceforge地址：  
https://sourceforge.net/projects/mingw/  
https://sourceforge.net/projects/mingw-w64/  


## linux使用
这里用的发行版是Ubuntu  
安装编译工具:  
```sh
sudo apt install mingw-w64
```

生成exe:  
```sh
# pe32
i686-w64-mingw32-gcc -m32 -o hello_x86.exe hello.c

# pe32+
x86_64-w64-mingw32-gcc -m64 -o hello_x64.exe hello.c
```


## windows使用
下载在线安装包：  
`https://sourceforge.net/projects/mingw-w64/files/Toolchains targetting Win32/Personal Builds/mingw-builds/installer/mingw-w64-install.exe`  
分别安装x86_64和i686版本的，Threads选择win32，其它选项默认即可  

如果下载在线安装太慢，在这里 https://sourceforge.net/projects/mingw-w64/files/ 下载2个压缩包，解压放到相应文件夹中  
```
https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win64/Personal%20Builds/mingw-builds/8.1.0/threads-win32/seh/x86_64-8.1.0-release-win32-seh-rt_v6-rev0.7z
https://sourceforge.net/projects/mingw-w64/files/Toolchains%20targetting%20Win32/Personal%20Builds/mingw-builds/7.3.0/threads-win32/sjlj/i686-7.3.0-release-win32-sjlj-rt_v5-rev0.7z
```
外网会快很多  

安装之后，将相关路径加入path，我加了这2个：  
```
D:\mingw-w64\mingw64\bin
D:\mingw-w64\mingw32\bin
```

生成exe和上面一致  
