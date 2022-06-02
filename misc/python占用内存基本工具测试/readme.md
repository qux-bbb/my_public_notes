# python占用内存基本工具测试

## memory_profiler
逐行显示变化，需要更改代码，添加装饰器  
示例测试代码如下，可以看到，函数前增加了装饰器：  
```python
@profile
def my_func():
    a = [1] * (10 ** 6)
    b = [2] * (2 * 10 ** 7)
    del b
    return a

if __name__ == '__main__':
    my_func()
```
运行命令：`python -m memory_profiler example.py`  


## Guppy-PE(heapy)
现在只知道显示基本类型的方法，需要插入代码中，示例代码如下：  
```python
# coding:utf8
from guppy import hpy

hp = hpy()

def hpy_show():
    print '#' * 40
    print hp.heap()

hpy_show()
a = 'hello'
b = ['good'] * 100
hpy_show()
```


## objgraph
可显示基本类型，需要插入代码中  
```python 
# coding:utf8
import objgraph

def obj_show():
    print '#' * 30
    objgraph.show_most_common_types()
    # objgraph.show_growth()

obj_show()
a = 'hello'
b = ['good'] * 100
obj_show()
```


## dowser
有一个例子，启动脚本后，会在指定端口启动web服务，公司有策略限制，windows下可以在浏览器看到效果，需要插入代码中  
```python
def launch_memory_usage_server(port = 80):
    import cherrypy
    import dowser

    cherrypy.tree.mount(dowser.Root())
    cherrypy.config.update({
        'environment': 'embedded',
        'server.socket_port': port
    })
                                       
    cherrypy.engine.start()

launch_memory_usage_server()
```
参考：https://stackoverflow.com/questions/110259/which-python-memory-profiler-is-recommended  
http://e-mats.org/2013/01/debugging-pythons-memory-usage-with-dowser/  


## pyrasite
使用其中的pyrasite-memory-viewer执行命令：  
```bash
pyrasite-memory-viewer <PID>
```
程序终止，错误如下：  
`Fatal Python error: This thread state must be current when releasing`  

可以用pyrasite-shell attach到一个进程  
```python
pyrasite-shell <PID>
```
attach不上msg_api进程，可以attach小的python脚本  
如果可以attach上去，就可以在不更改代码的情况下使用heapy或者objgraph来显示基本类型变化  

参考：http://pyrasite.readthedocs.io/en/latest/MemoryViewer.html  


---

python高性能编程 关于内存工具举例：  
https://m.aliyun.com/yunqi/articles/96907?spm=5176.11156381.0.0.4eeb2f95x6FZJI  


---
2020/3/9  
