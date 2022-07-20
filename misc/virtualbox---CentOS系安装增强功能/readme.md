# virtualbox---CentOS系安装增强功能

CentOS、Rocky直接安装增强功能会失败，提示如下：  
```r
Kernel headers not found for target kernel
```

做如下操作：  
```r
sudo yum update
sudo yum install kernel-devel kernel-headers
reboot  # 一定要重启
sudo install gcc make perl
```
然后再次安装即可。  

如果还是不行，查看提示的日志文件，按提示安装相应模块。  


参考链接: https://www.dev2qa.com/how-to-resolve-virtualbox-guest-additions-kernel-headers-not-found-for-target-kernel-error/  


2022/7/20  
