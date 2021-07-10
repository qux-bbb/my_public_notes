# qemu

QEMU，Quick EMUlator，是一个通用的、开源的机器仿真器和虚拟机。  

官网: https://www.qemu.org/  
文档地址: https://qemu-project.gitlab.io/qemu/  

使用举例：  
```bash
# 创建空磁盘 20G空间
qemu-img create -f qcow windows.img 20G
# 启动，用iso安装系统 内存4G
qemu-system-x86_64 -m 4G windows.img -cdrom ./cn_windows_7_ultimate_with_sp1_x64_dvd_u_677408.iso
# 启动虚机 内存4G
qemu-system-x86_64 -m 4G windows.img
```
qemu-system-x86_64可以使用 `-enable-kvm` 选项加速，虽然还是比较卡，大概用了3个小时，可能还有别的加速方式吧  


参考链接：  
1. https://baike.baidu.com/item/QEMU/1311178
2. https://www.cnblogs.com/youxia/p/linux019.html


2021/7/10  
