# python---可以修改的项目全局变量

python的global只能作为一个文件中的全局变量，跨文件只能读取，不可修改。  

可以使用python的dict，这样的全局变量可被修改。  
```python
a = {
    'value': 'HelloWorld'
}
```

参考：https://www.cnblogs.com/suwings/p/6358061.html  


2018/11/30  
