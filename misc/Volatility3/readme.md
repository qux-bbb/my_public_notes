# Volatility3

Volatility3是一个开源的内存取证工具，使用python3重写。  

官网: https://www.volatilityfoundation.org/  
github地址: https://github.com/volatilityfoundation/volatility3  

官方给的安装方法：  
```r
git clone https://github.com/volatilityfoundation/volatility3.git
cd volatility3
pip3 install -r requirements.txt
# 输出使用帮助
python3 vol.py -h
```

官方维护了一个python模块，可以这么安装：  
```r
pip install volatility3
```


## cheatsheet
系统信息：  
```r
vol.py -f “/path/to/file” windows.info
```

进程信息：  
```r
# PSLIST
vol.py -f “/path/to/file” windows.pslist
vol.py -f “/path/to/file” windows.psscan
vol.py -f “/path/to/file” windows.pstree

# PROCDUMP
vol.py -f “/path/to/file” -o “/path/to/dir” windows.dumpfiles ‑‑pid <PID>

# MEMDUMP
vol.py -f “/path/to/file” -o “/path/to/dir” windows.memmap ‑‑dump ‑‑pid <PID>

# HANDLES
vol.py -f “/path/to/file” windows.handles ‑‑pid <PID>

# DLLS
vol.py -f “/path/to/file” windows.dlllist ‑‑pid <PID>

# CMDLINE
vol.py -f “/path/to/file” windows.cmdline
```

网络信息：  
```r
vol.py -f “/path/to/file” windows.netscan
vol.py -f “/path/to/file” windows.netstat
```

注册表信息：  
```r
# HIVELIST
vol.py -f “/path/to/file” windows.registry.hivescan
vol.py -f “/path/to/file” windows.registry.hivelist

# PRINTKEY
vol.py -f “/path/to/file” windows.registry.printkey
vol.py -f “/path/to/file” windows.registry.printkey ‑‑key “Software\Microsoft\Windows\CurrentVersion”

# HIVEDUMP
# 无，可以使用带有偏移量的filedump提取注册表配置单元
```

文件信息：  
```r
# FILESCAN
vol.py -f “/path/to/file” windows.filescan

# FILEDUMP
vol.py -f “/path/to/file” -o “/path/to/dir” windows.dumpfiles
vol.py -f “/path/to/file” -o “/path/to/dir” windows.dumpfiles ‑‑virtaddr <offset>
vol.py -f “/path/to/file” -o “/path/to/dir” windows.dumpfiles ‑‑physaddr <offset>
```

其它：  
```r
# MALFIND
vol.py -f “/path/to/file” windows.malfind

# YARASCAN
vol.py -f “/path/to/file” windows.vadyarascan ‑‑yara-rules <string>
vol.py -f “/path/to/file” windows.vadyarascan ‑‑yara-file “/path/to/file.yar”
vol.py -f “/path/to/file” yarascan.yarascan ‑‑yara-file “/path/to/file.yar”
```

## 原链接
https://blog.onfvp.com/post/volatility-cheatsheet/  


---
2022/6/28  
