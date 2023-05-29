# Unity3d逆向

## 基础做法
工具: dnSpy  

核心逻辑在 Assembly-CSharp.dll  

## il2cpp相关
il2cpp, Intermediate Language to cpp，中间语言到cpp  

如果使用了il2cpp技术, 无法恢复源代码, 可以使用Il2CppDumper工具, 该工具可以恢复很多符号：函数名/字符串等，然后导入ida，可使分析简单很多，不能直接拿到源代码
https://github.com/Perfare/Il2CppDumper  

用法:  
```sh
Il2CppDumper.exe <executable-file> <global-metadata>
```
<global-metadata>指的是global-metadata.dat, 该文件的头部特征码为"AF1BB1FA"  

执行命令后, 如果成功解析, 会生成dump.cs/一些dll/script.json, 会有函数声明, 但没有具体函数实现  

使用IDA加载符号：执行ida.py，json选择script.json即可  


---
2020/4/7  
