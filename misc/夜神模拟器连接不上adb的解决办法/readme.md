# 夜神模拟器连接不上adb的解决办法

打开cmd运行命令：  
```r
adb connect 127.0.0.1:62001
```

若还是提示无法连接到127.0.0.1:62001，打开cmd，运行命令：  
```r
tasklist
```

找到NoxVMHandle.exe对应的PID，然后运行命令：  
```r
# 假设NoxVMHandle.exe对应的PID为5912
netstat -ano | findstr 5912
```

找到127.0.0.1:62xxx的地址，这里有：127.0.0.1:62026  

运行命令：  
```r
adb connect 127.0.0.1:62026
```
即可连接成功  


原链接: https://www.jianshu.com/p/6041e64518a8  


2020/5/20  
