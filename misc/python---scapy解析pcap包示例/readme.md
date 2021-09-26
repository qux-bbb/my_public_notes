# python---scapy解析pcap包示例

安装：  
```
pip install scapy
```

示例1，输出源ip  
```python
# coding:utf8

from scapy.all import rdpcap

caps = rdpcap('test.pcapng')

print(caps[0].show())
print(caps[0]['IP'].src)
```

示例2，解析icmp流量  
```python
# coding:utf8

from scapy.all import rdpcap

caps = rdpcap('icmp_data.pcap')

flag = ''
for cap in caps:
    if 'ICMP' in cap and cap['IP'].src == '30.0.250.11':
        flag += chr(cap['IP']['ICMP']['Raw'].original[8])
print(flag)
```

2018/5/2  
