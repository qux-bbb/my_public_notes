# pip安装mysql-python出错

python2.7 使用pip安装mysql-python `pip install mysql-python` 出现如下错误：  
```r
_mysql.c:44:10: fatal error: my_config.h: 没有那个文件或目录
    44 | #include "my_config.h"
        |          ^~~~~~~~~~~~~
compilation terminated.
error: command 'x86_64-linux-gnu-gcc' failed with exit status 1
```

解决方法：  
```r
sudo wget https://raw.githubusercontent.com/paulfitz/mysql-connector-c/master/include/my_config.h -P /usr/include/mysql/
```

原链接：https://stackoverflow.com/questions/62087499/failing-to-install-mysql-python  


2020/12/18  
