# guestfish修改镜像

keywords: img qcow2  

```r
# Mount
guestfish --rw -a centos63_desktop.img
# Launch
run
# 列出文件系统
list-filesystems
# mount一个文件系统
mount /dev/vg_centosbase/lv_root /
# 删除一个文件
rm /etc/udev/rules.d/70-persistent-net.rules
# 编辑一个文件
edit /etc/sysconfig/network-scripts/ifcfg-eth0
# 创建一个文件
touch /etc/sysconfig/modules/8021q.modules
# 修改文件权限
chmod 0755 /etc/sysconfig/modules/8021q.modules
# 退出
exit
```

原链接: https://docs.openstack.org/image-guide/modify-images.html  


2022/12/9  
