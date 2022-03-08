# shutdown命令

windows的shutdown命令可以用来定时关闭计算机、重启计算机。  

定时关闭计算机：  
```bat
:: 100秒后关机，有效范围是 0-315360000 (10 年)，默认值为 30
shutdown /s /t 100
```
取消定时关机：  
```bat
shutdown /a
```
立即重启计算机：  
```bat
shutdown /r /t 0
```


2022/3/7  
