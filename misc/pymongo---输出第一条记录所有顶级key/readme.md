# pymongo---输出第一条记录所有顶级key

```python

# coding:utf8         

from pymongo import MongoClient

conn = MongoClient('127.0.0.1', 27017)
print conn.database_names()
db = conn.hello
print db.collection_names()
collection = db.analysis
x = collection.find().limit(1)
for i in x:
    print i.keys()

```


2018/8/16  
