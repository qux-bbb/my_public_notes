# win10---永久关闭windows defender

修改安全中心设置配合修改组策略配置可以永久关闭windows defender  


左下角 Win 图标，鼠标右键 -> 设置 -> 更新和安全 -> Windows 安全中心 -> 病毒和威胁防护 -> 管理设置  
关闭"实时保护"、"云提供的保护"、"自动提交样本"、"篡改防护"  

左下角搜索"gpedit"，打开"编辑组策略"  
计算机配置 -> 管理模板 -> Windows 组件 -> Windows Defender 防病毒程序，右边选择"关闭 Windows Defender 防病毒程序"，配置为"已启用"  
计算机配置 -> 管理模板 -> Windows 组件 -> Windows Defender 防病毒程序 -> 实时保护，右边选择"关闭实时保护"，配置为"已启用"  

重启即可  


原链接：https://www.jianshu.com/p/93d7b41ce74f  


2020/9/1  
