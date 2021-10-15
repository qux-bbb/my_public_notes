# exe版本信息语言代码相关

有时候`版本信息`里的`语言代码`可以看出一些国家相关的信息。  

```r
BLOCK "VarFileInfo" { VALUE "Translation", langID, charsetID . . . }
```

举例：  
```r
VS_VERSION_INFO.VarFileInfo.Translation:04b00409
```
0409: langID, 表示语言为美国英语  
04b0: charsetID, 即1200，表示字符集为Unicode  


langID,charsetID可能取值参考该链接：  
https://docs.microsoft.com/zh-cn/windows/win32/menurc/varfileinfo-block  


---
2021/10/15  
