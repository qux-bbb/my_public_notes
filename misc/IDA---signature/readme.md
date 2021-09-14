# IDA---signature

## 简介
IDA 的 signature 用于给已知的系统函数或者库函数恢复名称  


## 常用库的signature
一个人收集的常用 signature：  
https://github.com/push0ebp/sig-database/  


## 手动制作signature
要用到 flair 工具  

总结为 2 步：
1. 生成模式文件：从库文件到 pat 文件
2. 生成signature文件：从 pat 文件 到 sig 文件

**第 1 步：**  
库文件在 windows 下是 `.lib` 结尾的文件，在 linux 下是 `.a` 结尾的文件  
相关工具：  
- plb.exe/plb。OMF库的解析器（Borland编译器常用）。  
- pcf.exe/pcf。COFF库的解析器（微软编译器常用）。  
- pelf.exe/pelf。ELF库的解析器（许多Unix系统常用）。  
- ppsx.exe/ppsx。Sony PlayStation PSX库的解析器。  
- ptmobj.exe/ptmobj。TriMedia库的解析器。  
- pomf166.exe/pomf166。Kiel OMF 166对象文件的解析器。  

**第 2 步：**  
相关工具：  
sigmake.exe/sigmake。  
可能会出现冲突，举例如下：  
```
.\libunicorn.sig: modules/leaves: 86/311, COLLISIONS: 11
```
需要编辑相应 .exc 文件，其文件头如下，需要删除：  
```
;--------- (delete these lines to allow sigmake to read this file)
; add '+' at the start of a line to select a module
; add '-' if you are not sure about the selection
; do nothing if you want to exclude all modules
```
对每组冲突添加一个 '+' 或 '-' 或什么都不做  

**命令举例：**  
```bat
pelf.exe hello.a hello.pat
sigmake.exe hello.pat hello.sig
```

**已知问题的解决：**  

生成库文件时，出现：  
```
Fatal [/mnt/c/MyFiles/libc.a] (__init_tls.lo): Unknown relocation type 42 (offset in section=0x3a).
```
加下参数：  
```
./flair/bin/linux/pelf -r42:58:0 libc.a musl.pat
```


## 相关项目
1. https://github.com/maroueneboubakri/lscan  
2. https://github.com/Maktm/FLIRTDB  
3. https://github.com/push0ebp/sig-database  


2020/5/18  
