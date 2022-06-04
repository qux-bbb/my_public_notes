# python---生成器

```python
a = [x * x for x in range(10)]
b = (x * x for x in range(10))
```
如上，a是数组，b是生成器  
a会直接有10个元素  
b会在使用的时候，一边循环，一边计算  

生成器的优点就是节省空间  


2017/9/24  
