# python---random

```python
# coding:utf8

import random

# 随机字符串
base_str = "0123456789abcdefghijklmnopqrstuvwxyz"
rand_str = ""
for i in range(5):
    rand_str += random.choice(base_str)
print(rand_str)

# 随机整数
rand_num = random.randint(3, 5) # [3, 5]
print(rand_num)

rand_num = random.randrange(3, 5) # [3, 5)
print(rand_num)
```


2022/5/30  
