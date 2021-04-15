# python网站开发部署使用软件关系

```
Django/Flask/Tornado --> uwsgi/gunicorn --> nginx/apache
```

原生python用python框架就行了  
uwsgi/gunicorn来加速, 高并发用uwsgi更好  
nginx做负载均衡  


supervisor可以用来监控原生python进程, 使进程非正常停止后仍能够重启  

相关文档:  
https://uwsgi-docs.readthedocs.io/en/latest/index.html  
http://docs.gunicorn.org/en/stable/  
http://supervisord.org/  


2019/12/04  
