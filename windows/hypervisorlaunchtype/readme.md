# hypervisorlaunchtype

keywords: 笔记本vmware虚拟机卡顿

hypervisorlaunchtype开启会严重影响VMware虚拟机的性能，如果用Vmware虚拟机，建议关掉。

两条命令都需要使用管理员权限打开cmd执行。

查看当前hypervisorlaunchtype：
```r
bcdedit /enum | findstr hypervisorlaunchtype
```

关闭hypervisorlaunchtype：
```r
bcdedit /set hypervisorlaunchtype off
```

还需要关闭内存完整性以提高性能
```
Windows安全中心 -> 设备安全性 -> 内核隔离 -> 内核隔离详细信息 -> 内存完整性，关闭，重启系统
```