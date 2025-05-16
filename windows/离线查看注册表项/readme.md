# 离线查看注册表项

注册表相关文件：
```r
# 系统注册表文件
C:\Windows\System32\config\
DEFAULT, HKEY_USERS\.DEFAULT, 默认用户配置
SAM, HKEY_LOCAL_MACHINE\SAM, 安全账户管理
SECURITY, HKEY_LOCAL_MACHINE\SECURITY, 安全策略
SOFTWARE, HKEY_LOCAL_MACHINE\SOFTWARE, 已安装的软件配置
SYSTEM, HKEY_LOCAL_MACHINE\SYSTEM, 系统硬件和服务配置

# 对应 HKEY_CURRENT_USER
C:\Users\<用户名>\NTUSER.DAT
```


## OfflineRegistryView
https://www.nirsoft.net/utils/offline_registry_view.html

小巧，但只能给定路径查看一个结果


## Registry Explorer
https://ericzimmerman.github.io/#!index.md

类似regedit的体验，除了不能直接输入路径跳转

需要额外下载安装.NET环境，打开软件会提示


---
2025/5/16
