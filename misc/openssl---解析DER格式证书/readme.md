# openssl---解析DER格式证书

```sh
openssl x509 -inform DER -in BitComet.cer -text > cert.txt
```

结果示例  
```
Certificate:
    Data:
        Version: 3 (0x2)
        Serial Number:
            4c:8d:45:fc:7c:c0:b5:84:d1:4e:16:47:fa:df:a2:b1
    Signature Algorithm: sha256WithRSAEncryption
        Issuer: C=PL, O=Unizeto Technologies S.A., OU=Certum Certification Authority, CN=Certum Code Signing CA SHA2
        Validity
            Not Before: Dec 26 06:07:11 2017 GMT
            Not After : Dec 25 06:07:11 2020 GMT
        Subject: C=CN, O=Xing Wang, L=Shanghai, CN=Xing Wang/emailAddress=wxhere@hotmail.com
        Subject Public Key Info:
            Public Key Algorithm: rsaEncryption
                Public-Key: (2048 bit)
                Modulus:
                    00:ea:bb:b5:42:7f:50:5e:62:71:2b:c1:4d:37:32:
                    5f:d2:d8:6c:bb:30:9b:46:7e:20:18:d3:9e:e4:dc:
                    3f:ce:81:c5:13:3e:22:57:9d:3e:14:83:f9:2b:16:
                    23:50:1b:5e:ca:c3:0b:4b:cc:51:2e:ca:fc:fe:4b:
                    c8:98:d9:50:f0:93:5b:c3:65:40:9d:c1:9f:c0:3d:
                    cc:a6:3c:bc:cd:07:37:75:70:bc:95:b7:66:24:57:
                    8c:4b:79:92:1e:ad:de:49:ee:2b:20:d8:ff:dd:0a:
                    cd:b1:3a:4d:b5:0e:68:fa:45:7b:54:48:8b:87:3a:
                    6a:da:03:09:8c:3a:b2:f3:4a:3a:38:5c:fe:8b:94:
                    95:54:f5:e2:a7:66:fa:e1:5e:8b:00:0a:bf:a9:76:
                    5d:a7:57:f6:6c:d9:d7:eb:26:30:97:0f:24:b9:b0:
                    f3:1c:32:34:be:54:bb:1c:6a:f8:85:70:7e:a1:50:
                    00:e0:aa:05:ed:e9:c9:05:c0:22:05:f0:de:1e:a6:
                    a7:9b:7b:0b:ae:bc:60:92:55:0b:b6:6a:a7:4b:75:
                    ed:07:b9:68:ef:cb:a8:a7:3c:ae:3b:84:e9:4a:5b:
                    07:b3:5e:d1:64:b1:ed:6f:e4:a5:8a:fe:2e:d2:d8:
                    49:ff:35:98:ec:b2:d3:e2:9f:5a:c7:9b:70:fb:55:
                    df:f9
                Exponent: 65537 (0x10001)
        X509v3 extensions:
            X509v3 Basic Constraints: critical
                CA:FALSE
            X509v3 CRL Distribution Points:

                Full Name:
                  URI:http://crl.certum.pl/cscasha2.crl

            Authority Information Access:
                OCSP - URI:http://cscasha2.ocsp-certum.com
                CA Issuers - URI:http://repository.certum.pl/cscasha2.cer

            X509v3 Authority Key Identifier:
                keyid:C0:7B:B4:C8:B7:6E:56:A7:09:48:9A:F8:72:4F:D7:D7:24:2C:36:3E

            X509v3 Subject Key Identifier:
                C4:B5:11:FD:03:7C:90:F0:8E:0F:8F:63:D5:80:CE:F6:78:99:2B:0C
            X509v3 Issuer Alternative Name:
                email:cscasha2@certum.pl
            X509v3 Key Usage: critical
                Digital Signature
            X509v3 Certificate Policies:
                Policy: 2.23.140.1.4.1
                Policy: 1.2.616.1.113527.2.5.1.4
                  CPS: https://www.certum.pl/CPS

            X509v3 Extended Key Usage:
                Code Signing, 1.3.6.1.4.1.311.61.1.1
    Signature Algorithm: sha256WithRSAEncryption
         78:32:3e:91:17:78:05:9b:83:fe:e2:ea:d8:1f:e6:49:ab:4b:
         22:ad:6c:80:50:70:0b:e4:94:cd:f1:8f:09:2a:1a:a5:dd:f9:
         0a:82:9e:32:b3:ff:a1:5c:7d:b5:a3:b2:31:18:4a:e0:87:2d:
         fe:5f:56:6c:ee:9b:e3:5a:1a:bb:56:4c:30:4d:bb:4e:3a:c2:
         41:d9:b3:db:55:e3:bd:a4:6e:17:68:6a:f8:88:22:86:64:a1:
         91:87:ab:11:ba:be:6e:bc:31:4e:aa:0d:4d:0a:a2:82:8e:55:
         cf:c7:f7:ee:1a:ca:c0:9c:ed:84:32:12:c7:0c:8e:b9:86:a3:
         30:bb:c0:b0:a7:7e:27:48:c4:38:e2:e3:48:42:05:04:9c:c4:
         a6:a1:8f:02:cb:c8:71:9f:0f:6c:06:22:75:cc:f2:c0:76:9f:
         1e:2c:3f:e0:4a:74:dd:99:73:87:cb:9b:d2:f4:dc:61:db:6e:
         4b:02:08:5d:0d:7d:b3:dc:05:27:5a:54:30:f9:d3:a9:b1:2d:
         e7:cf:21:e4:22:d3:c7:9e:86:55:dd:65:31:2a:d8:d6:dc:e9:
         f3:bc:7e:37:bc:24:5c:b4:3c:cf:9d:93:a2:5d:51:b0:42:5f:
         e7:ac:7a:7c:98:93:4f:2e:81:cb:bd:c0:ee:b9:a5:6b:37:bf:
         1c:82:ad:21
-----BEGIN CERTIFICATE-----
MIIFDjCCA/agAwIBAgIQTI1F/HzAtYTRThZH+t+isTANBgkqhkiG9w0BAQsFADCB
gDELMAkGA1UEBhMCUEwxIjAgBgNVBAoMGVVuaXpldG8gVGVjaG5vbG9naWVzIFMu
QS4xJzAlBgNVBAsMHkNlcnR1bSBDZXJ0aWZpY2F0aW9uIEF1dGhvcml0eTEkMCIG
A1UEAwwbQ2VydHVtIENvZGUgU2lnbmluZyBDQSBTSEEyMB4XDTE3MTIyNjA2MDcx
MVoXDTIwMTIyNTA2MDcxMVowazELMAkGA1UEBhMCQ04xEjAQBgNVBAoMCVhpbmcg
V2FuZzERMA8GA1UEBwwIU2hhbmdoYWkxEjAQBgNVBAMMCVhpbmcgV2FuZzEhMB8G
CSqGSIb3DQEJARYSd3hoZXJlQGhvdG1haWwuY29tMIIBIjANBgkqhkiG9w0BAQEF
AAOCAQ8AMIIBCgKCAQEA6ru1Qn9QXmJxK8FNNzJf0thsuzCbRn4gGNOe5Nw/zoHF
Ez4iV50+FIP5KxYjUBteysMLS8xRLsr8/kvImNlQ8JNbw2VAncGfwD3Mpjy8zQc3
dXC8lbdmJFeMS3mSHq3eSe4rINj/3QrNsTpNtQ5o+kV7VEiLhzpq2gMJjDqy80o6
OFz+i5SVVPXip2b64V6LAAq/qXZdp1f2bNnX6yYwlw8kubDzHDI0vlS7HGr4hXB+
oVAA4KoF7enJBcAiBfDeHqanm3sLrrxgklULtmqnS3XtB7lo78uopzyuO4TpSlsH
s17RZLHtb+Sliv4u0thJ/zWY7LLT4p9ax5tw+1Xf+QIDAQABo4IBljCCAZIwDAYD
VR0TAQH/BAIwADAyBgNVHR8EKzApMCegJaAjhiFodHRwOi8vY3JsLmNlcnR1bS5w
bC9jc2Nhc2hhMi5jcmwwcQYIKwYBBQUHAQEEZTBjMCsGCCsGAQUFBzABhh9odHRw
Oi8vY3NjYXNoYTIub2NzcC1jZXJ0dW0uY29tMDQGCCsGAQUFBzAChihodHRwOi8v
cmVwb3NpdG9yeS5jZXJ0dW0ucGwvY3NjYXNoYTIuY2VyMB8GA1UdIwQYMBaAFMB7
tMi3blanCUia+HJP19ckLDY+MB0GA1UdDgQWBBTEtRH9A3yQ8I4Pj2PVgM72eJkr
DDAdBgNVHRIEFjAUgRJjc2Nhc2hhMkBjZXJ0dW0ucGwwDgYDVR0PAQH/BAQDAgeA
MEsGA1UdIAREMEIwCAYGZ4EMAQQBMDYGCyqEaAGG9ncCBQEEMCcwJQYIKwYBBQUH
AgEWGWh0dHBzOi8vd3d3LmNlcnR1bS5wbC9DUFMwHwYDVR0lBBgwFgYIKwYBBQUH
AwMGCisGAQQBgjc9AQEwDQYJKoZIhvcNAQELBQADggEBAHgyPpEXeAWbg/7i6tgf
5kmrSyKtbIBQcAvklM3xjwkqGqXd+QqCnjKz/6FcfbWjsjEYSuCHLf5fVmzum+Na
GrtWTDBNu046wkHZs9tV472kbhdoaviIIoZkoZGHqxG6vm68MU6qDU0KooKOVc/H
9+4aysCc7YQyEscMjrmGozC7wLCnfidIxDji40hCBQScxKahjwLLyHGfD2wGInXM
8sB2nx4sP+BKdN2Zc4fLm9L03GHbbksCCF0NfbPcBSdaVDD506mxLefPIeQi08ee
hlXdZTEq2Nbc6fO8fje8JFy0PM+dk6JdUbBCX+esenyYk08ugcu9wO65pWs3vxyC
rSE=
-----END CERTIFICATE-----

```


2019/11/28  
