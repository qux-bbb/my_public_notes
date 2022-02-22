# dnspy

## 简介
反编译，调试.NET，很强大  

github地址: https://github.com/0xd4d/dnSpy  
dnspy原项目不再开发了，有人fork了项目继续开发: https://github.com/dnSpyEx/dnSpy  

## 调试
如果要调试，注意:  
32位程序使用32位dnspy打开  
64位程序使用64位dnspy打开  

还要安装.net4.0：  
https://www.microsoft.com/zh-cn/download/details.aspx?id=17718  

部分.net exe会解密出一个.net dll，但不会落地，在内存执行  
分析AgentTesla过程中，确定这样可以在相应dll中下断点继续调试：  
在执行完该语句后`Assembly assembly = Thread.GetDomain().Load(rawAssembly);`, dll已加载到内存中，  
此时 调试 -> 窗口 -> 模块，即可看到相应模块，选中，右键 转到模块，然后就能在模块中下断点继续调试了  