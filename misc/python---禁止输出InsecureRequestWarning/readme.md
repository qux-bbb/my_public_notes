# python---禁止输出InsecureRequestWarning

使用requests时，如果指定 `verify=False`，运行时会输出 `InsecureRequestWarning` 警告，这是urllib3的警告，可以设置禁止输出。  
```python
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
```


2023/4/18  
