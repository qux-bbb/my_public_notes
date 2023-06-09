# python2---json.dump汉字存为unicode

使用json.dump时，汉字会存为unicode，这是一种解决方法  

```python
# coding:utf8

import codecs
import json

origin_data = open('hello.json', 'r').read()
items = json.loads(origin_data)

using_items = []

for item in items:
    if item['used'] == 1:
        using_items.append(item)

with codecs.open('hello_used.json', 'w', encoding='utf-8') as f:
    json.dump(using_items, f, ensure_ascii=False,  indent=4)

print 'Done!'

```


2018/1/5  
