## 0x01 Concept & Goals
SQL注入概念和课程目标  
字符型注入、数字型注入  


## 0x02 What is SQL
说明SQL特点，没有标准版本，各厂商实现不同且有自身特性  
SQL :: Structured Query Language :: 结构化查询语言 包括数据操纵、定义、控制  


## 0x03 What is SQL Injection?
对数据库做出非预期操作，达到增删改查敏感数据的目的  


## 0x04 Consequences of SQL Injection
后果就是对数据影响呀，可小可大  
常见于php、asp、cold fusion等  


## 0x05 Severity of SQL Injection
看情况呗  


## 0x06 Example of SQL Injection
```
userName = Smith' or '1'='1

userName =' or 1=1 --

userID = 1234567 or 1=1

UserName = Smith';drop table users; truncate audit_log;--
```


## 0x07 Try It! String SQL Injection
相关SQL语句代码为：  
```
"select * from users where LAST_NAME = "'" + userName + "'";
```
输入 1' or '1'='1  
回车即可  


## 0x08 Try It! Numeric SQL Injection
相关SQL语句代码为：  
```
"select * from users where USERID = "  + userID;
```
输入 1 or 1=1  
回车即可  