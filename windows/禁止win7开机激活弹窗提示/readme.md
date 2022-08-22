# 禁止win7开机激活弹窗提示

激活弹窗和一个服务有关：  
```r
服务名称: sppsvc
显示名称: Software Protection
描述: 启用 Windows 和 Windows 应用程序的数字许可证的下载、安装和实施。如果禁用该服务，操作系统和许可的应用程序可能以通知模式运行。强烈建议您不要禁用软件保护服务。
可执行文件路径: C:\Windows\system32\sppsvc.exe
```
停止服务后将启动类型设置为"禁用"即可禁止开机弹激活窗口。  

因为是服务，所以也可以通过注册表项设置：  
```r
REG add "HKLM\SYSTEM\CurrentControlSet\services\sppsvc" /v Start /t REG_DWORD /d 4 /f
```
启动类型和数字关系：  
```r
Automatic   2
Manual      3
Disabled    4
```



原链接:  
1. https://computerstepbystep.com/software_protection_service.html
2. https://superuser.com/questions/1127298/how-do-i-disable-the-windows-7-activation-system-in-this-situation


2022/8/23  
