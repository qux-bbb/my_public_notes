# 硬盘占用解决方法

keywords: U盘 移动硬盘 文件 占用  

只是记一下相关信息，还没找到彻底解决的方法  

移除移动硬盘时弹出消息显示以下文件被占用：  
```r
E:\$Extend\$RmMetadata\$TxfLog\$TxfLog.blf
E:\$Extend\$RmMetadata\$TxfLog\$TxfLogContainer00000000000000000001
E:\$Extend\$RmMetadata\$TxfLog\$TxfLogContainer00000000000000000002
E:\$Extend\$RmMetadata\$Txf:$I30:$INDEX_ALLOCATION
```

在移动硬盘鼠标右键查看属性，取消勾选"除了文件属性外，还允许索引此驱动器上文件的内容"  
关闭所有文件管理器  

还无法移除时，使用PowerToys里的File Locksmith工具看是否有文件占用  


2024/4/22  
