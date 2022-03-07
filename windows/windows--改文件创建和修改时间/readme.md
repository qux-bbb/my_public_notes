# windows--改文件创建和修改时间

使用bat脚本调用powershell  
```r
@ECHO OFF
powershell.exe -command "ls 'a_file.txt' | foreach-object { $_.LastWriteTime = '01/11/1997 22:13:36'; $_.CreationTime = '01/11/1996 22:13:36' }"
PAUSE
```

来源：https://blog.csdn.net/u012223913/article/details/72123906  


2019/7/12  
