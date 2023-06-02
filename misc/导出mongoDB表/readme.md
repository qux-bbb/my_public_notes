# 导出mongoDB表

## 使用脚本

```python
# coding:utf8

from pymongo import MongoClient

conn = MongoClient('1.2.3.4', 27017)

db = conn.waf
my_coll = db.log

log = open("log", 'w')

for i in my_coll.find():
    print(i)
    log.write(i + "\n")

log.close()
print("[+] Done!")

```

## 使用mongoexport
```bash
mongoexport -h 127.0.0.1 -d waf -c log -q '{"time":{$gte:1513094400}}' -f "name,message,url" -o ./log
```


---
2017/12/14  
