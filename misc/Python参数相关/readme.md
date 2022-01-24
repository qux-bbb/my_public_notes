# Python参数相关

keywords: 传参限制  

## 实参类型顺序
Python实参分为两类：`positional argument` 和 `keyword argument`，在传参时要保证 `positional argument` 在 `keyword argument` 之前。例如：  
```python
def func(x, y, z):
   pass

func(1, y=2, z=3) # 正确传参
func(x=1, y=2, 3) # SyntaxError: positional argument follows keyword argument
func(1, y=2, 3)   # SyntaxError: positional argument follows keyword argument
```

## 可变参数：*args, **kwargs
Python函数传参时将多余的 `positional argument` 存放在 `args` 中，将多余的 `keyword argument` 存放在 `kwargs `中，函数内部使用时 `args` 为tuple， `kwargs` 为dict。例如：  
```python
def func(x, y, *args, **kwargs):
    print("x: " + str(x))
    print("y: " + str(y))
    print("args: ")
    for item in args:
        print(item)
    print("kwargs: ")
    for key, value in kwargs.items():
        print("{}: {}".format(key, value))

func(1, 2, 3, 4, 5, key1=6, key2=7)

# output:
# x: 1
# y: 2
# args: 
# 3
# 4
# 5
# kwargs: 
# key1: 6
# key2: 7
```

示例2：  
```python
# coding:utf8

def foo(*args, **kwargs):
    print(args, type(args))
    print(kwargs, type(kwargs))

foo(1, 2, a='hello', b='world')

'''
(1, 2) <class 'tuple'>
{'a': 'hello', 'b': 'world'} <class 'dict'>
'''
```


原链接：https://zhuanlan.zhihu.com/p/81044523  


2020/12/10  
