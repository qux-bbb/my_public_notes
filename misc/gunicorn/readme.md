# gunicorn

## 简介
官网：https://gunicorn.org/  

Gunicorn 'Green Unicorn' 是一个适用于UNIX的Python WSGI HTTP Server。它使用提前fork的工作模式，Gunicorn服务器与各种Web框架广泛兼容，实现简单，占用服务器资源少且速度非常快。  

安装：`pip install gunicorn`  


## 官方示例
myapp.py  
```python
def app(environ, start_response):
    data = b"Hello, World!\n"
    start_response("200 OK", [
        ("Content-Type", "text/plain"),
        ("Content-Length", str(len(data)))
    ])
    return iter([data])
```

执行命令：`gunicorn -w 4 myapp:app`  
启动4个工作进程执行app函数  


---
2020/10/12  
