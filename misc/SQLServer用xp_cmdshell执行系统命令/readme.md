# SQLServer用xp_cmdshell执行系统命令

keywords: SQL Server

启用 xp_cmdshell
```sql
-- 1. 允许修改高级选项
EXEC sp_configure 'show advanced options', 1;
RECONFIGURE;
GO

-- 2. 启用 xp_cmdshell
EXEC sp_configure 'xp_cmdshell', 1;
RECONFIGURE;
GO
```

执行系统命令
```sql
-- 查看当前目录文件
EXEC xp_cmdshell 'dir C:\';

-- 创建一个新的文件夹
EXEC xp_cmdshell 'mkdir C:\Temp\SQLTest';

-- 执行 PowerShell 命令
EXEC xp_cmdshell 'powershell -Command "Get-Process | Select-Object -First 5"';
```
