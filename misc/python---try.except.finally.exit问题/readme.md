# python---try.except.finally.exit问题

执行exit函数，不会立刻退出, except和finally会执行完  

exit算一种异常  

脚本:  
```python
# coding:utf8
"""
@time: 2020/03/16
"""

def main():
    try:
        print('try')
        exit(0)
    except:
        print('except')
        pass
    finally:
        print('finally')


if __name__ == '__main__':
    main()
```

输出：  
```
try
except
finally
```


2020/3/17  
