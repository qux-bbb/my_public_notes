# linux---tcpdump
dump traffic on a network  

```bash
# 监听eth0网卡流量并保存
tcpdump -i eth0 -w result.pcap

# 同时输出到终端和文件(文本文件，不是pcap)
tcpdump -l | tee result.txt

# 保存为pcap文件的同时输出到终端
# 可以把"-l"换成"-U", 以保证在每个平台都可以按行输出(使用"-l"，WinDump在windows下会按字符输出)
tcpdump -l -w - | tee result.pcap | tcpdump -r -

# 指定端口
tcpdump -i eth0 -w result.pcap port 80

# 指定host
tcpdump -i eth0 -w result.pcap host 1.2.3.4

# 超过大小生成新的文件，这里指定 1 M，新文件名字后面会加数字，如：result.pcap1
tcpdump -i eth0 -C 1 -w result.pcap


# 拆分流量包：每个100M
tcpdump -r source.pcap -C 100 -w result_pcap
```


参考链接: https://stackoverflow.com/questions/25603831/how-can-i-have-tcpdump-write-to-file-and-standard-output-the-appropriate-data  


2021/4/9  
