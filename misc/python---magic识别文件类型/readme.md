# python---magic识别文件类型

## 介绍
magic是一个识别文件类型的python模块  
原项目地址：  
https://github.com/ahupp/python-magic  
这个项目整合了一下windows的需要的库，直接用这个吧：  
https://github.com/julian-r/python-magic  


## 安装
`pip install python-magic-bin`  


## 简单使用
方法1  
```python
>>> import magic
>>> magic.from_file("testdata/test.pdf")
'PDF document, version 1.2'
>>> magic.from_buffer(open("testdata/test.pdf").read(1024))
'PDF document, version 1.2'
>>> magic.from_file("testdata/test.pdf", mime=True)
'application/pdf'
```

方法2  
```python
>>> f = magic.Magic(uncompress=True)
>>> f.from_file('testdata/test.gz')
'ASCII text (gzip compressed data, was "test", last modified: Sat Jun 28 21:32:52 2008, from Unix)'
```


## 一个解决实际问题的小例子
该例子结合了zipfile和magic的用法  
```python
# coding:utf8

import os
from zipfile import ZipFile
import magic

m = magic.Magic()

dir_name = '/home/some_zip/'
for root, dir, files in os.walk(dir_name):
    zipnames = files
    break

for a_zip_name in zipnames:
    print '#' * 80
    print a_zip_name
    with ZipFile(dir_name + a_zip_name) as azip:
        filenames = azip.namelist()
        for i in [10, 20, 30]:
            with azip.open(filenames[i], pwd='zippassword') as afile:
                print m.from_buffer(afile.read())
```


## 问题
1. magic.from_file不支持中文文件名
2. apk只能识别成zip
