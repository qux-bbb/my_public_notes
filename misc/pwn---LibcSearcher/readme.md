# pwn---LibcSearcher

## 简介
LibcSearcher  
该库可以使你不用再因为到处找符合条件的lib.so文件苦恼  
地址: https://github.com/lieanu/LibcSearcher  


## 安装
```bash
git clone https://github.com/lieanu/LibcSearcher.git
cd LibcSearcher
python setup.py develop
```


## 示例
```python
from LibcSearcher import *

#第二个参数，为已泄露的实际地址,或最后12位(比如：d90)，int类型
leaked_fgets_addr = 0X7ff39014bd90
libc = LibcSearcher("fgets", leaked_fgets_addr)

libc_base = leaked_fgets_addr - libc.dump("fgets")

system_offset = libc.dump("system")        #system 偏移
bin_sh_offset = libc.dump("str_bin_sh")    #/bin/sh 偏移
libc.dump("__libc_start_main_ret")    

real_system_addr = libc_base + system_offset
bin_sh_addr = libc_base + bin_sh_offset
```


## 添加自己机器上的libc库
```bash
cd ~/LibcSearcher/libc-database/
./add /lib/i386-linux-gnu/libc.so.6
```


---
2020/11/29  
