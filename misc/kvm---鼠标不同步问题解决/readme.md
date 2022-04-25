# kvm---鼠标不同步问题解决

带右尖括号的行都是对应的命令  

列出开机的虚机  
```r
> virsh list
 Id    Name                           State
----------------------------------------------------
 301   win10_x64                      running
 302   win7_x64                       running
```

关闭出问题的虚机  
```r
> virsh shutdown win10_x64
Domain win10_x64 is being shutdown
```

修改机器配置  
把 `<input type='mouse' bus='ps2'/>` 改为 `<input type='tablet' bus='usb'/>`  
```r
> virsh edit win10_x64
Domain win10_x64 XML configuration edited.
```

启动虚机  
```r
> virsh start win10_x64
Domain win10_x64 started
```


原链接：https://blog.csdn.net/sjx1989/article/details/48375317  


2020/8/6  
