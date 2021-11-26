# hashcat

官网: https://hashcat.net/hashcat/  
用来爆破各种hash  

```r
Usage: hashcat [options]... hash|hashfile|hccapxfile [dictionary|mask|directory]...
```
hash字符串或hash文件均可，掩码或字典文件均可  

官方提供示例：  
```r
- [ Basic Examples ] -

  Attack-          | Hash- |
  Mode             | Type  | Example command
 ==================+=======+==================================================================
  Wordlist         | $P$   | hashcat -a 0 -m 400 example400.hash example.dict
  Wordlist + Rules | MD5   | hashcat -a 0 -m 0 example0.hash example.dict -r rules/best64.rule
  Brute-Force      | MD5   | hashcat -a 3 -m 0 example0.hash ?a?a?a?a?a?a
  Combinator       | MD5   | hashcat -a 1 -m 0 example0.hash example.dict example.dict
```

`-a` 选项表示攻击模式，有以下几种：  
```r
  0 | Straight
  1 | Combination
  3 | Brute-force
  6 | Hybrid Wordlist + Mask
  7 | Hybrid Mask + Wordlist
````
一般使用掩码选择 `-a 3`, 使用字典文件选择 `-a 0`  

`-m` 选项表示hash类型，太多了  

如果已经爆破出结果，在结尾加 `--show` 可以直接显示结果  
默认结果会存在这个文件里: `~/.hashcat/hashcat.potfile`  

不会用的时候直接 `hashcat --help` 看一遍就好了，下面举些实际使用的例子  

## `md5爆破`
```r
hashcat -a 3 -m 0 cfa590c5b4c51852821cc9a7669cfcd1 ?l?l?l?l?l?l
# result: cfa590c5b4c51852821cc9a7669cfcd1:catdog
```
`-a 3` 表示攻击模式为暴力破解，  
`-m 0` 表示hash类型为md5，  
`?l?l?l?l?l?l` 表示6位小写字母  

如果在 `-m 0` 后增加 `-i` 选项，爆破字典会从1位小写字母到6位小写字母  


## `NTLM爆破`
```r
hashcat -a 3 -m 1000 7713897782ba041df924ae79af7a5226 ?l?l?l?l?l?l
# result: 7713897782ba041df924ae79af7a5226:jackey
```
`-m 1000` 表示hash类型为NTLM  


## `7z压缩包爆破`
```r
# 安装perl、7z2hashcat.pl、相关依赖
sudo apt update && sudo apt install perl liblzma-dev
sudo cpan install Compress::Raw::Lzma
wget https://raw.githubusercontent.com/philsmd/7z2hashcat/master/7z2hashcat.pl
chmod +x 7z2hashcat.pl
./7z2hashcat.pl hello.7z > hello.hash
hashcat -a 3 -m 11600 hello.hash ?d?d?d?d?d?d
# result: $7z$0$19$0$$16$f9f8df6bdb5696522021c1df15c797bb$232844721$128$122$e23335c4ac5dec3dae6ecc56bec7362a0bb5a36ad58311968341446c322824fdc9230f28edc144c04ff3645762aed08a325332226d8a360796659d7efe6b2f13b556420de6b89a461f80bfe93dd18f09f9fea2b5e3f78d192962bd399c19729c5356390c02c3cc65fa9cd849ef30268d8a7f729522ef7f1da98e84d5dd122f85:123456
```
`-m 11600` 表示hash类型为7-Zip，  
`?d?d?d?d?d?d` 表示6位数字  


---
2021/9/17  
