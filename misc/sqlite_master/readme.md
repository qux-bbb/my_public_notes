# sqlite_master

sqlite_master表是sqlite数据库的一个特殊表，该表定义数据库的模式  

该表结构  
```r
sqlite> .schema sqlite_master
CREATE TABLE sqlite_master (
  type text,
  name text,
  tbl_name text,
  rootpage integer,
  sql text
);
```
sql为创建一个表使用的sql语句  


原链接: https://blog.csdn.net/xingfeng0501/article/details/7804378  


2019/11/13  
