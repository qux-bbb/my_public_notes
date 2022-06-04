# python---MySQLdb

安装模块：  
```r
pip install mysqlclient
```

官方文档: https://mysqlclient.readthedocs.io/user_guide.html  

如果有修改数据的操作，一定要有commit操作来保存修改  

使用示例：  
```python
# coding:utf8

import sys
import MySQLdb


if len(sys.argv) != 2:
    print 'Usage:\npython submit_result.py <result_filename>'
    exit(0)

result_filename = sys.argv[2]

result_file = open(result_filename, 'r')
result = result_file.readlines()

conn = MySQLdb.connect(host='localhost', user='hello', passwd='world', db='examples', charset='utf8')
cur = conn.cursor()

for line in result:
    example_hash, example_result = line.strip().split(' ')
    print example_hash
    cur.execute('select attr from examples where hash_value = "%s"' % example_hash)
    query_result = cur.fetchone()
    if query_result and query_result[0]:
        continue
    if query_result:
        cur.execute('update examples set attr = "%s" where hash_value = "%s"' % (example_result, example_hash))
    else:
        cur.execute('insert into examples(attr, hash_value) values ("%s", "%s")'% (example_result, example_hash))

conn.commit()
conn.close()
```

如果想获取查询所有结果，使用cur.fetchall()  


2018/11/5  
