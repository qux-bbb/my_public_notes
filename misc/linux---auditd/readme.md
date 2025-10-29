# linux---auditd

auditd - The Linux Audit daemon, 可以监控文件、进程动作

安装auditd
```bash
sudo apt install auditd
```

## 监控文件写入
```bash
# 监控特定文件的写入操作
sudo auditctl -w /path/to/1.txt -p w -k file_write

# 监控整个目录的写入操作
sudo auditctl -w /path/to/directory/ -p w -k file_write
```

查询
```bash
# 搜索相关的审计记录
sudo ausearch -k file_write

# 或者查看原始日志
sudo tail -f /var/log/audit/audit.log | grep file_write
```


## 监控命令
注意不是完整命令行

```bash
# 监控所有execve系统调用（程序执行）
sudo auditctl -a always,exit -F arch=b64 -S execve
sudo auditctl -a always,exit -F arch=b32 -S execve
```

查询
```bash
# 搜索相关的审计记录
sudo ausearch -sc execve

# 或者查看原始日志
sudo tail -f /var/log/audit/audit.log | grep execve
```


## 列出规则
```bash
sudo auditctl -l
```


## 清空规则
```bash
sudo auditctl -D
```


## 持久化规则
编辑该文件 /etc/audit/rules.d/audit.rules 添加内容
```ini
# 监控64位程序的execve系统调用
-a always,exit -F arch=b64 -S execve -k EXEC_CMDLINE

# 监控32位程序的execve系统调用  
-a always,exit -F arch=b32 -S execve -k EXEC_CMDLINE
```

使规则生效
```bash
# 重新生成规则（这会编译/etc/audit/rules.d/下的所有规则）
sudo augenrules --load

# 检查生成的规则
sudo auditctl -l
```


---
2025/10/11
