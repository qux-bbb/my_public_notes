# RSA---n分解攻击1

题目给出public.key, flag.enc  

如果n较小，可以尝试分解n来进行攻击  

```python
# coding:utf8

"""
需要安装2个模块：rsa，pycrypto
如果有问题，应该把之前安装的crypto、pycrypto模块卸载掉重新安装一遍
还需要使用 yafu 分解n
"""

import rsa
from Crypto.PublicKey import RSA

def egcd(a, b):
  if a == 0:
    return (b, 0, 1)
  else:
    g, y, x = egcd(b % a, a)
    return (g, x - (b // a) * y, y)


pub = RSA.importKey(open('pub.key').read())
n = long(pub.n)
e = long(pub.e)

########################################################################################
# 通过yafu分解n,命令行打开yafu,输入factor(n)即可
# 如果可联网，还可以使用http://www.factordb.com/网站分解   
# p = 28596...
# q = 30400...

if not p or not q:
    print 'Need get p,q'
    exit(0)

d = egcd((p - 1) * (q - 1), e)[2]
if d < 0:
    d += (p - 1) * (q - 1)


key = RSA.construct((n, e, d))    # 如果e较小，e应转化成long型: e = long(e)
key.exportKey()
open("private.pem", "w").write(key.exportKey())


p = open("private.pem").read()
privkey = rsa.PrivateKey.load_pkcs1(p)
crypto = open("flag.enc").read()
message = rsa.decrypt(crypto, privkey)
print message

```


2018/6/1  
