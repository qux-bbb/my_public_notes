# python3---configparser

keywords: python 配置文件  

和python2相比，ConfigParser变成了configparser。写入的值必须是字符串，如"True"。  

3.7的官方文档: https://docs.python.org/3.7/library/configparser.html  

```python
# coding:utf8

import configparser

def write_conf():
    config = configparser.ConfigParser()
    config.add_section('translate_service')
    config.set('translate_service', 'enabled', 'False')

    # Writing our configuration file to 'example.cfg'
    with open('cc.conf', 'w') as configfile:
        config.write(configfile)

def read_conf():
    config = configparser.ConfigParser()
    config.read('cc.conf')
    translate_service_enabled = config.getboolean('translate_service', 'enabled')
    print(translate_service_enabled)

def change_conf():
    config = configparser.ConfigParser()
    config.read('cc.conf')
    translate_service_enabled = config.getboolean('translate_service', 'enabled')
    if translate_service_enabled:
        print('translate_service is already enabled')
    else:
        config.set('translate_service', 'enabled', 'True')
        with open('cc.conf', 'w') as configfile:
            config.write(configfile)
        print('translate_service enabled')

write_conf()
read_conf()
change_conf()
```

如果配置文件中有中文，读取时需要指定encoding参数，比如 `encoding='utf8'`  


2022/1/24  
