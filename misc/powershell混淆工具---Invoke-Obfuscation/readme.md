# powershell混淆工具---Invoke-Obfuscation

https://github.com/danielbohannon  
这个人的混淆和检测混淆都有相关的项目，这里主要介绍 混淆项目  

项目地址：  
https://github.com/danielbohannon/Invoke-Obfuscation  

freebuf 相关介绍：  
https://www.freebuf.com/sectool/136328.html  

使用：  
```r
Import-Module ./Invoke-Obfuscation.psd1
Invoke-Obfuscation
```

简单命令记录：  
```r
# 设置脚本内容或路径
SET SCRIPTBLOCK script_block_or_command
SET SCRIPTPATH path_to_script_or_URL

# 显示当前选项
show options

# 导出混淆内容
out
```


2020/5/28  
