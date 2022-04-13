# linux---fdisk

keywords: 磁盘大小 硬盘大小  

fdisk 操作磁盘分区表，可以用来查看所有硬盘大小  

```r
sudo fdisk -l
```

```r
hello@hello-VirtualBox:~/Desktop$ sudo fdisk -l
...
Disk /dev/sda：40 GiB，42949672960 字节，83886080 个扇区
Disk model: VBOX HARDDISK   
单元：扇区 / 1 * 512 = 512 字节
扇区大小(逻辑/物理)：512 字节 / 512 字节
I/O 大小(最小/最佳)：512 字节 / 512 字节
磁盘标签类型：dos
磁盘标识符：0xa26009f7

设备       启动    起点     末尾     扇区  大小 Id 类型
/dev/sda1  *       2048  1050623  1048576  512M  b W95 FAT32
/dev/sda2       1052670 83884031 82831362 39.5G  5 扩展
/dev/sda5       1052672 83884031 82831360 39.5G 83 Linux
...
```


2022/4/13  
