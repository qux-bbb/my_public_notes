# 检查依赖工具

```r
确定您的Windows应用程序依赖于那些DLL的最全面的方式是使用随VisualC++提供的依赖项查看器（Depends.exe）打开该应用程序。
Depends.exe安装在VS(6.0/2005/2008/2010等)安装目录下的CommonX\Tools\Bin中（X根据安装VS的版本不同而不同）。
请注意，VS6.0是默认安装该工具的，但是之后的版本，只有当您选择Win32 Windows SDK工具（它位于Visual C++自定义安装的“Visual C++工具”类别中）时，才会安装Depends.exe。

当没有安装Depends.exe时，您可以从 http://www.dependencywalker.com/ 网站下载DependencyWalker。
DependencyWalker是一个扫描所有32位和64位Windows模块的免费工具，它创建一个所有依赖模块的层次树。
对于每个找到的模块，它会列出所有被该模块导出的函数，这些函数实际上会被其它模块所调用。
    X86下载网址: http://www.dependencywalker.com/depends22_x86.zip
    X64下载网址: http://www.dependencywalker.com/depends22_x64.zip

Linux下依赖性检查使用lld(List Library Depends)命令，如下：
lld execute-file

————————————————
版权声明：本文为CSDN博主「fan_hai_ping」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/fan_hai_ping/article/details/8020054
```


2020/7/2  
