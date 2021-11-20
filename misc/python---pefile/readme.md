# python---pefile

pefile可以解析、读取或修改PE文件。  

github地址: https://github.com/erocarrera/pefile/  
一些示例地址: https://github.com/erocarrera/pefile/blob/wiki/UsageExamples.md  

简单使用之修改PE：  
```python
# coding:utf8

import pefile

exe_sample = pefile.PE('test.exe')

# 输出一个导入表项的函数名
print(exe_sample.DIRECTORY_ENTRY_IMPORT[1].imports[0].name)

# 修改一个导入表项的函数名
exe_sample.DIRECTORY_ENTRY_IMPORT[1].imports[0].name = 'GoodEvening\x00'  # 使用\x00截断

# 将修改的PE写入到新文件
exe_sample.write(filename='new_test.exe')

# 关闭文件句柄 原来的文件不会被修改
exe_sample.close()
```

简单使用之获取.data数据：  
```python
# coding:utf8

from pefile import PE

def get_data(the_path):
    the_pe = PE(the_path)
    for section in the_pe.sections:
        if section.Name.startswith(b'.data\x00'):
            data = section.get_data()
            the_pe.close()
            return data
    return None
```


2019/10/30  
