# 把pyinstaller打包的exe还原成python脚本

keywords: pyinstaller 反编译  

自己写的脚本作废，直接用这个工具：  
https://pyinstxtractor-web.netlify.app/

~~https://github.com/extremecoders-re/pyinstxtractor~~  
~~用之前先用16进制编辑器或xanalyzer看看python版本，尽量用对应版本去还原，这样不容易出问题~~  

一个可执行文件可能有多个有用的pyc，用uncompyle6或pycdc反编译pyc  
详情见 [python---生成和反编译pyc](../../misc/python---生成和反编译pyc/readme.md)

---
有一点要注意：  
项目的脚本是根据当前运行python版本获取pyc magic 的，所以可能不对，需要自己根据 解出来的 python dll 确定到底应该是什么 magic  

这里有很多 pyc magic：  
https://github.com/rocky/python-xdis/blob/master/xdis/magics.py  
pyc文件的前2个字节是magic，没有换算关系，只能映射，比如：  
'\x03\xf3' 0xF303 python27  
'\xee\x0c' 0x0CEE python34  

```python
# coding:utf8

'''
把pyinstaller打包的exe还原成python脚本
需要安装 pyinstaller, uncompyle6

仅测试过python2.7, 其他不能用再修改

参考链接: https://www.52pojie.cn/thread-944487-1-1.html
'''

import os
import sys
import re

from PyInstaller.utils.cliutils.archive_viewer import get_archive, get_data


def main(file_path):
    arch = get_archive(file_path)

    pyc_magic = None
    for item in arch.toc.data:
        # pos, length, uncompressed, iscompressed, type, name
        # (16861, 429, 623, 1, 's', u'decode')
        # 需要收集更多 TODO 改成正则, python\d{2}.dll
        if item[5] == 'python27.dll':
            pyc_magic = '\x03\xf3\x0d\x0a\x00\x00\x00\x00'
            break
        if item[5] == 'python34.dll':
            pyc_magic = '\xee\x0c\x0d\x0a\x00\x00\x00\x00'
            break
    if not pyc_magic:
        print('Need pyc_magic')

    for item in arch.toc.data:
        item_type = item[4]
        item_name = item[5]
        if item_type == 's' and not item_name.startswith('pyi'):
            data = get_data(item_name, arch)
            with open(item_name+'.pyc', 'wb') as fp:
                fp.write(pyc_magic+data)
            os.system('uncompyle6 {0}.pyc > {0}.py'.format(item_name))
            os.remove(item_name+'.pyc')


if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_path = sys.argv[1]
        if not os.path.exists(file_path):
            print('{} does not exist!'.format(file_path))
        else:
            main(file_path)
    else:
        print('Usage: python {} <file_path>'.format(sys.argv[0]))
        
```


---
2020/9/7  
