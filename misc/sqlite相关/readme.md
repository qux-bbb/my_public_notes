# sqlite相关

官网: https://www.sqlite.org/  
下载页面: https://www.sqlite.org/download.html  
这里我下载了 https://www.sqlite.org/2023/sqlite-tools-win32-x86-3420000.zip  

## 一些操作
```r
# 打开数据库
sqlite3 test.db

# 建表示例
CREATE TABLE COMPANY(
   ID INT PRIMARY KEY     NOT NULL,
   NAME           TEXT    NOT NULL,
   AGE            INT     NOT NULL,
   ADDRESS        CHAR(50),
   SALARY         REAL
);

# 列出表
.table

# 列出建表语句，可指定表名
.schema

# 获取表字段
PRAGMA table_info('COMPANY');

# 退出(二选一)
.exit
.quit
```

## python操作sqlite数据库

涉及到创建、新增、修改、删除等有改动的操作，commit之后才能生效  

```python
import sqlite3

conn = sqlite3.connect("test.db")
print("数据库打开成功")

c = conn.cursor()

c.execute(
    """CREATE TABLE COMPANY
       (ID INT PRIMARY KEY     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);"""
)
conn.commit()
print("数据表创建成功")

c.execute(
    "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (1, 'Paul', 32, 'California', 20000.00 )"
)
c.execute(
    "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (2, 'Allen', 25, 'Texas', 15000.00 )"
)
c.execute(
    "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (3, 'Teddy', 23, 'Norway', 20000.00 )"
)
c.execute(
    "INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      VALUES (4, 'Mark', 25, 'Rich-Mond ', 65000.00 )"
)
conn.commit()
print("数据插入成功")

cursor = c.execute("SELECT id, name, address, salary  from COMPANY")
for row in cursor:
    print("ID = ", row[0])
    print("NAME = ", row[1])
    print("ADDRESS = ", row[2])
    print("SALARY = ", row[3], "\n")
print("数据查询成功")

conn.close()
```


## 参考链接
1. https://www.runoob.com/sqlite/sqlite-tutorial.html
2. https://www.runoob.com/sqlite/sqlite-python.html
3. https://www.runoob.com/sqlite/sqlite-python.html


---
2023/8/12  
