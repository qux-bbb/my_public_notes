# windbg---获取powershell反混淆脚本

这方法太繁琐而且效果不好，更好的方法参考笔记 `# 获取powershell反混淆脚本`  

使用 windbg 配合 SOS 调试扩展可以得到相对比较少混淆的 powershell 脚本，如果是多层混淆的脚本，可以节省好几层处理  
原理：iex 执行时有一个参数是 powershell 脚本内容，可以直接拿出来  

## 环境配置
SOS.dll 是一个辅助调试扩展，随 `.NET Framework` 安装，我的位置：  
```r
C:\Windows\Microsoft.NET\Framework64\v4.0.30319\SOS.dll
C:\Windows\Microsoft.NET\Framework\v4.0.30319\SOS.dll
```
分别是 64 位 和 32 位  

以 windbg 64位举例，我的 windbg 路径是：`D:\Windows Kits\10\Debuggers\x64`
需要把 SOS.dll 放在：`D:\Windows Kits\10\Debuggers\x64\winext` 下  

另外需要保证联网，这样才能下载 pdb 文件，缺少一些 pdb 文件会出错  

## 可找到相关windows api的情况
启动脚本有 2 种方式：  
1. 直接调用  
File -> Open Executable，文件名 选择 powershell.exe 的路径，Arguments 填脚本的绝对路径  
2. Attach  
先打开一个 Powershell 窗口，然后用 windbg attach，之后再执行脚本  

第 1 种可以在加载可执行文件后下断点，第 2 种方式需要在执行脚本前就下断点  

需要先找到脚本明显的系统 api 调用，比如在命令行有输出，那就可以在 `Kernel32!WriteConsoleA` `Kernel32!WriteConsoleW` 下断点  
```r
bp Kernel32!WriteConsoleW
```

然后 `g` 运行，在断下后，加载 sos：  
```r
.load sos
```
接着执行一条命令，就能获取到混淆比较少的代码：  
```r
!DumpStackObjects
```
命令也可以缩写成 `!dso`  

往上翻，可以看到很清晰的代码，越往上翻越整齐，基本就是完全解混淆的状态了  

如果想看 SOS 所有可用的命令，可以用这个命令 `!sos.help`  

## 找不到相关windows api的情况
加载 sos：  
```r
.load sos
```

一开始不知道 怎么给 iex 下断，去 msdn 查一下相关信息：  
https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.utility/invoke-expression?view=powershell-7  
了解到所在模块为 `Microsoft.PowerShell.Utility`  

name2ee 可以获取一些方法、类的结构和地址  
```r
Usage: !Name2EE module_name item_name
  or    !Name2EE module_name!item_name
       use * for module_name to search all loaded modules
Examples: !Name2EE  mscorlib.dll System.String.ToString
          !Name2EE *!System.String
```

我们通过 name2ee 找一下具体的模块：  
```r
!name2ee * iex
```

应该就是这个 dll：  
```r
Module: 000007fef0711000 (Microsoft.PowerShell.Commands.Utility.dll)
```

在电脑搜索这个 dll，用 dnSpy 打开，定位到 `Microsoft.PowerShell.Commands->InvokeExpressionCommand`，里面有一个 `ProcessRecord` 方法，所以最终我们要下断的方法是：  
```r
Microsoft.PowerShell.Commands.InvokeExpressionCommand.ProcessRecord
```

本来以为可以用 bpmd 命令直接下断，结果断不下来，所以还是用 name2ee 找到函数地址，以后就不用做上面的准备工作了，可以直接执行下面的命令：  
```r
!name2ee Microsoft.PowerShell.Commands.Utility.dll Microsoft.PowerShell.Commands.InvokeExpressionCommand.ProcessRecord
```

得到：  
```r
Module: 000007fef03e1000 (Microsoft.PowerShell.Commands.Utility.dll)
Token: 0x0000000006000476
MethodDesc: 000007fef03fd918
Name: Microsoft.PowerShell.Commands.InvokeExpressionCommand.ProcessRecord()
JITTED Code Address: 000007fef0548af0
```
`JITTED Code Address` 就是我们要下断的地址，下断：  
```r
bp 000007fef0548af0
```

断下来之后，怎么找到命令呢？  
执行 `!dso`，找到所有的 Object，复制出来，搜索 `Microsoft.PowerShell.Commands.InvokeExpressionCommand` 得到：  
```r
RSP/REG          Object           Name
rbx              00000000032bfff8 Microsoft.PowerShell.Commands.InvokeExpressionCommand
000000001c48dbb0 00000000032bfff8 Microsoft.PowerShell.Commands.InvokeExpressionCommand
```
dump Object:  
```r
!do 00000000032bfff8
```
得到：  
```r
Name: Microsoft.PowerShell.Commands.InvokeExpressionCommand
MethodTable: 000007fef079d758
EEClass: 000007fef0724998
Size: 128(0x80) bytes
Fields:
              MT    Field   Offset                 Type VT     Attr            Value Name
...
000007feed1a7b08  4000252       70        System.String  0 instance 00000000032bb050 _command
...
```

继续dump `_command` 对应的 value 
```r
!do 00000000032bb050
```

得到：  
```r
...
String: &("{1}{0}" -f'al','s') ("{0}{1}" -f't','est')...
...
```

可能的问题：  
```r
Failed to find runtime DLL (mscorwks.dll), 0x80004005
Extension commands need mscorwks.dll in order to have something to do.
```
还没加载好，现在比较笨的办法就是 g 一下，立马 break，不行就再 g break 一下  

可能多次触发断点，每次断点可能还有多个 InvokeExpressionCommand Object，一般最后一次断点的第 1 个 InvokeExpressionCommand 对应的 `_command` value dump 出来的 string 是这种方法能做到的最好的效果  

这种方法的优点是足够精确且通用，缺点就是略繁琐，如果能找到其他相关的 api 断点，就不需要用这种方法了  


## 相关资料
https://docs.microsoft.com/zh-cn/dotnet/framework/tools/sos-dll-sos-debugging-extension  

感谢yz  


---
2020/5/29  
