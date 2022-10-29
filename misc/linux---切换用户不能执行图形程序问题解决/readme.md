# linux---切换用户不能执行图形程序问题解决

使用su命令切换到其他用户，执行图形程序，会报如下错误：  
```r
alice@alice-machine:~$ sudo su bob
bob@alice-machine:/home/alice$ code
bob@alice-machine:/home/alice$ code --verbose
Authorization required, but no authorization protocol specified
[5331:1029/075724.593333:ERROR:ozone_platform_x11.cc(247)] Missing X server or $DISPLAY
[5331:1029/075724.593392:ERROR:env.cc(226)] The platform failed to initialize.  Exiting.
The futex facility returned an unexpected error code.
bob@alice-machine:/home/alice$ gedit
Authorization required, but no authorization protocol specified

(gedit:5357): Gtk-WARNING **: 07:57:34.725: cannot open display: :0
```

原因：  
Xserver默认情况下不允许其他用户的图形程序显示在当前屏幕上。  

解决方法：  
应以当前登陆的用户, 也就是切换身份前的用户执行如下命令：  
```r
xhost +
```

如果最后还是不想其他用户的图形程序显示在当前屏幕上，可以执行如下命令：  
```r
xhost -
```


参考链接: https://blog.csdn.net/sinat_28371057/article/details/109724576  


2022/10/29  
