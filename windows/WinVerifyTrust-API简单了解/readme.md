# WinVerifyTrust-API简单了解

WinVerifyTrust 是一个用于验证签名的API, 官方文档地址:  
https://docs.microsoft.com/en-us/windows/win32/api/wintrust/nf-wintrust-winverifytrust  

ReactOS是个好东西，直接看源码吧：  
https://github.com/reactos/reactos/blob/d296bbebbef07e1a9eab79dd6f503e20d38fdeeb/dll/win32/wintrust/wintrust_main.c  
后面的内容可以忽略。  

官方只给了WinVerifyTrust API 的定义, 但内部实现并没有描述, 我们可以通过IDA看一下它的伪代码  

WinVerifyTrust 在 wintrust.dll 中, windows路径为:  
```r
64位: C:\Windows\System32\wintrust.dll
32位: C:\Windows\SysWOW64\wintrust.dll
```
直接用IDA去看, 很多函数都没有名字, 有必要先把pdb文件下载好(我下的是32位dll的pdb文件)  


下载pdb文件的过程比较曲折, 描述一下:  
1. 使用x64dbg打开wintrust.dll
2. 切换到`符号`标签页, 选中wintrust.dll
3. 选中`wintrust.dll`模块, 右键选择`下载此模块的符号信息`

如果第3步下载成功了, 可以根据下方日志显示的本地位置拿到pdb文件, 如果没有下载成功, 也可以根据日志的下载链接手动下载.  我这里没有下载成功, 日志中的链接为:  
`https://msdl.microsoft.com/download/symbols/wintrust.pdb/D4263D1DBEC3B0AC2D6B03BEFC8020C51/wintrust.pdb`  
自己下载就可以了，下载之后可以复制到日志显示的对应本地位置, 调试就很方便    

用IDA打开wintrust.dll, 然后手动load下载好的wintrust.pdb, 接着IDA的F5大法, 就可以愉快地看伪代码了  

**如果想要调试怎么办?**  
微软的SysinternalsSuite工具集中有一个sigcheck.exe, 主功能就是调用WinVerifyTrust API实现的, 所以可以调试它  
1. 随意找一个有签名的PE文件, 比如为hello.exe  
2. x64dbg打开sigcheck.exe
3. 文件->改变命令行, 设置为:
    `"C:\Users\user_name\Desktop\sigcheck.exe" C:\Users\user_name\Desktop\hello.exe`
4. 给WinVerifyTrust下断点, F9运行

这样就可以调试了  


---
2020/5/13  
