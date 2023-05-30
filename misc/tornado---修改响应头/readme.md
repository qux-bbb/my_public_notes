# tornado---修改响应头

keywords: response header  

可以修改，但需要在每个get或者post方法写一行  
```python
self.set_header('Server', 'HelloWorld')
```

太麻烦了，故不做修改  


2018/8/20  
