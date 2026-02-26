# capesandbox

CAPE沙箱是一个自动化恶意软件分析系统，源于Cuckoo。添加了自动恶意软件脱壳和配置提取功能。  
名字是一个缩写: "Config And Payload Extraction"。  
自动脱壳允许基于Yara规则进行分类，以补充网络（Suricata）和行为（API）特征。  

社区实例demo(用于体验，不应该提交太多样本): https://capesandbox.com

github地址: https://github.com/kevoreilly/CAPEv2  
官方文档: https://capev2.readthedocs.io/en/latest  

一些信息：
```
https://github.com/CAPESandbox/community/tree/master/modules/signatures
大部分signature在这里

https://github.com/CAPESandbox/CAPE-parsers
cape-parsers模块里是一些家族配置解析脚本，如CobaltStrikeBeacon、CobaltStrikeStager
注意是一个模块，可以这样查看位置 poetry env info
cape_parsers位置举例如下
/home/cape/.cache/pypoetry/virtualenvs/capev2-t2x27zRb-py3.12/lib/python3.12/site-packages/cape_parsers

https://github.com/kevoreilly/capemon/tree/capemon/loader/loader
loader.exe源码位置

https://github.com/splunk/PPLinject
PPLinject.exe源码位置
```
