# Ghidra

Ghidra是NSA开发的逆向平台，有反编译和调试功能，类似IDA。  

官网: https://www.ghidra-sre.org/  
github地址: https://github.com/NationalSecurityAgency/ghidra  
安装文档: https://www.ghidra-sre.org/InstallationGuide.html  

## 调试相关
Ghidra10.0版本增加了调试器  
GADP: Ghidra Asynchronous Debug Protocol, Ghidra异步调试协议  

据文档介绍IN-VM模式直接调用调试器，会快一点，GADP模式通过协议连接调试器，比IN-VM模式慢，但不会导致数据丢失  

调试功能起码windows上现在不好用  


20190925
