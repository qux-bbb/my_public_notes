# hypervisorlaunchtype

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
