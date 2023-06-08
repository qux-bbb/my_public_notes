# 勒索软件思路

```
勒索软件所有者生成RSA的公私钥
RSA
public key --- pub_key
private key --- pri_key

AES key --- aes_key

pub_key放在软件中，aes_key在加密前随机生成，加密完成后使用pub_key对aes_key加密，形成aes_enc_key，发往勒索软件服务器，原来的aes_key即可删除

这样，在支付赎金之后，勒索软件所有者就能使用pri_key解密aes_enc_key，发给受害者，受害者就能解密文件了
```


2019/9/8  
