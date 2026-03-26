# Falco

Falco是一个云原生安全工具，由Sysdig创建，旨在实时检测异常行为和潜在安全威胁并发出警报。

官网: https://falco.org/  


## 快速演示部署
https://github.com/falcosecurity/falco/tree/master/docker/docker-compose

使用docker compose快速部署Falco, falcosidekick, falcosidekick-ui, redis  
部署后可访问 falcosidekick-ui http://127.0.0.1:2802

敏感命令示例:
```bash
sudo cat /etc/shadow
```


---
信息来源: https://cloud.tencent.com/developer/article/2452623  
