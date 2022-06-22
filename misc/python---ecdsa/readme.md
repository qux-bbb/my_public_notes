# python---ecdsa

ecdsa库主要提供了椭圆曲线形式的数字签名和密钥协商功能。  
该库未考虑安全性，仅作为测试和教学工具，生产建议使用 [cryptography](https://cryptography.io/).  

ECDSA, Elliptic Curve Digital Signature Algorithm, 椭圆曲线数字签名算法  
ECDH, Elliptic Curve Diffie-Hellman, 椭圆曲线Diffie-Hellman密钥协商，生成共享密钥  

安装：  
```r
pip install ecdsa
# 如需更高性能可以继续安装gmpy2
# pip install gmpy2
```

签名验证示例：  
```python
from ecdsa import SigningKey
sk = SigningKey.generate() # uses NIST192p
vk = sk.verifying_key
signature = sk.sign(b"message")
assert vk.verify(signature, b"message")
```


参考链接: https://github.com/tlsfuzzer/python-ecdsa  


2022/6/23  
