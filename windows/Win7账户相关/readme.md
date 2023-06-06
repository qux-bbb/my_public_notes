# Win7账户相关

Windows账户查看
- 用户组管理查看，不可靠
- 命令行查看，不可靠
- 注册表HKLM-SAM|SAM|Domains|Accounts|Users&Names 查看，非常可靠

Windows隐藏账户添加  
1. 添加账户`Hider$`(添加`$`符号，在cmd中不显示)
2. 从注册表导出Hider的键值，Names键值和对应的数字项
3. 删除用户
4. 导入之前导出的2个键即可(注册表导入法，在计算机管理窗口中，不显示)


2019/9/12  
