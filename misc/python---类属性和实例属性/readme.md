# python---类属性和实例属性

```python
# coding:utf8

class Test(object):
    # 类属性
    a = 100

    def __init__(self, b):
        # 实例属性
        self.b = b


t = Test(100)

# 通过实例化对象访问 类属性
print("t.a = %d" % t.a)

# 通过类名访问 类属性
print("Test.a = %d" % Test.a)

# 通过实例化对象访问 实例属性
print("t.b = %d" % t.b)

# 通过类名访问 实例属性
print("Test.b = %d" % Test.b)  # error 无法通过（类名.属性名）的方式访问实例属性
```

类属性可以通过实例化对象、类名访问  
实例属性只能通过实例化对象访问  


原链接: https://blog.csdn.net/Leo_Coding/article/details/72935271  


2018/10/19  
