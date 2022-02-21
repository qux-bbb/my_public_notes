# pyinstaller生成exe在win7下显示丢失dll

keywords:  pyinstaller api-ms-win-core-path-l1-1-0.dll  

用 python3.9 的 pyinstaller4.1 生成一个exe，在win7下显示"丢失 api-ms-win-core-path-l1-1-0.dll"，具体是：  
```r
recovery.exe - 系统错误  
无法启动此程序，因为计算机中丢失 api-ms-win-core-path-l1-1-0.dll。尝试重新安装该程序以解决此问题。  
```

从官网找到了原因: `PyInstaller works with Python 3.5—3.7`  

换成支持的python版本重新编译就好了  


2020/12/10  
