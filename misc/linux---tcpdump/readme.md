# linux---tcpdump
dump traffic on a network  

```bash
# 监听eth0网卡流量并保存
tcpdump -i eth0 -w result.pcap

# 指定端口
tcpdump -i eth0 -w result.pcap port 80

# 指定host
tcpdump -i eth0 -w result.pcap host 1.2.3.4

# 超过大小生成新的文件，这里指定 1 M，新文件名字后面会加数字，如：result.pcap1
tcpdump -i eth0 -C 1 -w result.pcap


# 拆分流量包：每个100M
tcpdump -r source.pcap -C 100 -w result_pcap
```


2021/4/9  
