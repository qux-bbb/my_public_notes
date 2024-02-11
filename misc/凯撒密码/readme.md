# 凯撒密码

keywords: rot13 rotate  

凯撒密码属于古典密码的移位密码，将明文每个字母加3即得到密文，密文每个字母减3即得到明文。  

简单脚本示例：  
```python
# coding:utf8

def caser(the_str):
    for n in range(1, 26):
        tmp_str = ''
        for c in the_str:
            tmp_num = ord(c)
            if tmp_num >= 65 and tmp_num <= 90:  # 'A'~'Z'
                tmp_num = ((tmp_num - 65 + n) % 26) + 65
            elif tmp_num >= 97 and tmp_num <= 122:  # 'a'~'z'
                tmp_num = ((tmp_num - 97 + n) % 26) + 97
            tmp_str += chr(tmp_num)
        print(tmp_str)

# the_str = 'khoor_zruog'
the_str = 'hello_world'

caser(the_str)
```


2021/11/28  
