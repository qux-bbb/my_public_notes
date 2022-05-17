# linux---查找可提权程序

```r
find / -perm -4000 ! -type l
```

为什么是4000？  
http://www.gnu.org/software/findutils/manual/html_mono/find.html#Numeric-Modes  


2020/6/17  
