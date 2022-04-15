# iptables---禁止某ip访问或解封

封杀某ip：  
```r
iptables -I INPUT -s 123.44.55.66 -j DROP
```

解封ip：  
```r
iptables -D INPUT -s 123.44.55.66 -j DROP
```


2019/2/11  
