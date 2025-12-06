# 弹出移动硬盘显示某个程序正在使用

移动硬盘使用完后，点击右下角的"安全删除硬件并弹出媒体"，弹窗信息如下：
```r
弹出USB大容量存储设备时出问题

Windows无法停用“卷”设备，原因是某个程序正在使用它。关闭可能使用该设备的所有程序，然后稍后重试。
```

TODO 2种方法都不一定有效

## 方法1 File Locksmith
File Locksmith 选中盘符，右键“使用 File Locksmith 解锁”，即可查看正在使用该盘的进程，关闭即可

## 方法2 Process Explorer
先确定盘符，假设是F盘  
Process Explorer，Find -> Find Handle or DLL..., 输入`F:\`，即可查看正在使用该盘的进程，关闭即可
