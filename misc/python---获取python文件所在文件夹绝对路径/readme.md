# python---获取python文件所在文件夹绝对路径

keywords: 项目 根目录 脚本路径 脚本文件夹路径  

```python
current_py_dir = os.path.dirname(os.path.abspath(__file__)) + '/'
```

`__file__` 指当前文件  
`os.path.abspath()` 获取绝对路径  
`os.path.dirname()` 获取文件所在文件夹  

如果只使用`os.path.dirname(__file__)`，只能返回相对路径，有时候拼接路径就容易出错，比如当前文件夹就会返回空字符串  


2020/6/15  
