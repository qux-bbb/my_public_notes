# MongoDB相关

官网: https://www.mongodb.com/  
官方文档: https://www.mongodb.com/docs/manual/  

一个非关系型数据库  


## linux使用
安装
```r
sudo apt-get install mongodb
```

如果失败，可以参考这些链接安装：  
https://techviewleo.com/install-mongodb-on-ubuntu-linux/  
https://www.mongodb.com/docs/manual/administration/install-on-linux/  


简单命令
```r
# 进入mongodb shell
# 原来命令是"mongo"，在5.0废弃了
# https://www.helenjoscott.com/2022/01/29/mongod-mongo-mongosh-mongos-what-now/
mongosh

# 帮助
help

# 显示所有数据库
show dbs

# 选择数据库
use the_db

# 显示表
show collections

# 表查询例子，加pretty()可以更好地显示
db.analysis.find({"_id":ObjectId("5b73d70dfa9e3c651ecc2d25")}).pretty()

# 退出
exit
```


## python使用
python有一个pymongo模块  
pypi地址: https://pypi.org/project/pymongo/  
官方文档: https://pymongo.readthedocs.io/en/stable/  
github地址: https://github.com/mongodb/mongo-python-driver  

安装  
```r
pip install pymongo
```

使用示例  
```python
# coding:utf8
# python3

import pymongo

myclient = pymongo.MongoClient('127.0.0.1', 27017)

# 获取所有数据库名
database_names = myclient.list_database_names()
print('database_names: {}'.format(database_names))

my_db = myclient['test_db']

my_col = my_db['article']
# 清空集合
my_col.drop()

the_article = {'title': 'hello', 'content': 'Hello World!'}
# 插入1条数据
my_col.insert_one(the_article)

# 查找1条数据
hello_article_find = my_col.find_one({'title': 'hello'})
print('hello_article_find: {}'.format(hello_article_find))

myclient.close()
```

参考链接: https://www.runoob.com/python3/python-mongodb.html  


## Compass
Compass 是一款免费的图形化跨平台交互式工具，用于查询、优化和分析 MongoDB 数据。  

地址: https://www.mongodb.com/products/tools/compass  
