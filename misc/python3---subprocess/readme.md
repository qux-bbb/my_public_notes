# python3---subprocess

keywords: 执行命令  

https://docs.python.org/3/library/subprocess.html  

subprocess.run 阻塞型  
```python
import subprocess

result1 = subprocess.run(["echo", "hello"])  # doesn't capture output
print("result1: ", result1.returncode, result1.stdout)

result2 = subprocess.run(["echo", "hello"], capture_output=True)
print("result2: ", result2.returncode, result2.stdout)

'''
hello
result1:  0 None
result2:  0 b'hello\n'
'''
```

subprocess.Popen 非阻塞型  
```python
import subprocess

p = subprocess.Popen(["echo", "hello"])
# 可以使用 p.wait() 等待子进程结束再执行后面的语句
```


2022/8/15  
