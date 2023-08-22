# 一些IDA插件

## keypatch
https://github.com/keystone-engine/keypatch  
以汇编形式修改可执行文件  

**安装**  
需要先安装keystone  
https://github.com/keystone-engine/keystone/releases/download/0.9.1/keystone-0.9.1-python-win64.msi
python路径选在IDA下的python文件夹  

然后安装keypatch  
https://raw.githubusercontent.com/keystone-engine/keypatch/master/keypatch.py  
放在plugin下即可  

参考: https://www.cnblogs.com/zhaijiahui/p/7978897.html  


## OllyDumpEx
http://low-priority.appspot.com/ollydumpex/  
dump进程  
```plain
- OllyDumpEx_IdaRT.plw, OllyDumpEx_IdaRT.p64
  for IDA Pro 32bit build version 5.x or higher (6.9 tested)
- OllyDumpEx_IdaRT.dll, OllyDumpEx_IdaRT64.dll
  for IDA Pro 64bit build version 7.0 or higher (7.1 tested)
- OllyDumpEx_IdaFW.plw
  for IDA Freeware 32bit build version 5.0 (5.0 tested)
- OllyDumpEx_IdaFW64.dll
  for IDA Freeware 64bit build version 7.0 (7.0.190307 tested)
```


## Hexlight
对应的括号可以突出显示  
https://bbs.pediy.com/thread-226099.htm  


## findcrypt
查找二进制文件使用已知算法的特征  
安装方法：把从52POJIE下载的ida_plugin.zip里的findcrypt.plw放在plugins文件夹即可  
理论来说是这样安装，但我在插件菜单里找不到，，  


## findcrypt-yara
https://github.com/polymorf/findcrypt-yara  
通过查找加密常量确定某种加密算法  

安装方法: 把 findcrypt3.py findcrypt3.rules放在plugins文件夹即可  
yara-python最新版本不支持python27了，需要手动指定支持的版本：  
python -m pip install yara-python==3.11.0  


## x64dbgida
https://github.com/x64dbg/x64dbgida  
可以把IDA和x64dbg的符号等信息互相导入  

安装方法：x64dbgida.py放在plugins文件夹即可，去release下载，注意版本  


## Finger
https://github.com/aliyunav/Finger  
听说可以恢复一些符号，需要联网，有机会试试  


---
2019/7/11  
