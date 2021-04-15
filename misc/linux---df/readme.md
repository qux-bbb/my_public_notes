df, disk free, 查看磁盘剩余空间，可显示总容量和已用空间  

一次执行如下：  
```
hello@hello-PC:~/Desktop$ df -h
文件系统                   容量  已用  可用 已用% 挂载点
udev                       1.9G     0  1.9G    0% /dev
tmpfs                      391M  2.9M  388M    1% /run
/dev/mapper/vg0-Roota       15G  5.8G  8.2G   42% /
tmpfs                      2.0G   39M  1.9G    2% /dev/shm
tmpfs                      5.0M  4.0K  5.0M    1% /run/lock
tmpfs                      2.0G     0  2.0G    0% /sys/fs/cgroup
/dev/sda1                  1.5G  185M  1.2G   14% /boot
/dev/mapper/vg0-_dde_data   77G  448M   73G    1% /data
/dev/mapper/vg0-Backup      12G  6.4G  4.8G   58% /recovery
tmpfs                      391M   48K  391M    1% /run/user/1000
```

参考: https://wiki.jikexueyuan.com/project/learn-linux-step-by-step/command-abbreviation.html  