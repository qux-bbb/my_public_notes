# 制作linux的U盘启动盘

windows下直接用rufus：  
https://rufus.ie/  

linux命令也很简单：  
```r
# 找到U盘对应的名字，比如/dev/sdb
fdisk -l
# 将镜像写入U盘
dd if=kali-linux-2016.2-amd64.iso of=/dev/sdb bs=1M
```


2017/9/2  
