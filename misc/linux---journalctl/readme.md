# linux---journalctl

journalctl 可以用来查看systemd产生的日志。  

来自 tldr  
```r
# [f]ollow new messages (like `tail -f` for traditional syslog):
journalctl -f

# Show all messages by a specific [u]nit:
journalctl -u unit

# Filter messages within a time range (either timestamp or placeholders like "yesterday"):
journalctl --since now|today|yesterday|tomorrow --until YYYY-MM-DD HH:MM:SS

# Show all messages by a specific process:
journalctl _PID=pid

# Show all messages by a specific executable:
journalctl path/to/executable
```

导出日志示例，来自chatgpt：  
```r
# 导出自2023-01-01以来的nginx服务日志
journalctl --since="2023-01-01" -u nginx > nginx_logs.txt
# 仅导出错误日志
journalctl --since="2023-01-01" -u nginx -p err > nginx_error_logs.txt
```


2023/3/14  
