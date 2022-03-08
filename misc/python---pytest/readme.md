# python---pytest

pytest好像是python比较好用的ut工具  

官网: http://pytest.org/en/latest  


## 安装
```r
pip install pytest
```


## 官方的简单例子
```python
# content of test_sample.py
def func(x):
    return x + 1


def test_answer():
    assert func(3) == 5
```

命名为`test_sample.py`, 当前目录命令行下执行pytest就好了  


## 一个类中的多个测试
```python
# content of test_class.py
class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

    def test_two(self):
        x = "hello"
        assert hasattr(x, "check")
```


## 会测试的文件/类/方法规则
只有特定名称的文件/类/方法才会被测试, 默认情况如下:  
1. 以test开头或者以test结尾的文件
2. 以Test开头的类
3. 以test开头的方法

可以通过配置文件`pytest.ini`来修改默认规则  


2020/1/20  
