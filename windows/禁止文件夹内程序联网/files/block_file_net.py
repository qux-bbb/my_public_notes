# coding:utf8
# python3

'''
https://blog.csdn.net/weixin_43625577/article/details/88258369

netsh advfirewall firewall add rule name="新规则名称" dir=out program="禁止程序的路径" action=block

netsh 不能设置组
'''

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


def main(group_name, folder_path, ext_list):
    file_paths = get_special_filepaths(folder_path, ext_list)
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
