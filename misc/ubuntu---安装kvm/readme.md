# ubuntu---安装kvm

keywords: kvm 界面 ubuntu14.04  

KVM：Kernel-based Virtual Machine  

要装桌面环境才能使用virt-manager  

安装软件  
```r
sudo apt-get install qemu qemu-kvm qemu-system libvirt-bin bridge-utils
sudo apt-get install virt-manager
```

添加到相应的用户组  
```r
sudo usermod -G libvirtd -a <username>
```

重启  
```r
sudo reboot
```

查看kvm是否安装成功，"can be used" 则成功  
```r
kvm-ok
```

查看kvm内核模块是否已加载  
```r
sudo lsmod | grep kvm
```
若KVM内核没加载执行下面命令加载：  
```r
sudo modprobe kvm
```

启动虚拟机管理界面，开始使用  
```r
virt-manager
```

用virt-manager安装虚拟机和vmware步骤差不多，找一个iso镜像，一步一步装就可以了  


参考：  
https://www.cnblogs.com/hanson1/p/7105291.html  
Unable to connect to libvirt. 解决方法：  
https://askubuntu.com/questions/736550/kvm-qemu-vmm-local-host-not-connected  


2019/1/8  
