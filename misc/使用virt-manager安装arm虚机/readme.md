# 使用virt-manager安装arm虚机

该方法有问题，安装debian11时，会进入一个 `UEFI Interactive Shell`，暂时没什么办法解决，不知道当时写笔记是装什么成功了。  
```r
UEFI Interactive Shell v2.2
EDK II
UEFI v2.70 (EDK II, 0x00010000)
Mapping table
     BLK1: Alias(s):
        VenHw(93E34C7E-B50E-11DF-9223-2443DFD72085,00)
    BLK0: Alias(s):
        PciRoot(0x0)/Pci(0x1,0x4)/Pci(0x0,0x0)
Press ESC in 1 seconds to skip startup.nsh or any other key to continue.
Shell> 
```

---

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
