# RSA要点总结

keywords: RSA  

RSA是一种非对称算法，原理是：根据数论，寻求两个大素数比较简单，而将它们的乘积进行因式分解却极其困难，因此可以将乘积公开作为加密密钥。  
名字来源于3个作者姓氏首字母：罗纳德·李维斯特（Ron Rivest）、阿迪·萨莫尔（Adi Shamir）和伦纳德·阿德曼（Leonard Adleman）。  

## 文字版
**公钥**  
n: 两素数 p 和 q 的乘积(p 和 q 必须保密)  
e: 与 (p-1)(q-1) 互素  

**私钥**  
d: $e^{-1}  \mod (p-1)(q-1)$  
也就是 $d*e \equiv 1 \mod (p-1)(q-1)$  

**加密**  
$c \equiv m^e \mod n$  

**解密**  
$m \equiv c^d \mod n$  


## 图片版
![RSA要点总结](images/rsa_point.png)  


2020/1/11  
