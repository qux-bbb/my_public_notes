# John the Ripper

John the Ripper 是一个hash爆破工具。  
官网: https://www.openwall.com/john/  

爆破zip示例：  
```r
# 提取hash
zip2john hello.zip > hello.hash
# 使用字典爆破
john --wordlist pass.txt hello.hash
# 显示爆破结果
john --show hello.hash
```


参考链接: https://dfir.science/2014/07/how-to-cracking-zip-and-rar-protected.html  


2021/9/29  
