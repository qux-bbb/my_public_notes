# python---pyelftools

pyelftools 可以用来解析elf文件。  

github地址: https://github.com/eliben/pyelftools  

安装：  
```r
pip install pyelftools
```

示例：  
```r
# coding:utf8

import re
from elftools.elf.elffile import ELFFile

ip_re = rb"\x00(?P<ip>(?:\d{1,3}\.){3}\d{1,3})\x00"

def extract(filepath):
    result = None
    the_file = open(filepath, "rb")
    elffile = ELFFile(the_file)
    rodata = elffile.get_section_by_name(".rodata")
    if rodata:
        ip_search = re.search(ip_re, rodata.data())
        if ip_search:
            result = ip_search.group("ip")

    the_file.close()

    return result

```


2022/6/20  
