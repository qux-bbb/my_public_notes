# powershell---下载文件

```powershell
$src = 'https://www.pstips.net/index.php'
$des = "index.php"
Invoke-WebRequest -uri $src -OutFile $des
Unblock-File $des
```

最后一条命令是解锁文件使可执行  

原链接: https://www.pstips.net/powershell-download-files.html  


2019/7/28  
