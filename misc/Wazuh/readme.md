# Wazuh

keywords: EDR

开源安全平台，为端点和云工作负载提供统一的 XDR 和 SIEM 保护。  
可以收集系统信息(系统版本、CPU、内存大小等)，软件信息(软件、补丁、浏览器扩展)，进程信息(进程ID、名称、路径等)，网络信息(IP地址、端口、协议等)等。

不适合只通过服务端在客户端执行自定义脚本检查漏洞。

官网: https://wazuh.com/  
github地址: https://github.com/wazuh/wazuh  
各种部署方式(包含预构建虚机): https://documentation.wazuh.com/current/deployment-options/index.html


## 一些注意点
```
Windows客户端的简单UI程序路径
C:\Program Files (x86)\ossec-agent\win32ui.exe

使用预构建虚机部署时，如果服务端没有ip地址，试试把网络模式改成NAT模式

默认不会实时监控进程创建，只会每小时获取一次进程信息，可以问Hermes怎么配置实时进程监控和命令行获取

官方只提供从官网下载安装客户端的命令，不提供从本地下载安装的命令，可以下载之后手动安装
https://packages.wazuh.com/4.x/windows/wazuh-agent-4.14.5-1.msi
msiexec.exe /i wazuh-agent-4.14.5-1.msi /q WAZUH_MANAGER='192.168.116.147' 
```
