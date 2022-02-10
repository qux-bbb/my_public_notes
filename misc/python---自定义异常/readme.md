# python---自定义异常

```python
__author__ = "Burgess Zheng"
 
class BurgessError(Exception):  # Exception：所有的异常
    # 类BurgessError 继承异常Exception
    # 简单理解就是现在BurgessError和其他异常一样，是个自定义异常
    def __init__(self, msg):
        self.message = msg
 
try:
    raise BurgessError('数据库连不上')
    # ('数据库连不上')作为BurgessError异常的形参 msg = 数据库连不上
    # raise触发BurgessError异常
except BurgessError as e:  # 抓取BurgessError异常里自定义的信息
    print(e)  # 得到自定义的异常信息
#  自定义异常的名字最好不要和本身系统的异常名字一样，会导致抓取效果不一致，且又不能完全覆盖
```

原链接: https://blog.csdn.net/Burgess_zheng/article/details/85763375  


2020/1/13  
