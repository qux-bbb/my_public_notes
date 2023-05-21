# 仿射密码解密举例

## 思路1
```
加密：n=(3m+5)mod 26

解密： m=(n-5)*3的逆元
        3的逆元根据辗转相除法可求出（26和3进行辗转相除）
```
逆元表  
![](images/逆元表.png)  


## 思路2：提前计算所有对应关系
```python
# coding:utf8

import string
s = string.ascii_lowercase # a-z
s += '_'
d = {}
for c in range(len(s)): 
    d[s[(c*4 + 15)%27]] = s[c]
ciphertext = 'ifpmluglesecdlqp_rclfrseljpkq'
s1 = ''
for x in ciphertext:
    s1 += d[x]
print s1
```

https://ctf.pediy.com/itembank-details-87.htm  


---
2016/7/16  
2020/3/21  
