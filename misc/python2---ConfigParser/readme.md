# python2---ConfigParser

## 官方文档
https://docs.python.org/2/library/configparser.html  

## 使用示例
配置文件示例：  
```r
[info]
username = hello
password = world
```

使用配置文件的脚本（和配置文件内容无对应关系）：  
```python
# coding:utf8

import ConfigParser

def write_conf():
    config = ConfigParser.ConfigParser()
    config.add_section('translate_service')
    config.set('translate_service', 'enabled', False)

    # Writing our configuration file to 'example.cfg'
    with open('cc.conf', 'wb') as configfile:
        config.write(configfile)

def read_conf():
    config = ConfigParser.ConfigParser()
    config.read('cc.conf')
    translate_service_enabled = config.getboolean('translate_service', 'enabled')
    print translate_service_enabled

def change_conf():
    config = ConfigParser.ConfigParser()
    config.read('cc.conf')
    translate_service_enabled = config.getboolean('translate_service', 'enabled')
    if translate_service_enabled:
        print('translate_service is already enabled')
    else:
        config.set('translate_service', 'enabled', True)
        with open('cc.conf', 'wb') as configfile:
            config.write(configfile)
        print('translate_service enabled')

write_conf()
read_conf()
change_conf()
```

## 注释
以 `#` 或 `;` 开头的行被识别为注释  
`;` 还可以作为行内注释使用  
写配置会丢失注释, 如果想保留注释, 可以自己修改或者使用ConfigObj  


---
2020/8/29  
