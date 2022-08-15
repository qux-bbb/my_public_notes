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
超级好看  

github地址: https://github.com/Textualize/rich  
官方文档: https://rich.readthedocs.io/en/stable/introduction.html  

简单的rich例子1  
```python
import time
from rich.progress import track

for i in track(range(20), description="Processing..."):
    time.sleep(1)  # Simulate work being done
```

简单的rich例子2  
```python
import time

from rich.progress import Progress

with Progress() as progress:

    task1 = progress.add_task("[red]Downloading...", total=1000)
    task2 = progress.add_task("[green]Processing...", total=1000)
    task3 = progress.add_task("[cyan]Cooking...", total=1000)

    while not progress.finished:
        progress.update(task1, advance=0.5)
        progress.update(task2, advance=0.3)
        progress.update(task3, advance=0.9)
        time.sleep(0.02)
```


原链接：  
1. https://www.cnblogs.com/huma/p/12198386.html  
2. https://zhuanlan.zhihu.com/p/145568973  


2020/7/17  
