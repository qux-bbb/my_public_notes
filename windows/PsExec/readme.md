# PsExec

keywords: PsTools 远程执行命令

PsExec 是一个可以远程连接其他Windows执行命令的工具，在SysinternalsSuite套件中。

下载链接: https://learn.microsoft.com/en-us/sysinternals/downloads/psexec


## 目标机器配置
1. 高级安全 Windows Defender 防火墙 -> 入站规则 -> 文件和打印机共享（SMB-In）, 根据情况启用“域”或“专用，公用”的规则
2. 以下内容保存为reg文件双击添加注册表项
```reg
Windows Registry Editor Version 5.00

[HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Windows\CurrentVersion\Policies\System]
"LocalAccountTokenFilterPolicy"=dword:00000001
```


## 使用示例
```bat
:: -i 是交互的意思
:: 启动cmd
.\PsExec.exe \\1.2.3.4 -u jack -i cmd

:: 查看网络连接
.\PsExec.exe \\1.2.3.4 -u jack -i netstat -ano

:: 查看进程路径
.\PsExec.exe \\1.2.3.4 -u jack -i wmic process where processid=<PID> get executablepath
```

如果中文乱码，可以修改编码之后再使用psexec
```bat
:: 936表示GBK
chcp 936
```


---
2025/9/8
