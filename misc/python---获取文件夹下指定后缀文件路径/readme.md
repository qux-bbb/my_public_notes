# python---获取文件夹下指定后缀文件路径

```python
# coding:utf8

import os

def get_special_filepaths(folder_path, the_ext):
    '''
    获取某一文件夹下指定后缀的所有文件路径
    :return: 特定后缀的文件路径列表
    '''
    special_filepaths = []
    for dirpath, dirnames, filenames in os.walk(folder_path):
        for filename in filenames:
            if filename.endswith(the_ext):
                special_filepath = os.path.join(dirpath, filename)
                special_filepaths.append(special_filepath)
    return special_filepaths
```


