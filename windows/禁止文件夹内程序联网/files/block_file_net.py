# coding:utf8
# python3

'''
https://blog.csdn.net/weixin_43625577/article/details/88258369

netsh advfirewall firewall add rule name="新规则名称" dir=out program="禁止程序的路径" action=block

netsh 不能设置组
'''

import os


def get_special_files(folder_name, ext_list):
    '''
    获取某一文件夹下所有文件
    :param folder_name: 使用绝对路径的文件夹名，例如：D:\games
    :return: 所有文件名(绝对路径形式)list
    '''
    all_files = []
    for root, dir, files in os.walk(folder_name + '\\', True):
        if files:
            for file in files:
                if file.endswith(ext_list):
                    all_files.append(root + '\\' + file)
    return all_files


def main(group_name, folder_path, ext_list):
    file_paths = get_special_files(folder_path, ext_list)
    for file_path in file_paths:
        rule_name = '{}-{}'.format(group_name, file_path.split('\\')[-1])
        command = 'netsh advfirewall firewall add rule name="{}" dir=out program="{}" action=block'.format(
            rule_name,
            file_path
        )
        os.system(command)
        print('[*] firewall {} blocked'.format(file_path))
    

if __name__ == '__main__':
    group_name = 'sogou_input'
    folder_path = 'D:\Program Files (x86)\SogouInput'
    ext_list = ('.exe')
    main(group_name, folder_path, ext_list)
