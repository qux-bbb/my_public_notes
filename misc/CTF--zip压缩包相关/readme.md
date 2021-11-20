# CTF---zip压缩包相关

ctf里，压缩包很常出现，这里记一些处理zip压缩包的思路。  

## `伪加密`
原理就是把表示是否加密的位设为1  
可以使用脚本处理，参照: https://github.com/qux-bbb/de-zip  


## `归档明文攻击`
一个有密码的zip压缩包，其中有文件以归档形式(STORE)存在，且该文件部分明文已知，如jpg图片。  
或者图片本身已经是压缩形式，"压无可压"，如png图片。  
这时可以采用明文攻击，使用这个项目提供的工具 https://github.com/kimci86/bkcrack  

以jpg举例：  
```r
# jpg_header文件内容为 任意jpg文件的前12字节(这里需要注意，jpg图片的前12字节并不总是相同的)
./bkcrack -C target.zip -c t.jpg -p jpg_header
bkcrack 1.3.3 - 2021-11-08
[21:48:20] Z reduction using 4 bytes of known plaintext
100.0 % (4 / 4)
[21:48:20] Attack on 1387043 Z values at index 7
Keys: b0a90b36 14dd97b9 f5d648cf
16.6 % (230200 / 1387043)
[22:00:34] Keys
b0a90b36 14dd97b9 f5d648cf

# 耗时12分钟得到密钥，使用密钥生成一个密码为"easy"的压缩包
./bkcrack -C target.zip -k b0a90b36 14dd97b9 f5d648cf -U target_with_new_password.zip easy
```
这样就可以解压新压缩包查看文件信息了。  


## `明文攻击`
一个有密码的zip压缩包里有a.txt,b.txt，不知道密码，你有一个相同的a.txt(可通过crc32判断)，想知道b.txt的内容  
这时可以使用工具：ARCHPR，可以随便在网上搜一个，然后虚拟机里临时用  

做法：把a.txt压缩，然后用ARCHPR的明文攻击选项，就能得到压缩包的密码或者直接得到没有密码的压缩包。  
这里需要注意的是能否成功和压缩的软件有关系，由于不同的压缩软件压缩方法不同，所以明文攻击的效果也不一样，可以逐个测试，常用的压缩软件有：winrar，好压，7z  


## `担保Winzip恢复`
英文是 Guaranteed WinZip attack，WinZip8.0和之前的版本使用了脆弱的随机数生成器，导致密钥可以很快爆破出来，详细介绍可以看ARCHPR的帮助文档。  
场景：WinZip8.0及之前版本压缩的压缩包，压缩包内至少有5个加密的文件  

做法：攻击类型选择"担保Winzip恢复"，点击开始即可  
分为两个阶段，第一阶段完成即可获得没有密码的压缩包，第二阶段完成有几率获得密码(耗时很长，大概率拿不到密码)  


## `普通的加密压缩包`
这个就没什么办法了，我知道的有几种：  
- 弱密码
- 跑生日
- 纯暴力破解
- 各种地方花式藏密码
- 汉字密码

也许这两个项目的字典可以排上用场：  
https://github.com/TheKingOfDuck/fuzzDicts  
https://github.com/danielmiessler/SecLists  


2017/5/9  
2021/10/13  
