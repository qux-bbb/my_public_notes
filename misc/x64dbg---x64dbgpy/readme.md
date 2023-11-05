# x64dbg---x64dbgpy

## 简介
https://github.com/x64dbg/x64dbgpy/  
x64dbgpy 是一个插件，可以使用 python 脚本自动化调试过程  


## 安装
需要下载的文件看这里: https://github.com/x64dbg/x64dbgpy/releases  
1. 需要同时安装 python2.7 的 x64 和 x86 版本，可以改一下安装目录，比如 x86 的就装在 `C:\\python27_x86` 目录下  
2. x64dbgpy(如x64dbgpy_8c0538a.zip)不需要复制到x64dbg安装目录, 解压按位数复制到插件目录就好了，最外面的 .h 文件和 .lib 文件不用管  
    x64dbgpy_8c0538a\x32\plugins -> snapshot_2023-09-21_00-53\release\x32\plugins  
    如果已经安装了其它插件，需要把plugins里的文件复制到相应同名目录下  


## 示例脚本
大部分函数都可以在 x64dbg/release/x32/plugins/x64dbgpy/x64dbgpy/pluginsdk/x64dbg.py 找到  

简单脚本  
```python
# coding:utf8
'''
设置断点，读内存
'''

from x64dbgpy.pluginsdk import x64dbg
from x64dbgpy.pluginsdk import memory

x64dbg.SetBreakpoint(0x00401235)
x64dbg.Run()
# 地址 长度
name = memory.Read(0x00406930, 0xFF)
print('name: {}'.format(name))
```

简单脚本2  
```python
# coding:utf8

'''
拼接字符串
'''

from x64dbgpy.pluginsdk import x64dbg

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
from x64dbgpy.pluginsdk import memory


def get_ansi_str(addr):
    final_str = ''
    i = 0
    while True:
        c = memory.Read(addr+i, 1)
        if c == '\x00':
            break
        final_str += c
        i += 1
    return final_str


def get_wide_str(addr):
    final_str = ''
    i = 0
    while True:
        c = memory.Read(addr+i, 2)
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


## 运行脚本方法
### 方法1
插件 -> x64dbgpy  
然后可以根据实际情况选择"Open GUI Script.."或"Open Async Script.."，加载python脚本执行  

### 方法2
在右下角将命令方式更换为"Python"，将脚本内容粘贴到命令行内回车执行  


## MISC
函数在 x64dbg.py 里，scriptapi.pyd 也可以用，但写代码时提示不友好  
函数名可以整个文件夹搜，这样比较快  

建议在 x64dbg\release\x32\plugins\x64dbgpy 文件夹里写脚本，这样不会出现引用错误，整个文件夹在 vscode 打开，写脚本和搜索api都很方便  

想引用label.py中的函数  
`from x64dbgpy.pluginsdk import label`  


---
2020/8/15  
