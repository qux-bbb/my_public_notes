# python---dict和单引号字符串互转

```python
# coding:utf8

import ast

aa = {
    "a": "hello",
    'b': 'world'
}
print(aa)

# dict 转单引号字符串
bb = str(aa)
print(bb)

# 单引号字符串转dict
cc = ast.literal_eval(bb)
print(cc)
```

如果想转双引号字符串，用json模块，json只允许双引号  


2020/9/23  
