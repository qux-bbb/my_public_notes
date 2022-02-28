# vmpdump

github地址: https://github.com/0xnobody/vmpdump  

基于VTIL的动态VMP转储程序和导入修复程序。VMProtect 3.X x64 可用。  

使用方法：  
```r
VMPDump.exe <Target PID> "<Target Module>" [-ep=<Entry Point RVA>] [-disable-reloc]
    <Target PID>：目标进程的ID，十进制或十六进制形式。
    <Target Module>：要转储并修复的模块名称。如果针对 process image 模块，可以设置空字符串（""）。
    [-ep=<Entry Point RVA>]：可选，十六进制形式的入口点RVA。VMPDump会用这个值覆盖 optional header 中的入口点。
    [-disable-reloc]：可选，用于指示VMPDump在输出映像中标记relocs已被剥离，从而强制映像在转储的ImageBase中加载。如果需要可运行的转储程序，该选项很有用。
```

示例：  
```r
VMPDump.exe 3000 ""
```

经实际测试，针对x64程序的效果较好，x86程序基本没有变化。  

感谢 熊猫正正  

其它  
VTIL, Virtual-machine Translation Intermediate Language  
https://github.com/vtil-project/VTIL-Core  


2022/2/28  
