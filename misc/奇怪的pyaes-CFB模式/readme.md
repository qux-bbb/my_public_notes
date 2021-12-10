# 奇怪的pyaes-CFB模式

这个解密只能用pyaes的CFB模式来做，用pycrypto只有前2个字节是正确的，不知道为什么。  

```python
# coding:utf-8

import pyaes
import base64

key = "2e79134a9819cdc849cb98c449cecc9eca9e68ca9c1b9c059b2e99cd0ac93e9b"
IV = "0d0e0d100e0e10140e0e0e14140e0e0e"
cipher = "XclSH6nZEPVd41FsAsqeChz6Uy+HFzV8Cl9jqMyg6mMrcgSoM0vJtA1BpApYahCY"

key = bytes.fromhex(key)
IV = bytes.fromhex(IV)
cipher = base64.b64decode(cipher)

aes = pyaes.AESModeOfOperationCFB(key, iv = IV, segment_size = 16)
decrypted = aes.decrypt(cipher)
decrypted = pyaes.util.strip_PKCS7_padding(decrypted)

print(repr(decrypted))
# b'suctf{andr01d_encrypt_s0much_4un}'
```


2021/12/10  
