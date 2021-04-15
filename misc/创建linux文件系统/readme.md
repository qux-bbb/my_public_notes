创建linux文件系统，会用到dd mkfs.ext4 mount umount命令  
```bash
# 生成一个空文件(100M)
dd if=/dev/zero of=100M.img bs=1M count=100
# 在空文件上建立ext4格式的文件系统
mkfs.ext4 100M.img
# 挂载此文件系统到a_folder文件夹，然后就可以在a_folder文件夹内对该文件系统做操作
# a_folder文件夹必须存在
mount 100M.img a_folder
# 卸载此文件系统
umount a_folder
```

把a_folder下的hello_folder映射到b_folder  
```bash
mount --bind a_folder/hello_folder b_folder
```
deepin应该就用到了这个思路  