# android---脱壳相关项目

## PKID-APP
查壳工具  
https://bbs.pediy.com/thread-225120.htm  


## FRIDA-DEXDump
Fast search and dump dex on memory.  
https://github.com/hluwa/FRIDA-DEXDump  
只要打开相关应用，运行 main.py 就好了  


## Frida-Apk-Unpack
基于Frida的脱壳工具  
https://github.com/GuoQiang1993/Frida-Apk-Unpack  
执行命令：  
```r
frida -U -f com.xxx.xxx -l dexDump.js --no-pause
```
梆梆不行，MainActivity 被隐藏了  


## FART
ART环境下自动化脱壳方案  
https://github.com/hanbinglengyue/FART  
还没试过，前面的够用了  


---
2020/5/20  
