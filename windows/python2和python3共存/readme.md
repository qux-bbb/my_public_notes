# python2和python3共存

windows上同时安装python2和python3，直接用python执行命令可能会搞不清楚用了哪个版本，这时可以用py.exe来执行命令。  
```r
# 指定python2
py -2 hello.py
# 指定python3
py -3 hello.py
```

使用不同版本的pip：  
```r
# 指定python2，通过模块使用
py -2 -m pip install requests
# 指定python3，通过模块使用
py -3 -m pip install requests
```

参考链接: https://www.zhihu.com/question/21653286/answer/95532074  


2016/10/22  
