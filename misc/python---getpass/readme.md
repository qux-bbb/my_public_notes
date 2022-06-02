# python---getpass

getpass可用于命令行获取密码输入, 不会显示密码  

```python
# coding:utf8

import getpass

username = raw_input('username: ')
password = getpass.getpass('password: ')

print(username)
print(password)

```

需要注意的点  
`getpass.getuser()`用于获取当前环境中的用户名, 不是让输入用户名的  

原文链接：https://blog.csdn.net/weixin_42936566/article/details/87858195  


2020/1/11  
