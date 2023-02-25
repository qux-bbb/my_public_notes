# htaccess解析上传的其他后缀文件

在网站目录下增加名为".htaccess"的文件，内容如下，即可将hello.jpg的内容解析为php  

```r
<FilesMatch "hello.jpg">
SetHandler application/x-httpd-php
</FilesMatch>
```


参考：https://blog.csdn.net/c465869935/article/details/51800354  


2018/6/21  
