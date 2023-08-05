# 端口转发

Windows下也有类似iptables的端口转发功能  

```bat
:: 查看所有端口转发规则
netsh interface portproxy show all
:: 添加端口转发规则，从监听端口转发到目标端口
netsh interface portproxy add v4tov4 listenport=[你的监听端口] listenaddress=[你的监听地址] connectport=[目标端口] connectaddress=[目标地址]
:: 删除端口转发规则，提供监听端口和监听地址即可
netsh interface portproxy delete v4tov4 listenport=[你的监听端口] listenaddress=[你的监听地址]
```

示例：  
```bat
:: 添加端口转发规则，从9999端口转发到2017端口
netsh interface portproxy add v4tov4 listenport=9999 listenaddress=127.0.0.1 connectport=2017 connectaddress=127.0.0.1
:: 删除添加的转发规则
netsh interface portproxy delete v4tov4 listenport=9999 listenaddress=127.0.0.1
```


参考: chatgpt  


2023/8/5  
