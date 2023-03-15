# powershell---计算文件hash

```r
Get-FileHash [-Path] <string[]> [-Algorithm {SHA1 | SHA256 | SHA384 | SHA512 | MACTripleDES | MD5 | RIPEMD160}]  [<CommonParameters>]
```

示例：  
```powershell
# 默认计算SHA256
Get-FileHash hello.txt
```

输出：  
```r
Algorithm       Hash                                                                   Path
---------       ----                                                                   ----
SHA256          7F83B1657FF1FC53B92DC18148A1D65DFC2D4B1FA3D677284ADDD200126D9069       D:\recent\tmp\hello.txt
```

其它用法：  
```powershell
# 指定某种算法
Get-FileHash -Algorithm SHA1 hello.txt
# 只输出hash字符串
(Get-FileHash -Algorithm SHA1 hello.txt).Hash
```


2023/3/15  
