# Defender相关

Defender, 微软自带的病毒引擎。  

关于Defender的逆向：  
https://www.bilibili.com/video/BV1C94y1U7LP  

"C:\Program Files\Windows Defender\MsMpEng.exe"  
MsMpEng.exe, Microsoft Malware protect engine  

## 命令行扫描
"C:\Program Files\Windows Defender\MpCmdRun.exe"  

示例：
```r
"C:\Program Files\Windows Defender\MpCmdRun.exe" -Scan -ScanType 3 -File hello.exe
```

相关选项：
```r
   -Scan [-ScanType value]
        0  Default, according to your configuration
        1  Quick scan
        2  Full system scan
        3  File and directory custom scan

           [-File <path>]
                Indicates the file or directory  to be scanned, only valid for custom scan.
```

信息来源：腾讯元宝  


---
2024/10/20  
