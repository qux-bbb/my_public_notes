# LLVM和OLLVM

## LLVM

官网: https://llvm.org  
github地址: https://github.com/llvm/llvm-project  

LLVM是构架编译器(compiler)的框架系统，以C++编写而成，可以简化编译器的实现，优化编译器的功能。  

LLVM和原来的全称（Low Level Virtual Machine）没什么关系。作者本来想写类似jvm的底层虚拟机，最后变成了这个编译器框架。  

传统编译器的3个阶段如下，比较耦合  
```
前端（Frontend）-- 优化器（Optimizer）-- 后端（Backend）
```

LLVM框架也分成3个阶段：  
```
前端（Frontend）-- 优化器（Optimizer）-- 后端（Backend）
```
1. 前端负责分析源代码，可以检查语法级错误，并构建针对语言的抽象语法树（AST，Abstract Syntax Tree），然后转换成LLVM的中间表示IR（Intermediate Representation）  
2. 优化器负责对中间表示IR操作进行优化  
3. 后端负责将优化好的IR解释成对应平台的机器码

这样的好处是，解耦合。  
要增加新的语言，只需要写新的前端。  
要增加处理器架构，只需要写新的后端。  

linux下从最新源码编译LLVM：  
```bash
git clone https://github.com/llvm/llvm-project.git
cd llvm-project
cmake -S llvm -B build
cd build
make
```
make的`-j` 参数表示并行数，据说可显著提高编译速度  
默认make用时 `4h 3m 9s`，  
添加 `-j8` 经历 `2h 15m 6s` 之后出错了，  
自己电脑是4核的，添加 `-j4` 经历2个小时后也还是出错了  


## OLLVM
OLLVM，Obfuscator-LLVM，基于LLVM框架的开源代码混淆器，通过LLVM的pass方法来混淆原程序。  
项目地址：https://github.com/obfuscator-llvm/obfuscator  
项目中包含3个相对独立的LLVM pass：  
1. Instructions Substitution，指令替换
2. Bogus Control Flow，伪造控制流
3. Control Flow Flattening，控制流平坦化


OLLVM的混淆操作就是在中间表示IR层，通过编写pass来混淆IR，然后后端依据IR来生成的目标代码也就被混淆了。得益于LLVM的设计，OLLVM适用LLVM支持的所有语言（C,C++,Objective-C,Ada和Fortran）和目标平台（x86,x86-64.PowerPC-64,ARM,Thumb,SPARC,Alpha,CellSPU,MIPS,MSP430,SystemZ,和XCore）。


## 其他
这里介绍了怎么配置visual studio使用LLVM：  
https://llvm.org/builds/  
提到的下载链接太慢，可以从这里下载：  
https://github.com/llvm/llvm-project/releases  

如果要做LLVM的工作，估计就是改LLVM的源代码，重新编译这套工具吧  


## 参考链接
1. https://llvm.org/  
2. https://www.jianshu.com/p/1367dad95445  
3. https://blog.csdn.net/yayaayaya123/article/details/83993041  
4. https://blog.csdn.net/water1307/article/details/81390175  
5. https://github.com/obfuscator-llvm/obfuscator  
6. https://www.jianshu.com/p/e0637f3169a3


2020/11/24  
