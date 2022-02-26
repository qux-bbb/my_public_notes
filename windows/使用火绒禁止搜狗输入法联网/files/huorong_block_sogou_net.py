# coding:utf8
# python3

'''
该脚本可生成火绒规则json，用于禁止搜狗输入法联网

火绒规则示例json
{
    "ver":"5.0",
    "tag":"ipproto",
    "data":[
        {
            "icmp_type":0,
            "id":1,
            "recname":"sougou1",
            "block":1,
            "procname":"D:\\Program Files (x86)\\SogouInput\\SogouExe\\SogouExe.exe",
            "enabled":true,
            "lport":"*",
            "protocol":260,
            "laddr":"*",
            "direction":0,
            "raddr":"*",
            "rport":"*",
            "priority":1
        }
    ]
}
'''

import os
import json


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
    result_dict = {
        "ver":"5.0",
        "tag":"ipproto",
        "data":[]
    }
    file_paths = get_special_filepaths(folder_path, ext_list)
    for file_path in file_paths:
        rule_name = '{}-{}'.format(group_name, file_path.split('\\')[-1])
        rule = {
            "icmp_type":0,
            "id":1,
            "recname":rule_name,
            "block":1,
            "procname":file_path,
            "enabled":True,
            "lport":"*",
            "protocol":260,  # tcp and udp
            "laddr":"*",
            "direction":0,
            "raddr":"*",
            "rport":"*",
            "priority":1
        }
        result_dict['data'].append(rule)
        with open('rules.json', 'w') as f:
            json.dump(result_dict, f, indent=4)
    

if __name__ == '__main__':
    group_name = 'sogou_input'
    folder_path = 'D:\Program Files (x86)\SogouInput'
    ext_list = ('.exe')
    main(group_name, folder_path, ext_list)
