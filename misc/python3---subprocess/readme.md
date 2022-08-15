# python3---subprocess

https://docs.python.org/3/library/subprocess.html  

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


2022/8/15  
