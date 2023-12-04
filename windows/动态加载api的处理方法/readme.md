# 动态加载api的处理方法

分析样本时经常会遇到动态加载api使用的情况，这种方法降低了静态分析的效率，如果不做处理，不容易根据api快速确定函数功能，下面整理一下一些情况的处理方法。

## 情况1：集中恢复
有些样本会在一个地方集中恢复api  
我们可以调试，执行完恢复api的函数之后，有2种处理方法：  
- dump程序后使用新文件做静态分析  
- 复制相应地址和api名称，使用脚本将标签添加到IDA里，见笔记 `IDAPython---地址添加标签`  

## 情况2：使用时单个恢复
有些样本在使用api时才会恢复单个api  
有3种方法：  
```
1. 借助调试器，下简单的断点输出日志
    优点：简单
    确定：没有运行的地方就无法自动获取
2. 借助调试器，python调用恢复的api去获取
    优点：比较全
    缺点：需要搭建环境，写脚本麻烦(需要些从反编译软件收集参数的脚本，调试器里使用的python脚本)
3. 完全分析清楚，自己模拟实现
    优点：最透彻
    缺点：需要很多时间
```

最后可以写脚本把api信息作为注释添加到反编译器里  

### 示例  
4029f9fcba1c53d86f2c59f07d5657930bd5ee64cca4c5929cbd3142484e815a  

有一部分函数未识别，可以使用该笔记里的脚本处理: [IDAPython---未识别函数创建](../../misc/IDAPython---未识别函数创建/readme.md)  

#### 断点输出日志  
```
sub_30A3170 是获取api的函数
在sub_30A3170函数的结尾准备返回位置 0x030A3301 下断点，编辑断点：
暂停条件: 0
日志文本: 0x{[esp]-5}: "{modname@eax}.{label@eax}",

运行，整理去重后，部分结果如下：
0x309A57F: "kernel32.dll.LoadLibraryA",
0x309A5E6: "kernel32.dll.GetProcAddress",
0x309F5CB: "kernel32.dll.GetProcessHeap",
0x3092138: "ws2_32.dll.WSAStartup",
```
IDA汇编视图设置注释: [set_comments.py](./files/set_comments.py)  
直接粘代码到底部的python输入框回车执行即可  

IDA反编译视图(伪代码视图)里设置注释更方便查看: [set_comments_in_pseudocode_view.py](./files/set_comments_in_pseudocode_view.py)  

缺点：没有调用的地方就获取不到，比如 0x03091CAC 应该是 kernel32.ExitProcess  

#### python调用获取  
前提：x64dbg安装x64dbgpy插件  

获取步骤：  
1. 需要在IDA里收集参数: [search_func_args.py](./files/search_func_args.py)
2. 将收集的参数整理去重，x64dbg运行脚本获取api信息: [x64dbg_get_api_info.py](./files/x64dbg_get_api_info.py)
3. 最后把结果写到IDA里: [set_comments_from_x64dbg_in_pseudocode_view.py](./files/set_comments_from_x64dbg_in_pseudocode_view.py)

缺点：动态生成参数的地方就获取不到，比如 0x03091CCD 第2个参数是 0x07A85C71 api应该是 user32.MessageBoxA  


---
2023/10/28  
