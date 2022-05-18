# adb端口转发

设置端口转发  
```r
# 主机端口 6100 到设备端口 7100 的转发
adb forward tcp:6100 tcp:7100
```

查看端口转发列表  
```r
adb forward --list
```

删除端口转发  
```r
adb forward --remove tcp:23946
```


参考链接: https://developer.android.google.cn/studio/command-line/adb#forwardports  


2020/8/4  
