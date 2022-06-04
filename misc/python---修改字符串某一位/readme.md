# python---修改字符串某一位

尝试修改string的值（导致“TypeError: 'str' object does not support item assignment”）  
string是一种不可变的数据类型，该错误发生在如下代码中：  
```python
spam = 'I have a pet cat.' 
spam[13] = 'r' 
print(spam) 
```

而你实际应该这样做，代码如下：  
```python
spam = 'I have a pet cat.'
spam = spam[:13] + 'r' + spam[14:]
print(spam)
```


原链接: https://www.jb51.net/article/31014.htm  


2017/3/1  
