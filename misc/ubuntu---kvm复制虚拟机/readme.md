# ubuntu---kvm复制虚拟机

kvm虚拟机比较重要的就是磁盘文件和配置文件了，把相关的文件放到正确的位置，然后使用命令定义新的虚拟机，这样就完成了kvm虚拟机的复制  

xml配置文件位置：  
```r
/etc/libvirt/qemu/winxp.xml
```
磁盘文件位置：  
```r
/var/lib/libvirt/images/winxp.qcow2
```
定义新虚拟机的命令：  
```r
virsh define /etc/libvirt/qemu/winxp.xml
```


如果需要覆盖，不能直接覆盖，会造成莫名其妙的问题，应该先删除再添加新的  
关闭所有虚拟机、删除快照、undefine、删除相关镜像和xml文件、添加新的  
列出所有虚拟机：  
```r
virsh list --all
```
列出指定虚拟机的所有快照  
```r
virsh snapshot-list winxp
```
删除指定虚拟机的指定快照  
```r
virsh snapshot-delete --domain winxp --snapshotname i_am_ready
```
undefine一个虚拟机：  
```r
virsh undefine winxp
```

之所以要删除快照，是因为先删除快照才能undefine虚拟机  


参考：https://www.cyberciti.biz/faq/howto-linux-delete-a-running-vm-guest-on-kvm  


2019/4/20   
