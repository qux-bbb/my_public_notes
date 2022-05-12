# sqlite相关

官网: https://www.sqlite.org/  

打开数据库  
```r
sqlite3 test.db
```

查看表  
```r
.table
```

查看建表语句  
```r
.schema   查看建表语句
```

退出(二选一)  
```r
.exit
.quit
```

获取表字段  
```r
PRAGMA table_info('tablename');
```

python查看sqlite数据库  
```python
#导入SQLite驱动：
import sqlite3
#连接到SQlite数据库
#数据库文件是test.db，不存在，则自动创建
conn = sqlite3.connect('Login Data')
#创建一个cursor：
cursor = conn.cursor()
#执行查询语句：
cursor.execute('select password_value from logins')
#使用featchall获得结果集（list）
values = cursor.fetchall()
print(values[0][0].hex()) 
#关闭cursor
#关闭conn
cursor.close()
conn.close()
```

python查看表是否存在  
```python
conn = sqlite3.connect(db_path)
c = conn.cursor()
records = c.execute('''SELECT name FROM sqlite_master WHERE type='table' and name='fn';''').fetchall()
if records:
    print(records)
else:
    print('Nothing!!!')
conn.commit()
conn.close()
```


2019/12/22  
