# python---enumerate

enumerate, 枚举, 在python里可以同时取list的下标和值  

```python
aa = ['hello', 'world', 'good', 'bad']

print(enumerate(aa))
for i, v in enumerate(aa):
    print(i, v)
```
输出：  
```r
<enumerate object at 0x0000000002792D18>
0 hello
1 world
2 good
3 bad
```


参考链接: https://www.runoob.com/python/python-func-enumerate.html  


2021/11/27  
