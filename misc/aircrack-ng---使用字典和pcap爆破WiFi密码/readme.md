# aircrack-ng---使用字典和pcap爆破WiFi密码

在成功获取到WPA-PSK验证数据报文后，即可开始破解  
命令：  
```r
aircrack-ng -w 字典文件 捕获的cap文件
```

因为可以用fluxion无脑拿到验证数据报文，所以这是种代替aircrack前面繁琐步骤的好方法  


2016/6/21  
