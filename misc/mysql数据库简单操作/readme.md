# mysql数据库简单操作

基本操作  
```r
mysql -u root -p    # 登陆，linux上root账户登录需要root权限
show databases;     # 显示所有数据库名
use mysql;          # 选择名为mysql的数据库
show tables;        # 显示所选数据库中所有表名
desc hello_table;   # 显示指定的表结构
```

创建数据库  
```r
create database hello;  # 建立数据库
create database if not exists your_database default charset utf8 collate utf8_general_ci;  # 指定编码
```

删除数据库  
```r
drop database if exists your_database;
```

按降序排列  
```r
select * from world order by day desc;
```

mysql设置任意数据库远程访问  
```r
create user 'your_name'@'%' identified by 'your_pass';
grant all privileges on *.* to 'your_name'@'%';
flush privileges;
# 如果是云主机，还需要打开3306端口
```

模糊查询  
```r
select a, b from m_table where a like "%hello%";
```

过滤NULL  
```r
... where ** is NULL
... where ** is not NULL
```

更新某字段值  
```r
update table_name set column_name="hello";
```


2017/2/16  
