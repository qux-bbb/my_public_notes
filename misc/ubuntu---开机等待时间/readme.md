# ubuntu---开机等待时间

keywords: 开机 启动 等待时间  

ubuntu启动后，会等待一段时间进入系统，默认开机等待时间是10秒，太长了。  

要修改的文件: `/etc/default/grub`  

修改项：  
`GRUB_TIMEOUT=10 # 等待选择时间，单位是秒，自己随便设`  

修改完之后需要运行命令: `update-grub`, 使修改生效  


2017/9/2  
