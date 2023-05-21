# pcap---USB键盘信息相关

info为"URB_INTERRUPT in"则为键盘的USB信息  

使用tshark分离usb.capdata, Lefover Capture Data  
```r
tshark -r usb-keyboard-data.pcap -T fields -e usb.capdata
```


2019/9/24  
