# web渗透简单套路

1. 可能有robots.txt
2. 在域名后输admin、login访问，可能会直接跳到后台
3. google hack: `site:域名 inurl:admin,login intitle:后台 intext:登录`
4. whatweb，检测基本信息
5. 在域名后输phpmyadmin，可能会有phpmyadmin后台
6. 找ip
7. 找子域名，sublist3r
8. `nmap -sS` 静默扫描端口
9. 找有漏洞的服务，测试

有时候一种方法没有思路时，试试另一种，思维发散一些  
比如GET没有结果，试试POST  


2017/9/6  
