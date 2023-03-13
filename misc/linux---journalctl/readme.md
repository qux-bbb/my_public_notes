# linux---journalctl

journalctl 可以用来查看systemd产生的日志。  

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

来自 tldr  


2023/3/14  
