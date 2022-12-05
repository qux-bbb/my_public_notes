# John the Ripper

John the Ripper 是一个hash爆破工具。  
官网: https://www.openwall.com/john/  

爆破结果会保存在: `~/.john` 目录下  

爆破zip示例：  
```r
# 提取hash
zip2john hello.zip > hello.hash
# 使用字典爆破
john --wordlist=pass.txt hello.hash
# 显示爆破结果
john --show hello.hash
```

爆破7z示例：  
```r
# 7z2john不是自带的，需要下载
wget https://github.com/truongkma/ctf-tools/blob/master/John/run/7z2john.py
# 提取hash，注意该脚本只支持python2
python 7z2john.py hello.7z > hello.hash
# 使用字典爆破
john --wordlist=pass.txt hello.hash
# 显示爆破结果
john --show hello.hash
```

爆破shadow示例：  
```r
# shadow是linux存储密码hash的文件，把里面需要爆破的行复制出来存到新文件就可以爆破了，不需要unshadow之类的工具
# 但由于各个系统采用的hash算法不同，可能不一定支持
john --wordlist=rockyou.txt shadow.txt
john --show shadow.txt
```

john支持400多种的hash爆破，但也有些算法不支持，如yescrypt，查看支持的算法命令如下：  
```r
john --list=formats
```


参考链接：  
1. https://dfir.science/2014/07/how-to-cracking-zip-and-rar-protected.html
2. https://www.hackingarticles.in/beginner-guide-john-the-ripper-part-1/
3. https://www.hackingarticles.in/beginners-guide-for-john-the-ripper-part-2/


2021/9/29  
