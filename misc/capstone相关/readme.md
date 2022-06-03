# capstone相关

官网介绍：  
Capstone是一个轻量级的多平台，多架构的反汇编框架。 我们的目标是使 Capstone 成为安全社区中用于二进制分析和逆向的终极反汇编引擎。
  
官网：  
http://www.capstone-engine.org/  

官网 python 文档：  
http://www.capstone-engine.org/lang_python.html  

python 安装：  
```r
pip install capstone
```

python 简单的例子：  
```python
# test1.py
from capstone import *

CODE = b"\x55\x48\x8b\x05\xb8\x13\x00\x00"

md = Cs(CS_ARCH_X86, CS_MODE_64)
for i in md.disasm(CODE, 0x1000):
    print("0x%x:\t%s\t%s" %(i.address, i.mnemonic, i.op_str))
```

注意 0x1000 是在内存里 eip 的初始位置，不是要模拟代码的偏移  


2020/5/9  
