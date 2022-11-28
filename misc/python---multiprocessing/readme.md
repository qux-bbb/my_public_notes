# python---multiprocessing

keywords: 多进程  

multiprocessing，进程并行模块  

## Pool
使用Pool并行处理数据  
```python
# python3

from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(5) as p:
        print(p.map(f, [1, 2, 3]))
```


## Process
类似threading模块的使用方法  

```python
# python3

from multiprocessing import Process

def f(name):
    print('hello', name)

if __name__ == '__main__':
    process_list = []
    for name in ['Alice', 'Bob']:
        p = Process(target=f, args=(name,))
        process_list.append(p)
    for p in process_list:
        p.start()
    for p in process_list:
        p.join()
```


## 进程间同步
使用锁确保进程间同步，执行完一个再执行另一个  

```python
from multiprocessing import Process, Lock


def f(lock, i):
    lock.acquire()
    try:
        print("hello world", i)
        print("hello world", i)
    finally:
        lock.release()


if __name__ == "__main__":
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()
```

错误情况：  
```r
RuntimeError: Lock objects should only be shared between processes through inheritance
```
解决方法：  
```r
from multiprocessing import Manager

lock = Manager.lock()
...
lock.acquire()
...
lock.release()
```
解决方法原链接: https://zhuanlan.zhihu.com/p/22223656  


---
参考链接: https://docs.python.org/zh-cn/3/library/multiprocessing.html  
