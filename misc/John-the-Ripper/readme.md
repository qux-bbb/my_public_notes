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

爆破7z示例：  
```r
# 722john不是自带的，需要下载
wget https://github.com/truongkma/ctf-tools/blob/master/John/run/7z2john.py
# 提取hash，注意该脚本只支持python2
python 7z2john.py hello.7z > hello.hash
# 使用字典爆破
john --wordlist pass.txt hello.hash
# 显示爆破结果
john --show hello.hash
```


参考链接：  
1. https://dfir.science/2014/07/how-to-cracking-zip-and-rar-protected.html
2. https://www.hackingarticles.in/beginner-guide-john-the-ripper-part-1/
3. https://www.hackingarticles.in/beginners-guide-for-john-the-ripper-part-2/


2021/9/29  
