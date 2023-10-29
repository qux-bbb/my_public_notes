# python3---AES加解密

pycrypto已经不维护了，python3安装会出问题，所以安装pycryptodome  
```r
pip install pycryptodome
```

从pycrypto抄的python2示例：  
```python
>>> from Crypto.Cipher import AES
>>> obj = AES.new('This is a key123', AES.MODE_CBC, 'This is1 an IV456')
>>> message = "The answer is no"
>>> ciphertext = obj.encrypt(message)
>>> ciphertext
'\xd6\x83\x8dd!VT\x92\xaa`A\x05\xe0\x9b\x8b\xf1'
>>> obj2 = AES.new('This is a key123', AES.MODE_CBC, 'This is an IV456')
>>> obj2.decrypt(ciphertext)
'The answer is no'
```
对同一内容连续用2次obj产生结果不同，因为密钥流发生了变化  

整理一下：  
```python
from Crypto.Cipher import AES

message = b'The answer is no'

obj = AES.new(b'This is a key123', AES.MODE_CBC, b'This is an IV456')
ciphertext = obj.encrypt(message)
print(ciphertext)

obj2 = AES.new(b'This is a key123', AES.MODE_CBC, b'This is an IV456')
plaintext = obj2.decrypt(ciphertext)
print(plaintext)

'''
b'\xd6\x83\x8dd!VT\x92\xaa`A\x05\xe0\x9b\x8b\xf1'
b'The answer is no'
'''
```


链接: https://pypi.org/project/pycrypto/  


---
2020/4/21  
