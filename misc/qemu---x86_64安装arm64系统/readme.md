# qemu---x86_64安装arm64系统

安装系统  
```r
$ sudo apt install qemu-utils qemu-system-arm

为了速度快，把源换成了国内的
$ wget https://mirrors.huaweicloud.com/debian/dists/bullseye/main/installer-arm64/current/images/netboot/debian-installer/arm64/initrd.gz
$ wget https://mirrors.huaweicloud.com/debian/dists/bullseye/main/installer-arm64/current/images/netboot/debian-installer/arm64/linux
$ wget https://mirrors.huaweicloud.com/debian/dists/bullseye/main/installer-arm64/current/images/netboot/mini.iso
$ qemu-img create -f qcow2 debian-3607-aarch64.qcow2 32G
$ qemu-system-aarch64 -M virt -cpu cortex-a53 -m 1G -kernel ./linux -initrd ./initrd.gz \
    -hda debian-3607-aarch64.qcow2 -append "console=ttyAMA0" \
    -drive file=mini.iso,id=cdrom,if=none,media=cdrom \
    -device virtio-scsi-device -device scsi-cd,drive=cdrom -nographic
需要联网才能安装，选一个国内的源快一些，大概得一个小时，安装时不需要选图形界面，重启又回到安装界面直接把窗口关掉就可以了
设置了用户 root/root snow/ball
```

提取新的vmlinuz和initrd.img  
```r
$ sudo apt install libguestfs-tools

$ ls /boot/vmlinuz* -lh
    lrwxrwxrwx 1 root root  25  5月  7 11:11 /boot/vmlinuz -> vmlinuz-5.19.0-41-generic
    -rw------- 1 root root 12M 10月 18  2022 /boot/vmlinuz-5.15.0-53-generic
    -rw-r--r-- 1 root root 12M  4月 18 23:26 /boot/vmlinuz-5.19.0-41-generic
    lrwxrwxrwx 1 root root  25  5月  7 11:11 /boot/vmlinuz.old -> vmlinuz-5.15.0-53-generic
$ sudo chmod 644 /boot/vmlinuz-5.19.0-41-generic  # 必须执行这一步，否则virt-ls不会正常执行，注意先看看/boot/文件夹下的文件，修改最近类似的文件权限
$ virt-ls -a debian-3607-aarch64.qcow2 /boot/
    System.map-5.10.0-22-arm64
    config-5.10.0-22-arm64
    initrd.img
    initrd.img-5.10.0-22-arm64
    initrd.img.old
    lost+found
    vmlinuz
    vmlinuz-5.10.0-22-arm64
    vmlinuz.old
$ virt-copy-out -a debian-3607-aarch64.qcow2 /boot/vmlinuz-5.10.0-22-arm64 /boot/initrd.img-5.10.0-22-arm64 .
```

启动虚机  
```r
$ qemu-system-aarch64 -M virt -cpu cortex-a53 -m 1G -initrd initrd.img-5.10.0-22-arm64 \
    -kernel vmlinuz-5.10.0-22-arm64 -append "root=/dev/vda2 console=ttyAMA0" \
    -drive if=virtio,file=debian-3607-aarch64.qcow2,format=qcow2,id=hd \
    -net user,hostfwd=tcp::10022-:22 -net nic \
    -device intel-hda -device hda-duplex -nographic
```

ssh连接虚机  
```r
ssh snow@localhost -p 10022
```


原链接: http://phwl.org/2022/qemu-aarch64-debian/  


2023/5/8  
