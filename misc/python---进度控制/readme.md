# python---进度控制

keywords: 进度显示 显示进度  

```python
# coding:utf8

import sys
import time

for i in range(100):
    time.sleep(0.05)
    sys.stdout.write('%2d%%' % i)
    sys.stdout.write("\r")
    sys.stdout.flush()
```

参考链接: https://blog.csdn.net/weixin_42555080/article/details/85705178  


2019/8/29  
