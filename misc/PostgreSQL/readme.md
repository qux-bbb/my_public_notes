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
# 列出所有库
\l
# 查看当前连接库
\c
# 连接到指定库
\c <database_name>
# 列出tables、views、sequences信息
\d
# 查看表详细信息，参数是表名
\d <table_name>
# 查看表数据
SELECT * FROM table_name;
# 退出psql
\q
```


菜鸟教程: https://www.runoob.com/postgresql/postgresql-tutorial.html  


2022/8/1  
