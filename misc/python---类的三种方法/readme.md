# python---类的三种方法

1. 普通方法，或实例方法
2. 类方法
3. 静态方法

```python
class A:
    # 类属性
    explanation = "this is my program"

    # 普通方法，或实例方法
    def normal_method(self):
        print(self.explanation)

    # 类方法，可以访问类属性
    @classmethod
    def class_method(cls):
        print(cls.explanation)

    # 静态方法，不可以访问类属性
    @staticmethod
    def static_method():
        print("hello")
```

原链接: https://www.cnblogs.com/jayliu/p/9030725.html  

2019/3/28  
