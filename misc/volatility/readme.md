# Volatility

Volatility是一个开源的内存取证工具。  
这里的Volatility指Volatility2，最新版是2.6，使用python2编写，不兼容python3。  

官网: https://www.volatilityfoundation.org/  
github地址: https://github.com/volatilityfoundation/volatility  

可以下载压缩包、python模块安装包、或者独立的可执行文件  
!!!如果没有特殊需求，强烈推荐使用独立的可执行文件(下文的命令把“vol.py”换成“volatility_2.6_win64_standalone.exe”)，非常方便  

hed(非官方)维护了一个python模块，可以这么安装：  
```r
pip install volatility261
```


## cheatsheet
系统信息：  
```r
vol.py -f “/path/to/file” imageinfo
# 如果使用imageinfo找不到合适的配置文件，则可以使用kdbgscan收集其他信息
vol.py -f “/path/to/file” kdbgscan
```

进程信息：  
```r
# PSLIST
vol.py -f “/path/to/file” ‑‑profile <profile> pslist
vol.py -f “/path/to/file” ‑‑profile <profile> psscan
vol.py -f “/path/to/file” ‑‑profile <profile> pstree
vol.py -f “/path/to/file” ‑‑profile <profile> psxview

# PROCDUMP
vol.py -f “/path/to/file” ‑‑profile <profile> procdump -p <PID> ‑‑dump-dir=“/path/to/dir”

# MEMDUMP
vol.py -f “/path/to/file” ‑‑profile <profile> memdump -p <PID> ‑‑dump-dir=“/path/to/dir”

# HANDLES
vol.py -f “/path/to/file” ‑‑profile <profile> handles -p <PID>

# DLLS
vol.py -f “/path/to/file” ‑‑profile <profile> dlllist -p <PID>

# CMDLINE
vol.py -f “/path/to/file” ‑‑profile <profile> cmdline
vol.py -f “/path/to/file” ‑‑profile <profile> cmdscan
vol.py -f “/path/to/file” ‑‑profile <profile> consoles
```

网络信息：  
```r
# NETSCAN
vol.py -f “/path/to/file” ‑‑profile <profile> netscan
vol.py -f “/path/to/file” ‑‑profile <profile> netstat
# XP/2003 SPECIFIC
vol.py -f “/path/to/file” ‑‑profile <profile> connscan
vol.py -f “/path/to/file” ‑‑profile <profile> connections
vol.py -f “/path/to/file” ‑‑profile <profile> sockscan
vol.py -f “/path/to/file” ‑‑profile <profile> sockets
```

注册表信息：  
```r
# HIVELIST
vol.py -f “/path/to/file” ‑‑profile <profile> hivescan
vol.py -f “/path/to/file” ‑‑profile <profile> hivelist

# PRINTKEY
vol.py -f “/path/to/file” ‑‑profile <profile> printkey
vol.py -f “/path/to/file” ‑‑profile <profile> printkey -K “Software\Microsoft\Windows\CurrentVersion”

# HIVEDUMP
vol.py -f “/path/to/file” ‑‑profile hivedump -o <offset>
```

文件信息：  
```r
# FILESCAN
vol.py -f “/path/to/file” ‑‑profile <profile> filescan

# FILEDUMP
vol.py -f “/path/to/file” ‑‑profile <profile> dumpfiles ‑‑dump-dir=“/path/to/dir”
vol.py -f “/path/to/file” ‑‑profile <profile> dumpfiles ‑‑dump-dir=“/path/to/dir” -Q <offset>
vol.py -f “/path/to/file” ‑‑profile <profile> dumpfiles ‑‑dump-dir=“/path/to/dir” -p <PID>
```

其它：  
```r
# MALFIND
vol.py -f “/path/to/file” ‑‑profile <profile> malfind

# YARASCAN
vol.py -f “/path/to/file” yarascan -y “/path/to/file.yar”
```

## 原链接
https://blog.onfvp.com/post/volatility-cheatsheet/  


---
2022/6/28  
