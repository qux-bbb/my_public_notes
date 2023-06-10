# xshell6家庭版去除tab限制脚本

```python

# coding:utf8

"""
xshell 6 家庭版去除tab限制脚本
在安装目录下运行该脚本即可
"""

import os

if not os.path.exists('XshellLib.dll'):
    print 'Failed!\nCan not find file "XshellLib.dll"'
    exit(0)
if os.path.exists('XshellLib.dll.bak'):
    print 'Failed!\nThe backup file "XshellLib.dll.bak" exists, plz mv or del it'
    exit(0)

os.rename('XshellLib.dll', 'XshellLib.dll.bak')


want_dll = open('XshellLib.dll.bak', 'rb').read()
if 'c786ec00000004000000'.decode('hex') in want_dll:
    ok_dll = want_dll.replace(
        'c786ec00000004000000'.decode('hex'), 'c786ec000000ffff0000'.decode('hex'))
    open('XshellLib.dll', 'wb').write(ok_dll)
    print 'Success!\nPlz Open and test it'
else:
    print 'Failed!\nThe XshellLib.dll does not contain what I can change'

```


2018/9/23  
