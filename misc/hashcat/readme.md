# hashcat

官网: https://hashcat.net/hashcat/  
用来爆破各种密码  

```r
Usage: hashcat [options]... hash|hashfile|hccapxfile [dictionary|mask|directory]...
```
一般不会的时候直接 `hashcat --help` 看一遍就好了，这里举些例子  

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


如果已经爆破出结果，在结尾加 `--show` 可以直接显示结果  


2021/9/17  
