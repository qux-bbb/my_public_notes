# python---中途有一次输入的自动化交互

```python
# coding:utf8

import subprocess

pname = 'C:/Users/11476/Desktop/Repwn.exe'
input = '20101001X1Y0uN3tG00dHaCk'

p = subprocess.Popen(pname, stdin=subprocess.PIPE, stdout=subprocess.PIPE)
result = p.communicate(input=input)
print(result)
```

可以用在需要按任意键结束的场景：  
```python
import subprocess

p = subprocess.Popen(
    ["de4dot/de4dot.exe", "test.py"],
    stdin=subprocess.PIPE,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)
p.communicate(input=b"a")
p.wait()
print("hello")
```

参考：https://jingyan.baidu.com/article/e52e361578d8c540c60c513a.html  


2019/4/7  
