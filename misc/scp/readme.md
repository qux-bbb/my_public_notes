# scp

scp, secure copy, linux相关机器之间上传下载文件。  

远程复制到本地  
```r
scp -P 2222 passcode@pwnable.kr:/home/passcode/passcode  ./passcode
```

本地复制到远程  
```r
scp -P 2222 ./a.py passcode@pwnable.kr:/home/passcode/a.py
```

直接指定密码  
```r
sshpass -p Hello scp -P 2222 passcode@pwnable.kr:/home/passcode/passcode ./passcode
```

注：  
```r
-P 指定端口
复制文件夹：scp -r -P 2222....
```
