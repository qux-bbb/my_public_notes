# python2---lambda表达式

## 官方资料

官方链接: https://docs.python.org/2.7/tutorial/controlflow.html#lambda-expressions  

Small anonymous functions can be created with the `lambda` keyword. This function returns the sum of its two arguments: `lambda a, b: a+b`. Lambda functions can be used wherever function objects are required. They are syntactically restricted to a single expression. Semantically, they are just syntactic sugar for a normal function definition. Like nested function definitions, lambda functions can reference variables from the containing scope:  

```r
>>> def make_incrementor(n):
...     return lambda x: x + n
...
>>> f = make_incrementor(42)
>>> f(0)
42
>>> f(1)
43
```
The above example uses a lambda expression to return a function. Another use is to pass a small function as an argument:  

```r
>>> pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
>>> pairs.sort(key=lambda pair: pair[1])
>>> pairs
[(4, 'four'), (1, 'one'), (3, 'three'), (2, 'two')]
```

## 简单翻译
lambda表达式可以用来创建小的匿名函数, 举例如:  
`lambda a, b: a+b`  
类似:  
```python
def hello(a, b):
    return a+b
```


---
2020/2/5  
