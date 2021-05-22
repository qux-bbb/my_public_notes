# virsh简介

virsh，命令行虚机管理工具，介绍说可以管理多种虚拟机，只试过kvm。  

简单命令  
```sh
# 列出开机虚机
virsh list

# 列出所有虚机
# 如果没有相应的结果，加 sudo 试试
virsh list --all

# 打开虚机 hello
virsh start hello

# 关闭虚机 hello
virsh shutdown hello

# 编辑虚机 hello 对应的配置文件
virsh edit hello

# 列出虚机快照
virsh snapshot-list hello

# 修改虚机快照名称（通过修改配置文件实现）
# 问题：改完确实可以看到改了，但是恢复到相应快照时会报错说不存在
virsh snapshot-edit win7_x64 --snapshotname cuckoo_ready --rename
```


2020/08/06  
