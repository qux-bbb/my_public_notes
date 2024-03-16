# github公钥相关

放在github上的公钥用于免密认证  


通过这个地址可以看到相应用户在github存储的公钥：  
```r
https://github.com/<github account name>.keys  
```


在这里可以看到每个公钥的SHA256信息：  
https://github.com/settings/keys  


SHA256信息计算方式：  
```python
import base64
from hashlib import sha256

public_key = "AAAAB..."
tmp1 = base64.b64decode(public_key)
tmp2 = sha256(tmp1).digest()
result = base64.b64encode(tmp2).strip(b"=")
print(result)
```


2024/3/16  
