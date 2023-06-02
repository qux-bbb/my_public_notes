# python---bson解析

```python
# !/usr/bin/python
# coding:utf8

import sys
import bson
import struct

filename = sys.argv[1]

bson_file = open(filename, 'r')
while True:
    data = bson_file.read(4)
    if not data or len(data) != 4:
        exit(0)
    blen = struct.unpack("I", data)[0]
    data += bson_file.read(blen-4)
    if len(data) < blen:
        exit(0)
    if 'loads' in dir(bson):
        bson_content = bson.loads(data)  # windows
    else:
        bson_content = bson.BSON(data).decode()  # linux
    print bson_content
```


2018/9/9  
