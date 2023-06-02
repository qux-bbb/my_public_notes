# 前期侦查

```
信息侦查
查询dns服务器：whois  host
域名列表查询： fierce -dns domainName
反向查询：dig -x ip@dnsserver  举例：dig -x 218.75.123.181 @dns1.abc.edu.cn

nmap扫描  nmap识别操作系统：nmap -O url
识别系统  nmap -O -Pn url
tcp扫描（TCP3次握手），得到一些服务信息  nmap -sT -Pn url
syn扫描（TCP2次握手），速度快  nmap -sS -Pn url


p0f 被动检测工具：  p0f -i eth0 -p 可以进行操作系统检测
wafw00f url   检测防火墙保护
google高级搜索 ：setting --> 高级搜索
shodan

google黑客语法：
批量查找学校后台
site:abc.edu.cn  intext:管理|后台|登录|用户名|密码|验证码|系统|账号|后台管理|后台登录
搜索站点特定类型文件：
site:abc.edu.cn filetype:xls

maltego
社工神器


whatweb   网站指纹识别工具： wahtweb url
dirbuster  爆破目录和文件名
```


2017/9/2  
