# Falco

Falco是一个云原生安全工具，由Sysdig创建，旨在实时检测异常行为和潜在安全威胁并发出警报。

官网: https://falco.org/  
github地址: https://github.com/falcosecurity/falco


## 快速演示部署
https://github.com/falcosecurity/falco/tree/master/docker/docker-compose

使用docker compose快速部署Falco, falcosidekick, falcosidekick-ui, redis  
部署后可访问 falcosidekick-ui http://127.0.0.1:2802

敏感命令示例:
```bash
sudo cat /etc/shadow
```

搜索日志:
```bash
grep falco /var/log/syslog
```


## 规则
Falco规则文件: https://github.com/falcosecurity/rules

配置和规则文件夹 /etc/falco/

规则示例：父进程是Bash的进程命令记录
```yaml
# Commands with Bash as Parent Logging rule
- rule: Log Commands with Bash as Parent
  desc: Logs all commands where bash is the parent process
  condition: >
    evt.type in (execve, execveat) and
    proc.pname = bash
  output: >
    Command executed with bash as parent (user=%user.name proc=%proc.name pid=%proc.pid ppid=%proc.ppid exe=%proc.exe command=%proc.cmdline args=%proc.args exeline=%proc.exeline parent_command=%proc.pcmdline)
  priority: INFO
  tags: [shell, command, monitoring, bash_as_parent]
```

规则示例：Bash网络连接检测
```yaml
# 现在这条规则检测到的cmdline不完整 https://github.com/falcosecurity/falco/issues/3842
- rule: Detect Bash Network Connection
  desc: Detects when a bash process initiates a network connection (potential reverse shell or data exfiltration)
  condition: >
    evt.type = connect and
    proc.name = bash and
    fd.typechar in ('4', '6')
  output: >
    Bash process detected making network connection 
    (user=%user.name process=%proc.name cmdline=%proc.cmdline connection=%fd.name container_id=%container.id)
  priority: WARNING
  tags: [network, shell, mitre_execution]
```


---
相关链接: https://cloud.tencent.com/developer/article/2452623  
