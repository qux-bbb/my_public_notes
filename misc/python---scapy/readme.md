# python---scapy

scapy可发送、捕获、解析流量包。  

官网: https://scapy.net/  
官方文档: https://scapy.readthedocs.io/  

安装：  
```r
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

示例3，保存caps  
```python
# coding:utf8

from scapy.all import wrpcap

wrpcap('want_caps.pcapng', caps)
```

一些点：  
1. 每一层的original都是原始数据(包括属性)，如果想获取tcp原始数据，就是 `cap['IP']['TCP'].orginal`  
2. 如果不想包括属性，只想取数据部分，就是 `cap['IP']['TCP']['Raw'].orginal`  
3. cap不能用get方法，因为没有，只能一步一步判断了  


2018/5/2  
