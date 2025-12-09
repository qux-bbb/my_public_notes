# testssl

testssl.sh 是一个命令行工具，用于检查服务器在任意端口上对 TLS/SSL 加密套件、协议的支持情况，以及是否存在近期发现的加密漏洞等。

官网: https://testssl.sh/

最简单的使用方法
```bash
./testssl.sh https://www.hello.com:1234
```

如果扫描的是ip，建议使用这样的形式避免长时间的等待
```bash
./testssl.sh --nodns none https://1.2.3.4:1234
```
