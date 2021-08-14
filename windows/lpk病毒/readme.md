# lpk病毒

windows下的每个exe程序执行的时候都需要加载系统目录下的lpk.dll，用于某些功能。  

lpk病毒把自己复制到每个有exe的文件夹和zip、rar压缩包内，利用dll加载优先级机制，达到只要有exe执行，lpk病毒就能启动的目的。  

分析的一个lpk病毒把自己的功能写在了DllEntryPoint函数内  
f7e6385b09f867527e02990351fab912  

按Visual Studio的dll生成方式，自己是不能操作DllEntryPoint函数的，搞不清楚它是怎么实现的 &&&&&&&  


2021/8/14  
