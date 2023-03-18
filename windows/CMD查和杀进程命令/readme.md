# CMD查和杀进程命令

```r
# 查看进程
tasklist
# 查看服务相关的进程
tasklist /svc
# 结束进程，以 进程ID 结束
taskkill /pid 1 /T /F
# 结束进程，以 进程名 结束
taskkill /im notepad.exe /T /F
# /T = 以树形结束所有子进程
# /F = 强制结束
```

原链接: http://www.ln10086.net/jswz/shownews.php?lang=cn&id=19  


2016/7/12  
