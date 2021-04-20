# pdb路径处理

## 简介
pdb, Program Database, 保存变量函数名等符号信息的文件。  

默认情况下使用VS生成的可执行程序会带符号文件路径。  


## 具体去除方法

如果想去掉，可以用以下几种方法  

### VS项目设置
推荐使用该方法  

项目 -> 项目具体属性 -> 配置属性 -> 链接器 -> 调试  

可以把"生成调试信息"选项设置为"否"，这样就不会有pdb路径了  
也可以设置"生成程序数据库文件"，自定义路径名称  

### 16进制编辑器修改
16进制编辑器直接搜索`.pdb`，定位之后随便修改  

### 脚本搜索替换
其实没必要这么做，但还是记一下  
```python
# coding:utf8
# python2/3均可

import re
import shutil

file_path = 'Test.exe'
replace_str = b'Hello World'

f = open(file_path, 'rb')
content = f.read()
f.close()

s = re.search(b'[A-Z]:\\\\.+?\.pdb', content)
if s:
    pdb_path = s.group(0)
    pdb_path_len = len(pdb_path)
    replace_str_len = len(replace_str)
    if replace_str_len > pdb_path_len:
        print('The replace content is too long.')
    else:
        replace_str += b' ' * (pdb_path_len - replace_str_len)
        content = content.replace(pdb_path, replace_str)

        shutil.copyfile(file_path, file_path + '.bak')

        f = open(file_path, 'wb')
        f.write(content)
        f.close()

        print('Finished.')
else:
    print('Can not find the pdb string.')
```


20190830 16进制编辑器修改  
20190831 脚本搜索替换  
20210420 VS项目设置  
