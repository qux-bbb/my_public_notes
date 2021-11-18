# 多系统---默认启动系统

keywords: ubuntu kali windows 双系统 默认引导  

要修改的文件: `/etc/default/grub`  

修改项：  
```r
# 从0开始计数，默认是0,想要哪个当启动项就改成相应的数字，可以在开机启动选择系统界面看看顺序
GRUB_DEFAULT=0
```  

修改完之后需要运行命令: `update-grub`, 使修改生效  


2017/9/2  
