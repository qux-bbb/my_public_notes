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


def get_files(folder_path):
    '''
    获取某一文件夹下所有文件
    :param folder_path: 使用绝对路径的文件夹路径，例如：D:\games
    :return: 所有文件名(绝对路径形式)list
    '''
    all_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            a_file = os.path.join(root, file)
            all_files.append(a_file)
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
