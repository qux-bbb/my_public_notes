# 禁用MobaXterm的Tux Consolesaver

```python
# coding:utf8

"""
Disable ConsoleSaver
python2
"""

import os
import sys
import re
from shutil import copyfile

re_want_hex = re.compile(r'74328b45fc8b80..5c00008b55fc3b9c829..c0000741d')
re_final_hex = re.compile(r'90908b45fc8b80..5c00008b55fc3b9c829..c00009090')

if len(sys.argv) != 2:
    print('Disable ConsoleSaver')
    print('python {} exe_file'.format(sys.argv[0]))
    exit(0)

file_path = sys.argv[1]
if not os.path.exists(file_path):
    print('{} does not exist!!!'.format(file_path))
    exit(0)

exe_file = open(file_path, 'rb')
file_content = exe_file.read().encode('hex')
exe_file.close()

match_want_hex = re_want_hex.search(file_content)
match_final_hex = re_final_hex.search(file_content)
if match_want_hex:
    bak_file_path = file_path + '.bak'
    if not os.path.exists(bak_file_path):
        copyfile(file_path, bak_file_path)

    match_content = match_want_hex.group()
    file_content = file_content.replace(
        match_content, '9090'+match_content[4:-4]+'9090')

    exe_file = open(file_path, 'wb')
    exe_file.write(file_content.decode('hex'))
    exe_file.close()
    print('Modify success!')
elif match_final_hex:
    print('exe_file already modified.')
else:
    print('Modify failed, can not find the bytes!!!')

```


2020/1/8  
