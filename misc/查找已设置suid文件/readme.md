# 查找已设置suid文件

查找设置了suid并且不是链接文件的文件，这样可以找到潜在可以提权的程序  
```r
find / -perm -4000 ! -type l
```

为什么是4000：  
```r
4000      Set user ID on execution
```
http://www.gnu.org/software/findutils/manual/html_mono/find.html#Numeric-Modes  


2018/6/5  
