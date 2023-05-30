# openssl---cer转pem

windows下使用openssl转证书格式：cer转pem  

```cmd
openssl x509 -inform der -in test.cer -out test.pem
```

参考：https://jingyan.baidu.com/article/9989c746d1681bf648ecfebe.html  


2018/11/30  
