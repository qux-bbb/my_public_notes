# python---multiprocessing
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


原链接: https://docs.python.org/zh-cn/3/library/multiprocessing.html  
