# python---写六位数字字典

```python
the_file = open("a.txt", "w")

for i in range(999999 + 1):
    the_file.write("%06d\n" % i)

the_file.close()
```


2016/6/26  
