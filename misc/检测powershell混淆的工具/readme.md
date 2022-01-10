# 检测powershell混淆的工具

只是检测，没有去混淆。  

## Revoke-Obfuscation
项目地址：  
https://github.com/danielbohannon/Revoke-Obfuscation  
生成 ATS，刷权重，最后得出分数  
生成ATS使用了原生接口 System.Management.Automation.Language.Parser  

感觉有用的使用方法摘要：  
```r
IMPORT FRAMEWORK :: Import-Module .\Revoke-Obfuscation.psd1

FUNCTION #2 :: Measure-RvoObfuscation
This function is the heart and soul of this framework for detecting obfuscated PowerShell scripts/commands. Simply pipeline into or point the function to PowerShell scripts, commands or Get-RvoScriptBlock results.

    EXAMPLE 1 (URL):
    $obfResults = Measure-RvoObfuscation -Url 'http://bit.ly/DBOdemo1' -Verbose

    EXAMPLE 2 (Directory of scripts):
    $obfResults = Get-Content -Path .\Demo\DBOdemo*.ps1 -Raw | Measure-RvoObfuscation -Verbose -OutputToDisk

    EXAMPLE 3 (Chaining both functions together):
    $obfResults = Get-ChildItem .\Demo\*.evtx | Get-RvoScriptBlock | Measure-RvoObfuscation -Verbose -OutputToDisk

RESULTS :: When the -OutputToDisk switch is used then OBFUSCATED results will be output to .\Results\Obfuscated\, but all results (obfuscated, not obfuscated and whitelisted) will be included in the PSCustomObject returned by Measure-RvoObfuscation. Check out all of the metadata returned in $obfResults
```


## powershellprofiler

混淆识别工具：  
https://github.com/pan-unit42/public_tools/tree/master/powershellprofiler  
尝试解码或解密内容，然后进行特征匹配  
提到的文章：  
https://unit42.paloaltonetworks.com/practical-behavioral-profiling-of-powershell-scripts-through-static-analysis-part-1/  

python3 项目  

使用命令举例：  
```r
py -3 PowerShellProfiler.py -f malicious.ps1 -d
```

帮助内容  
```r
usage: PowerShellProfiler.py [-h] -f <file_name> [-d]

PowerShellProfiler analyzes PowerShell scripts statically to identify and
score behaviors.

optional arguments:
  -h, --help            show this help message and exit
  -f <file_name>, --file <file_name>
                        PowerShell Script to behaviorally profile
  -d, --debug           Enables debug output
```


---
2020/5/28  
