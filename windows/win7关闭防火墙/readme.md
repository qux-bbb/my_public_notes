# win7关闭防火墙

keywords: 禁用防火墙  


## 方法1: 图形化界面
控制面板 -> 系统和安全 -> Windows防火墙 -> 打开或关闭Windows防火墙  
把所有"启用Windows防火墙"切换为"关闭Windows防火墙"  


## 方法2: 命令行(管理员权限)
```r
netsh advfirewall set allprofiles state off
```


## 部分信息来源
1. chatgpt
2. 文心一言
3. https://learn.microsoft.com/zh-CN/troubleshoot/windows-server/networking/netsh-advfirewall-firewall-control-firewall-behavior


---
2024/4/19  
