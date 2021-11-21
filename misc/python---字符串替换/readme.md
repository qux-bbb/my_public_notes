# python---字符串替换

替换有两种方法：  
1. replace
2. re.sub

第1种直接替换，第2种可以用正则表达式，具体看下面例子  

```python
#coding:utf8

import re

str1 = "world,worid"

# repalce替换
print(str1.replace("world", "hello"))
# sub替换
print(re.sub(r"wor.d", "hello", str1))
```

2017/9/11  
