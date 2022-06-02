# python---命令行输出结构美化

python自带模块 pprint  

```python
from pprint import pprint

hello = {
    "a": 1,
    "b": "xx",
    "c": {"m": "mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm", "n": "nn"},
    "d": {
        "x": "xx",
        "y": "yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy",
        "z": "zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz",
    },
}

pprint(hello)
```
输出：  
```r
{'a': 1,
 'b': 'xx',
 'c': {'m': 'mmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmmm', 'n': 'nn'},
 'd': {'x': 'xx',
       'y': 'yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy',
       'z': 'zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz'}}
```


2020/8/26  
