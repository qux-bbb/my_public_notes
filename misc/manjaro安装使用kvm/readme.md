# manjaro安装使用kvm

安装  
```bash
sudo pacman -S qemu ebtables dnsmasq virt-manager
```
可能出现 `iptables-nft 与 iptables 有冲突` 提示，按 'y' 删除就好了  

启动 libvirt 守护进程并查看状态  
```bash
systemctl start libvirtd
systemctl status libvirtd
```

打开图形界面使用  
```bash
virt-manager
```
默认只能看到 LXC，这是 `linux container`，不用这个  
文件 -> 添加连接，选择 `QEMU/KVM`，点击"连接"  
点击 `QEMU/KVM`，右键"新建",接下来的步骤就和 vmware/virtualbox 类似了  


参考链接: https://baijiahao.baidu.com/s?id=1661665885678780903  


2021/5/9  
