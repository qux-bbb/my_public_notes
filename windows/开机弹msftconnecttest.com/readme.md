# 开机弹msftconnecttest.com

有时候windows开机会弹出网页msftconnecttest.com redirect，看名字就知道这是微软在测试网络连接状况，不过每次开机都直接打开，挺烦的，修改注册表就可以关掉了  

regedit打开注册表之后，在  
`HKEY_LOCAL_MACHINE\SYSTEM\ControlSet001\Services\NlaSvc\Parameters\Internet`  
下有一项：`EnableActiveProbing`  
值改为0即可  

如果觉得那个路径太长，可以直接 编辑→查找：  
查找目标为：`msftconnecttest`  
多选框只选数据  
搜索结果下就能看到那一项  


20180304  
