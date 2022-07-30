# ubuntu20.04---安装kvm

安装：  
```r
sudo apt -y install bridge-utils cpu-checker libvirt-clients libvirt-daemon qemu qemu-kvm
sudo apt -y install virt-manager
```

检查虚拟化功能：  
```r
kvm-ok

# 出现这样的行就可以了
# INFO: /dev/kvm exists
# KVM acceleration can be used
```

然后就可以用virt-manager安装虚拟机了  


原链接: https://ubuntu.com/blog/kvm-hyphervisor  


2022/7/26  
