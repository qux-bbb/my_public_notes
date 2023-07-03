# ASPack---定位oep

ASPack, Advanced Self-contained Packer, 一种和UPX类似的PE压缩加壳工具。  
官网: http://www.aspack.com/  

和UPX类似，也可以使用esp定律找到oep。  

流程  
1. 执行压栈: `pushad`  
2. 单击esp寄存器的值，右键转到内存，然后右键设置硬件访问断点  
3. F9运行，程序断下后，下面的ret就是返回到oep  
4. 取消硬件访问断点，执行ret指令后，就到了oep  


2023/7/3  
