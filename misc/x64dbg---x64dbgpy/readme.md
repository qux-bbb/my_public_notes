# x64dbg---x64dbgpy

## 简介
https://github.com/x64dbg/x64dbgpy/  
x64dbgpy 是一个插件，可以使用 python 脚本自动化调试过程  


## 安装
1. 需要同时安装 python2.7 的 x64 和 x86 版本，可以改一下安装目录，比如 x86 的就装在 `C:\\python27_x86` 目录下  
2. 在这里下载最新的 x64dbgpy： https://ci.appveyor.com/project/mrexodia/x64dbg-python/build/artifacts, 按位数复制到插件目录就好了，最外面的 .h 文件和 .lib 文件不用管  


## 示例脚本
大部分函数都可以在 x64dbg/release/x32/plugins/x64dbgpy/x64dbgpy/pluginsdk/x64dbg.py 找到  

因为 x64dbg/release/x32/plugins/x64dbgpy 在 python 的 path 里，所以可以用下面的方式把所有函数导入  
```python
from x64dbgpy.pluginsdk.x64dbg import *
```

简单脚本  
```python
# coding:utf8
'''
设置断点，读内存
'''

from x64dbgpy.pluginsdk import x64dbg
import scriptapi

x64dbg.SetBreakpoint(0x00401235)
x64dbg.Run()
# 地址 长度
name = scriptapi.Memory.read(0x00406930, 0xFF)
print('name: {}'.format(name))
```

简单脚本2  
```python
# coding:utf8

'''
拼接字符串
'''

from x64dbgpy.pluginsdk import x64dbg
import scriptapi

x64dbg.SetBreakpoint(0x0040133B)  # compare
x64dbg.SetBreakpoint(0x004013A6)  # right message
x64dbg.Run()

serial = ''
for i in range(10):
    dl = x64dbg.GetDL()
    serial += chr(dl)
    x64dbg.SetBL(dl)
    x64dbg.Run()
print(serial)
x64dbg.Run()
```

简单脚本3  
```python
# coding:utf8

'''
获取指定地址的字符串并比较
'''

from x64dbgpy.pluginsdk import x64dbg
import scriptapi


def get_ansi_str(addr):
    final_str = ''
    i = 0
    while True:
        c = scriptapi.Memory.read(addr+i, 1)
        if c == '\x00':
            break
        final_str += c
        i += 1
    return final_str


def get_wide_str(addr):
    final_str = ''
    i = 0
    while True:
        c = scriptapi.Memory.read(addr+i, 2)
        if c == '\x00\x00':
            break
        final_str += c
        i += 2
    return final_str


x64dbg.DbgScriptCmdExec('bp kernelbase.CreateFileW')
while True:
    x64dbg.Run()
    rcx = x64dbg.GetRCX()
    create_file_path = get_wide_str(rcx).replace('\x00', '')
    if 'encrypted.bin' in create_file_path:
        break

```

## MISC
函数在 x64dbg.py scriptapi.pyd 里，函数名需要整个文件夹搜，这样比较快  

搞不太清哪个比较重要，搜到哪个就用哪个吧  

如果出错了，调试器里还有 python 交互窗口，在里面 import 试一下  

建议在 x64dbg\release\x32\plugins\x64dbgpy 文件夹里写脚本，这样不会出现引用错误，整个文件夹在 vscode 打开，写脚本和搜索api都很方便  

想引用label.py中的函数  
`from x64dbgpy.pluginsdk._scriptapi import label`  


2020/8/15  
