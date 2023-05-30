# openssl---自签名证书

```sh
openssl genrsa -out server.key 2048
openssl req -new -x509 -key server.key -out server.cer
```


2018/8/20  
