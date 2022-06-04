# python--引用其他py文件的函数

有两种实现的方法，第一种有2个小的方法，第2个小方法比较正式  

## 添加`__init.py__`
**说明**   
在想引用的文件所在目录下和想执行的py目录下，新建一个文件： `__init.py__`，即可通过 相对路径的方式引用  
**方法1**    
目录如下：
```r
py_test/
├── a
│   ├── a.py
│   └── __init__.py
├── b
│   ├── b.py
│   └── __init__.py
└── __init__.py
```

a.py内容：  
```python
# coding:utf8
def a():
    print("I am a")
```
b.py内容：  
```python
# coding:utf8
from ..a import a
a.a()
```
其他文件为空  
和py_test同目录，执行命令：  
```r
python -m py_test.b.b
```
即可调用a.py中的函数  

**方法2**  
方法1的缺点是只能在那个路径下执行命令，如果不想使用方法1，就只能把b.py中的代码封装成一个函数，在py_test文件夹下新建c.py，通过c.py来调用b.py中封装的函数，这是比较正式的做法  
目录如下：  
```r
py_test
├── a
│   ├── a.py
│   └── __init__.py
├── b
│   ├── b.py
│   └── __init__.py
└── c.py
```
a.py内容：  
```python
# coding:utf8

def a():
    print("I am a")
```
b.py内容：  
```python
# coding:utf8

from a.a import a

def b():
    print("I am b!")
    a()
```
c.py内容：  
```python
# coding:utf8

from b.b import b

b()
```
其他文件为空，举例在py_test下执行命令：  
```r
python c.py
```
即可正常执行  


## sys添加路径
**说明**  
将想要用的文件所在目录path添加到系统路径，即可引用  
主要形式如下：  
```python
import sys
sys.path.append(path)
```
使用以上形式需要注意使用绝对路径，而且需要注意操作系统导致的路径差异  


---
2017/11/29  
