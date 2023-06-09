# CBC比特翻转攻击

将`admin=0`改成`admin=1`  
```python

from Crypto.Cipher import AES

m = 'hahahahahahahaha=1;admin=0;uid=1'
key = '1234567890abcdef'
iv = 'fedcba0987654321'
cipher = AES.new(key, AES.MODE_CBC, iv)
c = cipher.encrypt(m)
print c.encode('hex')

# 49a98685a527bdfa4077c400963a4e3c9effb4148566f10bce9e07ccbb731896
c = '49a98685a527bdfa4077c400963a4e3c9effb4148566f10bce9e07ccbb731896'.decode('hex')
# print hex(0x77 ^ ord('1') ^ ord('0')) 0x76
modify_c = '49a98685a527bdfa4076c400963a4e3c9effb4148566f10bce9e07ccbb731896'.decode('hex')

d = cipher.decrypt(modify_c)
print d

```


2019/9/13  
