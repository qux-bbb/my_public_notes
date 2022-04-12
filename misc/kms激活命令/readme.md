# kms激活命令

## 服务器搭建
这是一个kms激活服务器项目：  
https://github.com/SystemRage/py-kms  
不好用了  

## 激活过程
```r
cscript //nologo slmgr.vbs /upk
cscript //nologo slmgr.vbs /ipk <ProductKey>
cscript //nologo slmgr.vbs /skms 192.168.122.130:1688
cscript //nologo slmgr.vbs /ato
```

执行第2条命令时, 显示:  
```r
在运行 Microsoft Windows 非核心版本的计算机上，运行“slui.exe 0x2a 0xC004F015”
以显示错误文本。
错误: 0xC004F015
```

执行`slui.exe 0x2a 0xC004F015`, 显示:  
```r
软件授权服务报告许可证未安装
```

在ubuntu上运行server端, 在win10上执行2条命令, 成功激活:  
```r
cscript //nologo slmgr.vbs /skms 192.168.122.130:1688
cscript //nologo slmgr.vbs /ato
```

20200221  
20201220 增加服务器项目记录  


2020/12/20  
