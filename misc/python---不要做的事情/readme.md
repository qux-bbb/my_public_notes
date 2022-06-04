# python---不要做的事情

绝对不要在迭代的时候修改迭代对象, 会有不好想的问题出现  

```python
# coding:utf8

aa = [1, 2, 3]

for a in aa:
    if a == 2:
        aa.remove(a)
print(aa)
```

2020/1/3  
