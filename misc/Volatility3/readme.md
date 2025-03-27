# Volatility3

Volatility3是一个开源的内存取证工具，使用python3重写，运行要求Python 3.8.0及以上版本。  
感觉没有2.6好用  

官网: https://www.volatilityfoundation.org/  
github地址: https://github.com/volatilityfoundation/volatility3  

官方维护了一个python模块，可以这么安装：  
```r
pip install volatility3
```

如果想使用最新的稳定版，官方建议这样安装：  
```r
git clone https://github.com/volatilityfoundation/volatility3.git
cd volatility3/
python -m venv venv && . venv/bin/activate
pip install -e .[dev]
```

如果是windows，安装后使用 `venv\Scripts\vol.exe`, 避免和系统的vol命令出现冲突  


## cheatsheet
系统信息：  
```r
vol -f “/path/to/file” windows.info
```

进程信息：  
```r
# PSLIST
vol -f “/path/to/file” windows.pslist
vol -f “/path/to/file” windows.psscan
vol -f “/path/to/file” windows.pstree

# PROCDUMP
vol -f “/path/to/file” -o “/path/to/dir” windows.dumpfiles ‑‑pid <PID>

# MEMDUMP
vol -f “/path/to/file” -o “/path/to/dir” windows.memmap.Memmap ‑‑dump ‑‑pid <PID>

# HANDLES
vol -f “/path/to/file” windows.handles ‑‑pid <PID>

# DLLS
vol -f “/path/to/file” windows.dlllist ‑‑pid <PID>

# CMDLINE
vol -f “/path/to/file” windows.cmdline
```

网络信息：  
```r
vol -f “/path/to/file” windows.netscan
vol -f “/path/to/file” windows.netstat
```

注册表信息：  
```r
# HIVELIST
vol -f “/path/to/file” windows.registry.hivescan
vol -f “/path/to/file” windows.registry.hivelist

# PRINTKEY
vol -f “/path/to/file” windows.registry.printkey
vol -f “/path/to/file” windows.registry.printkey ‑‑key “Software\Microsoft\Windows\CurrentVersion”

# HIVEDUMP
# 无，可以使用带有偏移量的filedump提取注册表配置单元
```

文件信息：  
```r
# FILESCAN
vol -f “/path/to/file” windows.filescan

# FILEDUMP
vol -f “/path/to/file” -o “/path/to/dir” windows.dumpfiles
vol -f “/path/to/file” -o “/path/to/dir” windows.dumpfiles ‑‑virtaddr <offset>
vol -f “/path/to/file” -o “/path/to/dir” windows.dumpfiles ‑‑physaddr <offset>
```

其它：  
```r
# MALFIND
vol -f “/path/to/file” windows.malfind

# YARASCAN
vol -f “/path/to/file” windows.vadyarascan ‑‑yara-rules <string>
vol -f “/path/to/file” windows.vadyarascan ‑‑yara-file “/path/to/file.yar”
vol -f “/path/to/file” yarascan.yarascan ‑‑yara-file “/path/to/file.yar”
```

## 原链接
https://blog.onfvp.com/post/volatility-cheatsheet/  


---
2022/6/28  
