# powershell---Measure-Command

powershell里的 Measure-Command 可以用来记录命令或脚本执行时间。  

```powershell
# 执行命令，记录执行时间
Measure-Command { sleep 3 }
# 执行脚本，记录执行时间
Measure-Command { python hello.py }
```


2023/12/11  
