# fabric

Fabric是一个高级Python（2.7,3.4+）库，可以远程执行shell命令，返回有用python对象。  
它是在Invoke（子处理命令执行和命令行功能）和paramiko（SSH协议实现）上构建的，通过扩展其API以提供更多功能。  

官网: http://www.fabfile.org/

简单示例：  
```python
>>> from fabric import Connection
>>> result = Connection('web1.example.com').run('uname -s', hide=True)
>>> msg = "Ran {0.command!r} on {0.connection.host}, got stdout:\n{0.stdout}"
>>> print(msg.format(result))
Ran 'uname -s' on web1.example.com, got stdout:
Linux
```


这个链接写了挺多场景下的代码: https://my.oschina.net/u/4051725/blog/3167801  


2021/4/20  
