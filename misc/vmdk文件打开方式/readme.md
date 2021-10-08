# vmdk文件打开方式

## 打开方式
vmdk, VMWare Virtual Machine Disk Format, 是虚拟机VMware创建的虚拟硬盘格式。  

该类型文件用vmware打开，但不是直接打开。  
因为是一个磁盘文件，所以需要建一个虚拟机，新建虚拟机时要选"自定义"、"稍后安装操作系统"、"使用现有虚拟磁盘"(选择vmdk文件)，这样建完之后理论上就可以打开了。  

另一种直接浏览文件的方式，使用WinImage工具可以直接解析vmdk文件，提取想要的文件，比如注册表文件。  
http://www.winimage.com/download.htm  


## 参考链接
https://baike.baidu.com/item/vmdk/3369989  
https://jingyan.baidu.com/article/4853e1e54621591909f7262c.html  
https://blog.csdn.net/do2jiang/article/details/4982101  


2021/5/1  
