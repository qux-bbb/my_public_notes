# python---遍历windows所有文件

```python
# coding:utf8

import os

def get_all_partition():
    '''
    遍历获取所有存在盘符
    :return: 盘符list，如['C:', 'D:']
    '''
    exist_partitions = []
    for i in range(65,91):
        partition = chr(i) + ':'
        if os.path.isdir(partition):
            exist_partitions.append(partition)
    return exist_partitions


def get_files(folder_name):
    '''
    获取某一文件夹下所有文件
    :param folder_name: 使用绝对路径的文件夹名，例如：D:\games
    :return: 所有文件名(绝对路径形式)list
    '''
    all_files = []
    for root, dir, files in os.walk(folder_name + '\\', True):
        if files:
            for file in files:
                all_files.append(root + '\\' + file)
    return all_files


def get_all_computer_file():
    '''
    获取本电脑所有文件
    :return: 所有文件列表
    '''
    partitions = get_all_partition()
    computer_files = []
    for partition in partitions:
        computer_files.extend(get_files(partition))
    return computer_files
```


2018/4/29  
