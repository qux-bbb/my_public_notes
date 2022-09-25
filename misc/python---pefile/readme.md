# python---pefile

pefile可以解析、读取或修改PE文件。  

github地址: https://github.com/erocarrera/pefile/  
一些示例地址: https://github.com/erocarrera/pefile/blob/wiki/UsageExamples.md  

安装: `pip3 install pefile`  

## 简单使用
修改PE：  
```python
# coding:utf8

import pefile

exe_sample = pefile.PE('test.exe')

# 输出基址，如: 0x400000
print(exe_sample.NT_HEADERS.OPTIONAL_HEADER.ImageBase)

# 输出一个导入表项的函数名
print(exe_sample.DIRECTORY_ENTRY_IMPORT[1].imports[0].name)

# 修改一个导入表项的函数名
exe_sample.DIRECTORY_ENTRY_IMPORT[1].imports[0].name = 'GoodEvening\x00'  # 使用\x00截断

# 将修改的PE写入到新文件
exe_sample.write(filename='new_test.exe')

# 关闭文件句柄 原来的文件不会被修改
exe_sample.close()
```

获取.data数据：  
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
    the_pe.close()
    return None
```

获取特定资源数据：  
```python
import pefile

def get_resource_data(the_path):
    the_pe = pefile.PE(the_path)

    if hasattr(the_pe, 'DIRECTORY_ENTRY_RESOURCE'):
        rt_rcdata_resource_type_id = pefile.RESOURCE_TYPE['RT_RCDATA']

        for resource_entry in the_pe.DIRECTORY_ENTRY_RESOURCE.entries:
            if resource_entry.id != rt_rcdata_resource_type_id:
                continue
            for rt_rcdata_entry in resource_entry.directory.entries:
                if rt_rcdata_entry.name.string != b'SETTINGS':
                    continue
                settings_entry = rt_rcdata_entry.directory.entries[0]

                data_rva = settings_entry.data.struct.OffsetToData
                size = settings_entry.data.struct.Size
                data = the_pe.get_memory_mapped_image()[data_rva:data_rva+size]

                the_pe.close()
                return data
    
    the_pe.close()
    return
```


---
2019/10/30  
