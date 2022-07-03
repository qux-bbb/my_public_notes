# 使用virt-manager安装arm虚机

virt-manager只能在linux上运行，所以这个方法只适用linux。  

在安装qemu和virt-manager的基础上，需要安装 `qemu-system-arm`  
```r
sudo apt install qemu-system-arm
```

和安装普通虚机没太大区别，要选一下"架构选项：  
```r
aarch64 64位，苹果称之为arm64
arm     32位
```


2022/7/3  
