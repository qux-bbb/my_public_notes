# elf---PLT和GOT

## 解释
PLT :: Procedure Linkage Table :: 过程链接表  
GOT :: Global Offset Table :: 全局偏移表  

GOT 表用来将位置独立的地址重定向为绝对地址，在 ELF 文件中分为两个部分：  
.got，存储全局变量的引用。  
.got.plt，存储函数的引用。  
其相应的值由能够解析. rel.plt 段中的重定位的动态链接器来填写。  

PLT 表将位置独立的函数重定向到绝对地址，主要包括两部分：  
.plt，与常见导入的函数有关，如 read 等函数。  
.plt.got，与动态链接有关系。  


## 延迟绑定
一开始GOT（.got.plt）是空的，第一次调用外部函数时，通过PLT来填充GOT为有效地址，以后再次调用就直接通过GOT调用  
只有调用函数时才会被填充，这叫做*延迟绑定*  
这是一种避免浪费的机制  

延迟绑定可以在链接阶段被关掉（-z now），命令举例：  
```
gcc -z now -o test test.c
```
大概是这样的跳转关系：  
开延迟绑定： .plt -> .got.plt  
关延迟绑定：.plt.got -> .got  

可能意思就是开延迟绑定用的就是：.plt和.got.plt，关延迟绑定用的就是：.plt.got和.got  



## pwntools节对应关系
在pwntools中  
exe.plt['write'] 指的是 .plt节的内容  
exe.got['write']  指的是 .got.plt节的内容  
前者会跳向后者  


参考链接：https://ctf-wiki.github.io/ctf-wiki/executable/elf/elf-structure-zh/#sections  

感谢 逆向工程核心原理 群里的 atQ4n  


20201130  

2020/11/30  
