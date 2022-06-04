# python---常见的字符集合

```python
import string

print(string.ascii_letters)  # 52个小写和大写字母
print(string.ascii_lowercase)  # 26个小写字母
print(string.ascii_uppercase)  # 26个大写字母
print(string.digits)  # 10个数字
print(string.printable)  # 100个可打印字符(包含制表符、回车符等不可见字符)
print(string.hexdigits)  # 22个16进制字符(字母有大小写2种)
print(string.octdigits)  # 8个8进制字符
print(string.punctuation)  # 32个标点符号
print(string.whitespace)  # 6个空白字符(包含制表符、回车符等不可见字符)
```

输出：  
```r
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ
abcdefghijklmnopqrstuvwxyz
ABCDEFGHIJKLMNOPQRSTUVWXYZ
0123456789
0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

0123456789abcdefABCDEF

0123456789abcdefABCDEF
01234567
!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~
```


参考链接: https://zhidao.baidu.com/question/262545510.html  


2016/5/26  
