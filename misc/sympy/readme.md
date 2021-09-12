# sympy

Symphy是一个用于符号数学的Python库。  

官网: https://www.sympy.org/en/index.html  
官方文档: https://docs.sympy.org/latest/index.html  

安装: `pip install sympy`  

解一元二次方程：  
```python
# coding:utf8

from sympy import *

x = Symbol('x')
result = solve(x**2 - 9, x)

print(result)

# [-3, 3]
```

解多元一次方程：  
```python
# coding:utf8

from sympy import *

x, y = symbols('x,y')
f0 = x + y - 4
f1 = x - y - 2

result = solve([f0, f1])

print(result)

# {x: 3, y: 1}
```


2021/9/12  
