# PentAGI

keywords: 自动渗透测试

## 基本信息
PentAGI, Penetration testing Artificial General Intelligence, 全自主的渗透测试智能体。

官网: https://pentagi.com/  
github地址: https://github.com/vxcontrol/pentagi

在终端配置deepseek的时候，只填API key，不要填Provider Name，否则会报错

PentAGI生成的文件在 /var/lib/docker/volumes/ 目录下，不在的话用 `docker exec -it <pentagi_container_name> /bin/bash` 进指定容器查看

## 模板使用
可以自己写模板，方便后续使用：
```
网站渗透测试

对该网站渗透测试 {{TARGET_URL}}  
只扫描该网站，发现新网站时，仅记录供后续测试  
发现漏洞时，记录详细利用步骤  
使用中文生成步骤、描述、报告  

非漏洞情况：
- https使用低版本加密套件
- 请求头、响应头缺少安全限制

禁止项：
- 禁止进行全端口高频扫描
- 禁止大量爆破
- 禁止SSL/TLS安全评估与加密套件检测
```

---
信息来源: https://mp.weixin.qq.com/s/0x5is8TKXLbaQDHAOH_IuA
