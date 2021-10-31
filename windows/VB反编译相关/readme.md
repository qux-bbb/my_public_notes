# VB反编译相关

## vb exe识别
导入表有 dll 名字是：MSVBVM50.DLL 或 MSVBVM60.DLL，那就基本说明这个exe是vb生成的  


## VB 3/4反编译器
Dodi's VB 3/4 Disassembler  


## VB6.0一些点
实际上的数据计算和比较是在 msvbvm60.dll 及 oleaut32.dll 中完成的。  
msvbvm60.dll 中包含的函数名总是以“__vba”或“rtc”开头，而 oleaut32.dll 函数名以“var”开头。  
对于函数的作用，一般可以按照函数名从右往左理解，例如“__vbaI2Str”表示字符串转换为整数。  


## 调试器/反编译器
VB 5/6的p-code伪编译模式使得直接调试很难理解，该模式下大部分的代码都是跳到相关dll文件执行的  
反编译器：VB.Decompiler VBParser exedec  
调试器：WKTVBDE(在看雪可下载)  

VB.Decompiler 的反编译效果最好，在52破解可下载到比较新的  

WKTVBDE 看雪有专门的介绍，使用需要注意以下几点:  
1. 将目标软件复制到WKTVBDebugger安装目录里调试，即与Loader.exe同一目录
2. 将安装目录的WKTVBDE.dll，bdasmdll.dll文件复制到系统目录里

如果还是失败，搜一下看雪的书《加密与解密》提供的文档  


## 区分native编译和p-code编译
有一个很简单的方法，使用IDA打开，Search->Text(Alt+T)，搜索`mov     ebp, esp`，如果能找到，那就是 native编译，否则就是p-code编译  

原理：  
native编译，会有很明显的函数入口，众所周知一般的函数入口为：  
```r
push    ebp
mov     ebp, esp
```

native编译样本动态调试参数相关  
参数会压栈，但不是直接对应数据，而是一个结构  


## IDA与VB样本
IDA可以稍微整理一下native模式的vb样本，默认无法识别具体函数  
搜索函数的入口点`mov     ebp, esp`，确定函数开头，  
Edit -> Functions -> Create function， 或者直接按快捷键P， 即可识别一个函数  
配合VB.Decompiler效果更佳  


## 相关助记符
```r
BranchF             条件跳转，栈的值是0则跳转
BranchT             条件跳转，站的值是FFFFFFFh(-1)则跳转
Branch              无条件跳转
EqVarBool           比较，将比较结果(-1或0)压栈
LitI2_Byte          将数据压入栈
ConcatStr           字符串连接
FLdZeroAd/CvarStr   取字符串
```

## VB的Messagebox
rtcMsgBox  


## 比较模式
1. 字符串(String)比较  
    明码比较，用到的断点：__vbaStrComp __vbaStrCmp  
2. 变量(Variant)比较  
    用到的断点： __vbaVarTstEq  
3. 字节(Byte)比较  
    使用cmp指令  
4. 整型(Integer)比较  
    使用cmp指令  
5. 长整型(Long)比较  
    使用cmp指令，只能用来比较数字  
6. 单精度实数(Single)比较  
    使用cmp指令，只能用来比较数字，但可以将字符串转为实数进行比较  
7. 双精度(Double)比较  
    类似单精度  
8. 货币(Currency)比较  
    类似单精度


---
2020/7/15  
