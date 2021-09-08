# z3求解器

github地址: https://github.com/Z3Prover/z3  
pypi地址: https://pypi.org/project/z3-solver/  

教程: http://ericpony.github.io/z3py-tutorial/guide-examples.htm  

pip安装命令  
```sh
pip install z3-solver
```


简单使用  
```python
# coding:utf8

from z3 import *

a = Int('a_some')
b = Int('b_other')

s = Solver()
s.add(a + b == 4)
if s.check() == sat:
    print(s.model())

```

z3 结果的成员转整型：  
```
print(s.model()[a].as_long())
```


打印所有可能结果：  
```python
# coding:utf8
# https://stackoverflow.com/questions/13395391/z3-finding-all-satisfying-models
from z3 import *

a = Int('a_some')
b = Int('b_other')

s = Solver()
s.add(a + b == 4)
s.add(a > 0)
s.add(b > 0)
while s.check() == sat:
    print(s.model())
    # prevent next model from using the same assignment as a previous model
    s.add(Or(a != s.model()[a], b != s.model()[b]))
```


其他小片段  
```python
# 32位长度的无符号变量，可做位操作
a = BitVec('a', 32)

# 32位长度的无符号常量
b = BitVecVal(10, 32)

# 作比较
a = BitVecVal(-10, 32)
b = BitVecVal(-10, 32)
print(eq(a, b))

# list
X = [ Int('x%s' % i) for i in range(5) ]
```


循环左移  
```python
# coding:utf8

from z3 import *

x=BitVec('x', 32)
s = Solver()
s.add(RotateLeft(x, 8) == 0x8cc2c5a8)

if s.check() == sat:
    print(s.model())
```


2020/7/31  
