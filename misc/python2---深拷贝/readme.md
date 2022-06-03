# python2---深拷贝(深复制)

一些数据结构使用复制的方式还会有原来的引用, 需要使用深拷贝的方式复制一个全新的, 这样就可以随便改了  

```python
import copy

tmp_aa = copy.deepcopy(aa)
```

2020/2/5  
