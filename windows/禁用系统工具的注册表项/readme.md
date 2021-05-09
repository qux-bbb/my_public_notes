# 禁用系统工具的注册表项

可以通过以下注册表项禁用cmd，注册表编辑器，任务管理器  

```
".*\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Policies\\\\System\\DisableCmd$"
".*\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Policies\\\\System\\DisableRegistryTools$"
".*\\\\SOFTWARE\\\\Microsoft\\\\Windows\\\\CurrentVersion\\\\Policies\\\\System\\\\DisableTaskMgr$"
```

来自cuckoo signature  


20200928  
