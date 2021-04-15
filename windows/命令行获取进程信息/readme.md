# 命令行获取进程信息

keywords: windows 进程列表 参数  

获取进程列表：  
```cmd
tasklist
```

获取进程的命令行参数：  
```cmd
wmic process where caption="python.exe" get caption,commandline /value
```

原链接: https://www.qiansw.com/windows-get-commendline.html  
