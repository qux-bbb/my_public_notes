# python---捕获异常并输出完整信息

有异常，不想raise，想看到全部信息  

```python
# coding:utf8

import traceback

try:
    a = 1 / 0
except Exception as e:
    print(traceback.format_exc())
```

输出：  
```r
Traceback (most recent call last):
  File "test.py", line 6, in <module>
    a = 1 / 0
ZeroDivisionError: division by zero
```


2018/11/24  
