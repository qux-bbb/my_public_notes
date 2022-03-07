# powershell策略设置

keywords: 允许执行脚本  

最直接无脑的设置可执行脚本，管理员权限打开powershell窗口，执行该命令即可，一般没什么好担心的：  
```r
Set-ExecutionPolicy Unrestricted
```

默认情况下，windows不允许执行powershell脚本，需要设置策略。  
```r
# 查看当前执行策略
Get-ExecutionPolicy
# 查看所有执行策略
Get-ExecutionPolicy -List
# 设置执行策略
Set-ExecutionPolicy -ExecutionPolicy <PolicyName>
# 设置执行策略，指定范围
Set-ExecutionPolicy -ExecutionPolicy <PolicyName> -Scope <scope>
# 清除策略举例
Set-ExecutionPolicy -ExecutionPolicy Undefined -Scope LocalMachine
```

PolicyName 可能的取值和含义  
1. AllSigned.  
Requires that all scripts and configuration files are signed by a trusted publisher, including scripts written on the local computer.  

2. Bypass.  
Nothing is blocked and there are no warnings or prompts.  

3. Default.  
Sets the default execution policy. Restricted for Windows clients or RemoteSigned for Windows servers.

4. RemoteSigned.  
Requires that all scripts and configuration files downloaded from the Internet are signed by a trusted publisher. The default execution policy for Windows server computers.  

5. Restricted.  
Doesn't load configuration files or run scripts. The default execution policy Windows client computers.  

6. Undefined.   
No execution policy is set for the scope. Removes an assigned execution policy from a scope that is not set by a Group Policy. If the execution policy in all scopes is Undefined, the effective execution policy is Restricted.  

7. Unrestricted.  
Beginning in PowerShell 6.0, this is the default execution policy for non-Windows computers and can't be changed. Loads all configuration files and runs all scripts. If you run an unsigned script that was downloaded from the internet, you're prompted for permission before it runs.  


scope 可能的取值和含义  
1. MachinePolicy.  
Set by a Group Policy for all users of the computer.  
2. UserPolicy.  
Set by a Group Policy for the current user of the computer.  
3. Process.  
Affects only the current PowerShell session.  
4. CurrentUser.  
Affects only the current user.  
5. LocalMachine.  
Default scope that affects all users of the computer.  


举例:  
```r
# 当前session随意执行
Set-ExecutionPolicy -ExecutionPolicy Bypass -Scope Process
```

参考:  
1. https://docs.microsoft.com/zh-cn/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-6  


2020/5/25  
