# CPU

CPU, Central Processing Unit，中央处理器，计算机的大脑吧  

windows和linux对内核、处理器的叫法不一样(下面的东西可能是错的，暂时先这样写)  

```
windows cpu 内核    逻辑处理器
linux   cpu 处理器  总cpu核心数
```

## 查看逻辑处理器数量
Windows  
计算机->右键选择"管理"->设备管理器->处理器  
该项下有几行就是有几个逻辑处理器  
另外用win10的任务管理器切换到"性能"栏，可以很清楚看到"内核"和"逻辑处理器"的数量  

linux  
`cat /proc/cpuinfo | grep cores` 应该是把数字加起来就好了，不大确定  


参考链接: https://baike.baidu.com/item/中央处理器  


2021/5/6  
