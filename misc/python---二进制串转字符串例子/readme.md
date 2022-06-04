# python---二进制串转字符串例子

```python
# coding:utf8
# python3

import re

aa = "110011011011001100001110011111110111010111011000010101110101010110011011101011101110110111011110011111101"

# 7还是8，根据实际情况判断
bb = re.findall(r".{7}", aa)

str1 = ""
for b in bb:
    str1 += chr(int(b, 2))

print(str1)
# flag{W0W*funny}
```


2017/9/2  
