# win7安装python3

python官网显示python3.9以上已不支持win7，所以找一下python3.8  
```r
Note that Python 3.9+ cannot be used on Windows 7 or earlier.
```

python3.8提供安装包的版本只到python3.8.10  
```r
# https://www.python.org/downloads/release/python-3816/
Python 3.8.10 was the last full bugfix release of Python 3.8 with binary installers.
```

从这里下载相应安装包：  
https://www.python.org/downloads/release/python-3810/  

安装日志显示需要安装KB2533623补丁：  
```log
[09D4:09E4][2023-02-23T08:03:25]e000: Detected Windows 7 SP1 without KB2533623
[09D4:09E4][2023-02-23T08:03:25]e000: KB2533623 update is required to continue.
```

实测该补丁不适用于win7，偶然发现安装火绒后可以安装python3，发现安装了KB4474419补丁，测试确定安装该补丁重启系统后就可以安装pyhton3  
https://www.catalog.update.microsoft.com/Search.aspx?q=4474419  

https://catalog.s.download.windowsupdate.com/c/msdownload/update/software/secu/2019/09/windows6.1-kb4474419-v3-x64_b5614c6cea5cb4e198717789633dca16308ef79c.msu  


2023/2/23  
