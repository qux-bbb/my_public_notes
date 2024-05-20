# linux---占用指定大小内存

占用10240M内存：  
```bash
mkdir /tmp/memory
sudo mount -t tmpfs -o size=10240M tmpfs /tmp/memory
dd if=/dev/zero of=/tmp/memory/block
```

恢复：  
```bash
rm /tmp/memory/block
sudo umount /tmp/memory
rm /tmp/memory -r
```

占用前后可使用free命令查看当前内存占用情况  


原链接: https://blog.csdn.net/wsuyixing/article/details/123930318  


2024/5/20  
