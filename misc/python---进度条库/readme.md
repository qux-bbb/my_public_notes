# python---进度条库

## `tqdm`
```python
from time import sleep
from tqdm import tqdm
 
for i in tqdm(range(20)):
    sleep(0.5)
```
windows 下会乱  

## `progressbar`
```python
import time
from progressbar import *
 
progress = ProgressBar()
for i in progress(range(1000)):
    time.sleep(0.01)
```
样式简洁  


## `rich`
```python
from rich.progress import track
import  time

for step in track(range(30)):
    time.sleep(0.5)
```
rich 超级好看  

简单的rich例子  
```python
# coding:utf8

import time
from rich.progress import track


class Test:
    a = 0
    def add_and_sleep(self, total):
        while self.a < total:
            # 这里可以写具体的逻辑
            # 用 a 值当作进度
            time.sleep(0.1)
            yield self.a
            self.a += 1


    def show_progress(self):
        total = 100
        for step in track(self.add_and_sleep(total), total=total):
            _ = 1

Test().show_progress()
```


原链接：  
1. https://www.cnblogs.com/huma/p/12198386.html  
2. https://zhuanlan.zhihu.com/p/145568973  


2020/7/17  
