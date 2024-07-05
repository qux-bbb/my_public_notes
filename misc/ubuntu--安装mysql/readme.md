# ubuntu--安装mysql

```r
sudo apt install mysql-server
sudo apt install mysql-client 
sudo apt install libmysqlclient-dev
```

简单写下安装后怎么用，刚开始安装后，需要用root用户登录，root密码默认为空  
```r
sudo mysql -uroot -p
```

登录之后，可以创建一个新数据库，这里指定编码utf8  
```r
create database if not exists your_database default charset utf8 collate utf8_general_ci;
```

然后创建一个新用户，如果想远程访问，可以把'localhost'改成'%'  
```r
create user 'your_name'@'localhost' identified by 'your_pass';
```

最后把新数据库的所有权限给这个新用户，@后的内容不能省略  
```r
grant all privileges on your_database.* to 'your_name'@'localhost';
```

新版本的MySQL还需要修改配置才能远程访问  
编辑 /etc/mysql/mysql.conf.d/mysqld.cnf, 将 `bind-address          = 127.0.0.1` 的 `127.0.0.1` 改为 `0.0.0.0`，重启mysql服务  


2020/12/19  
