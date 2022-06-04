# python---dict键值交换

```python
my_dict = {'a':'A','b':'B','c':'C'}
new_dict = {v:k for k, v in my_dict.items()}
print(my_dict)
print(new_dict)

'''
{'a': 'A', 'b': 'B', 'c': 'C'}
{'A': 'a', 'B': 'b', 'C': 'c'}
'''
```


原链接: https://blog.csdn.net/cain/article/details/6575177  


2016/5/30  
