# 安装SQL Server

SQL Server支持Windows和Linux操作系统，这里记一下在Windows的安装关键点。

```
在这里下载SQL Server Express版
https://www.microsoft.com/zh-cn/sql-server/sql-server-downloads

如果要设置使用密码登陆
安装类型选择“Custom”
数据库引擎配置 -> 服务器配置 -> 身份验证模式，切换为“混合模式(SQL Server 身份验证和 Windows 身份验证)”，设置sa帐户的密码

如果要让数据库默认使用固定的1433端口
需要在“实例配置”页面切换为“默认实例”

默认数据库未开放端口，如果要开放端口
需要使用“SQL Server 配置管理器”
1. SQL Server 网络配置 -> 协议 -> TCP/IP，右键启用
2. SQL Server 服务 -> SQL Server (MSSQLSERVER)，右键重启

如果要通过ip地址访问数据库
高级安全Windows Defender防火墙，需要在入站规则中添加允许TCP端口策略
```
