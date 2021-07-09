# SigThief

一个可执行程序证书复制伪造工具，虽然验证无效，但可以看  

github地址: https://github.com/secretsquirrel/SigThief  

最简单用法：  
```bash
#                有签名          没有但想要                     有签名了！
./sigthief.py -i tcpview.exe -t x86_meterpreter_stager.exe -o /tmp/msftesting_tcpview.exe
```
具体的一次命令：  
```bash
py -3 sigthief.py -i has_cert.exe -t no_cert.exe -o result.exe
```


2021/7/9  
