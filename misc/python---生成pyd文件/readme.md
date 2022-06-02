# python---生成pyd文件

安装 Cython  
```r
pip install cython
```

准备两个文件  
test.py  
```python
#coding:utf-8
def hello():
    print("Hello world")
    input("<press ENTER to quit>")
```

setup.py  
```python
from distutils.core import setup
from Cython.Build import cythonize
 
setup(
  name = 'Hello world app',
  ext_modules = cythonize("test.py"),
)
```

执行以下命令生成 pyd 文件  
```r
python setup.py build_ext --inplace
```

pyd文件可以像平常一样 import 使用  

原链接：http://yshblog.com/blog/117  


2020/7/11  
