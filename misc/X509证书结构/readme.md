# X509证书结构

```
keywords: X.509 证书

X509证书信息

维基百科：
https://en.wikipedia.org/wiki/X.509
https://zh.wikipedia.org/wiki/X.509

标准字段结构如下

Certificate
    Version Number
    Serial Number
    Signature Algorithm ID
    Issuer Name
    Validity period
        Not Before
        Not After
    Subject name
    Subject Public Key Info
        Public Key Algorithm
        Subject Public Key
    Issuer Unique Identifier (optional)
    Subject Unique Identifier (optional)
    Extensions (optional)
        ...
Certificate Signature Algorithm
Certificate Signature

证书
    版本号
    序列号
    签名算法ID
    颁发者
    有效期
        起始日期
        截至日期
    使用者
    使用者公钥信息
        公钥算法
        使用者公钥
    颁发者唯一ID (可选)
    使用者唯一ID (可选)
    扩展(可选)
        ...
证书签名算法
数字签名(指纹)


证书实例举例
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            04:00:00:00:00:01:44:4e:f0:42:47
        Signature Algorithm: sha256WithRSAEncryption
        Issuer: C=BE, O=GlobalSign nv-sa, OU=Root CA, CN=GlobalSign Root CA
        Validity
            Not Before: Feb 20 10:00:00 2014 GMT
            Not After : Feb 20 10:00:00 2024 GMT
        Subject: C=BE, O=GlobalSign nv-sa, CN=GlobalSign Organization Validation CA - SHA256 - G2
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:c7:0e:6c:3f:23:93:7f:cc:70:a5:9d:20:c3:0e:
                    ...
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Key Usage: critical
                Certificate Sign, CRL Sign
            X509v3 Basic Constraints: critical
                CA:TRUE, pathlen:0
            X509v3 Subject Key Identifier:
                96:DE:61:F1:BD:1C:16:29:53:1C:C0:CC:7D:3B:83:00:40:E6:1A:7C
            X509v3 Certificate Policies:
                Policy: X509v3 Any Policy
                  CPS: https://www.globalsign.com/repository/

            X509v3 CRL Distribution Points:

                Full Name:
                  URI:http://crl.globalsign.net/root.crl

            Authority Information Access:
                OCSP - URI:http://ocsp.globalsign.com/rootr1

            X509v3 Authority Key Identifier:
                keyid:60:7B:66:1A:45:0D:97:CA:89:50:2F:7D:04:CD:34:A8:FF:FC:FD:4B

    Signature Algorithm: sha256WithRSAEncryption
         46:2a:ee:5e:bd:ae:01:60:37:31:11:86:71:74:b6:46:49:c8:
         ...


其他
由特定CA颁发的每个证书，序列号必须是唯一的

OID   OBJECT IDENTIFIER   对象标识符
可在该网站查看 http://oidref.com/
使用方法举例: http://oidref.com/1.2.840.113549.1.7.1

SPC   Software Publisher Certificate   软件发行者证书


补充: X509相关RFC文档
https://tools.ietf.org/html/rfc5280
https://tools.ietf.org/html/rfc2459
```


2018/11/20  
