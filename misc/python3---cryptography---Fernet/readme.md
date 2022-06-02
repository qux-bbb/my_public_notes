# python3---cryptography---Fernet

安装模块：  
```r
pip install cryptography
```

Fernet 是一个已经封装好的对称加密类，只需要提供 32 位长度的 key 即可进行加解密，内部是 AES 的 CBC 模式，PKCS7 填充，iv 随加密消息传递  

示例：  
```python
>>> from cryptography.fernet import Fernet
>>> key = Fernet.generate_key()
>>> f = Fernet(key)
>>> token = f.encrypt(b"my deep dark secret")
>>> token
b'...'
>>> f.decrypt(token)
b'my deep dark secret'
```

key 有格式要求：  
key (bytes) – A URL-safe base64-encoded 32-byte key. This must be kept secret. Anyone with this key is able to create and read messages.  

原 key 长度是 32，然后需要经过一种 base64 编码，`generate_key()` 的源码：  
```python
@classmethod
def generate_key(cls):
    return base64.urlsafe_b64encode(os.urandom(32))
```


**Using passwords with Fernet**  
```python
>>> import base64
>>> import os
>>> from cryptography.fernet import Fernet
>>> from cryptography.hazmat.backends import default_backend
>>> from cryptography.hazmat.primitives import hashes
>>> from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
>>> password = b"password"
>>> salt = os.urandom(16)
>>> kdf = PBKDF2HMAC(
...     algorithm=hashes.SHA256(),
...     length=32,
...     salt=salt,
...     iterations=100000,
...     backend=default_backend()
... )
>>> key = base64.urlsafe_b64encode(kdf.derive(password))
>>> f = Fernet(key)
>>> token = f.encrypt(b"Secret message!")
>>> token
b'...'
>>> f.decrypt(token)
b'Secret message!'
```


2020/5/7  
