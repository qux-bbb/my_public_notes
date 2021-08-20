# 保留NULL的异或

保留NULL的异或，规则如下：  
1. 如果明文中字符是NULL(值为0的字节)或者密钥本身，则被跳过
2. 如果明文中字符既不是NULL也不是密码本身，则将被使用XOR密钥加密

可以稍微增加一点识别和恢复的难度。  

python的一个实现：  
```python
# coding:utf8
# python3

the_file = open('git.exe', 'rb')
file_content = the_file.read()
the_file.close()

xor_key = 0x12
new_content = b''
for i in file_content:
    if i == 0 or i == xor_key:
        new_content += i.to_bytes(1, 'big')
    else:
        new_content += (i ^ xor_key).to_bytes(1, 'big')

new_file = open('enc_file', 'wb')
new_file.write(new_content)
new_file.close()
```


来源: 恶意代码分析实战  


2021/8/20  
