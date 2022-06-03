# python---根据字符串导入相应模块

keywords: python 动态导入

```python
import importlib

b = importlib.import_module('b')
```

简单示例  

b.py  
```python
# coding:utf8

import random


class Hello(object):
    name = ''

    def __init__(self, name):
        self.name = name

    def say_hello(self):
        print('hello, {}'.format(self.name))
    
    def say_bye(self):
        print('bye, {}'.format(self.name))
        
    def random_add(self):
        a = random.randint(10, 20)
        b = random.randint(40, 50)
        print(a+b)

```

main.py  
```python
# coding:utf8

import importlib

b = importlib.import_module('b')

hello = b.Hello('jack')
hello.say_hello()
hello.random_add()
hello.say_bye()
```


2020/1/19  
