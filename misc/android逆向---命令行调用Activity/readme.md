# android逆向---命令行调用Activity

keywords: 执行 运行  

```r
adb shell am start -n "com.kbtx.redpack_simple/.FlagActivity"
# 或者用这个命令
am start-activity "com.kbtx.redpack_simple/.FlagActivity"

# am, Activity manager, 可以管理Activity、Service等组件，直接执行 am 可以查看帮助信息
```

参考链接: https://www.52pojie.cn/forum.php?mod=viewthread&tid=1893531  


2024/5/19  
