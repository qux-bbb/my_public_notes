# linux---auditd

auditd - The Linux Audit daemon, 可以监控文件、进程动作

安装auditd
```bash
sudo apt install auditd
```

临时设置监控文件
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


2025/10/11
