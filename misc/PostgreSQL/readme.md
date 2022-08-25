# PostgreSQL

PostgreSQL是一个开源的关系型数据库。  

官网: https://www.postgresql.org/  

ubuntu安装：  
```r
sudo apt-get -y install postgresql
```

linux下，如果想用postgres用户登录数据库，需要切换为postgres用户，然后执行psql命令进入数据库  
```r
sudo -i -u postgres
psql
```

简单用法：  
```r
# list databases
\l
# connect to new database (currently "postgres")
\c
# list tables, views, and sequences
\d
# 查看表格信息，参数是表格名
\d <tablename>
# 查看数据
SELECT * FROM table_name;
# quit psql
\q
```


菜鸟教程: https://www.runoob.com/postgresql/postgresql-tutorial.html  


2022/8/1  
