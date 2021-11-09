# python---base64

python2：  
```python
import base64
encoded = base64.b64encode('hello')
decoded = base64.b64decode(encoded)
```

python3：  
```python
import base64
encoded = base64.b64encode('hello'.encode('utf8'))
decoded = base64.b64decode(encoded)
```

除了 `b64`，还有 `b32` `b16`  


2018/5/31  
