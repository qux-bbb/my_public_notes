# openssl---RSA加解密

注意：  
1. 这里所说的私钥不等于密码学中的私钥
2. RSA不用来加密大文件，性能和计算问题  

生成一个私钥：  
```bash
openssl genrsa -out test.key 2048
```
`-out`指定生成文件，需要注意的是生成的test.key包含了公钥和私钥两部分，也就是说这个文件既可用来加密也可以用来解密。后面的2048是生成私钥的长度。  

从test.key提取公钥：  
```bash
openssl rsa -in test.key -pubout -out test_pub.key
```
`-in`指定输入文件，`-out`指定保存公钥的文件。  

使用公钥加密hello.txt：  
```bash
openssl rsautl -encrypt -in hello.txt -inkey test_pub.key -pubin -out hello.enc
```
`-in`指定要加密的文件，`-inkey`指定密钥，`-pubin`表明是用纯公钥文件加密，`-out`为加密后的文件。  

使用私钥解密文件：  
```bash
openssl rsautl -decrypt -in hello.enc -inkey test.key -out hello.dec
```

生成aes加密的私钥：  
```bash
openssl genrsa -aes256 -out private.key 2048
```

查看私钥的结构：  
```bash
openssl rsa -text -in private.key
```


参考链接: http://www.cnblogs.com/aLittleBitCool/archive/2011/09/22/2185418.html  


2018/8/13  
