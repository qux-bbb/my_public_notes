# android逆向---Log输出寄存器值

```
    const-string v3, "SN"
    invoke-static{v3,v0}, Landroid/util/Log; -> v(Ljava/lang/String;Ljava/lang/String;)I

v0是你想要输出的寄存器
在androidkiller中添加之后保存（一定要保存）
然后用打开Android Studio，用adb安装apk文件，logcat中找Tag为SN的Log即可得到寄存器v0的值
```


2017/3/13  
