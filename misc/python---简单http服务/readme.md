## 简介
python的-m选项可以直接运行模块，可以通过运行http模块提供简单的http服务  


## python2
python模块原生的http服务有:  
- BaseHTTPServer  
- SimpleHTTPServer  
- CGIHTTPServer  

可以用下面的方式启动  
```
python -m SimpleHTTPServer 8080
```


## python3
```
python -m http.server 8080
```
