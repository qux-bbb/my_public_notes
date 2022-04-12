# ubuntu---mysql问题解决

**问题：**  
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)  
**解决：**  
可能 mysql-server 没安装，装一下  
```r
sudo apt install mysql-server
```
也可能mysql服务没起，启动一下  
```r
sudo service mysql start
```

**问题：**  
2003, "Can't connect to MySQL server  
**解决：**  
编辑该文件 /etc/mysql/mysql.conf.d/mysqld.cnf  
```r
bind-address        = 0.0.0.0
```
把 `127.0.0.1` 改成 `0.0.0.0`，重启服务  
```r
sudo service mysql restart
```


参考链接：  
1. https://stackoverflow.com/questions/11657829/error-2002-hy000-cant-connect-to-local-mysql-server-through-socket-var-run
2. https://www.digitalocean.com/community/questions/connect-error-2003-can-t-connect-to-mysql-server-on-111  


20200526  
20201215 增加服务没起的情况  


2020/12/15  
