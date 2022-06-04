# python---通过函数名字符串调用函数

```python
# coding:utf8


class Test:
    def hello(self):
        return "Hello"

    def world(self):
        return "World"

    def dispatch(self, func_name):
        fn = getattr(self, func_name, None)
        response = fn()
        return response


test = Test()
print(test.dispatch("world"))
```


2018/8/20  
