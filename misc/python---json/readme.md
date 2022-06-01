# python---json

json主要是4个方法  

json.load: 从文件对象读取  
json.dump: 写入到文件对象  

json.loads: 从字符串加载  
json.dumps: 转为字符串  


示例  
```python
# coding:utf8

import json

a_dict = {
    "hello": "world", 
    "good": "morning", 
    "number": 1
}

with open("test.json", "w") as f:
    json.dump(a_dict, f, indent=4)

with open("test.json", "r") as f:
    a_json = json.load(f)
    print(a_json)


with open("test.json", "r") as f:
    a_str = f.read()
    a_json = json.loads(a_str)
    print(a_json)

a_str = json.dumps(a_json, indent=4)
print(a_str)

```


2018/12/1  
