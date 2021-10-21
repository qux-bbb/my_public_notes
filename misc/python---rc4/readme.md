# python---rc4

安装模块: `pip install pycryptodome`  

示例：  
```python
import base64
from Crypto.Cipher import ARC4

key = b'the_key'
msg = b'hello world'

cipher = ARC4.new(key)
msg_enc = cipher.encrypt(msg)
print(base64.b64encode(msg_enc))

cipher = ARC4.new(key)
msg_dec = cipher.decrypt(msg_enc)
print(msg_dec)

'''
b'595F9wWgHiYsgJE='
b'hello world'
'''
```


2021/10/21  
