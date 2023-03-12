# 十五个Web狗的CTF出题套路

```r
一、爆破，包括包括md5、爆破随机数、验证码识别等
二、绕WAF，包括花式绕Mysql、绕文件读取关键词检测之类拦截
三、花式玩弄几个PHP特性，包括弱类型，strpos和===，反序列化+destruct、\0截断、iconv截断、
四、密码题，包括hash长度扩展、异或、移位加密各种变形、32位随机数过小
五、各种找源码技巧，包括git、svn、xxx.php.swp、*www*.(zip|tar.gz|rar|7z)、xxx.php.bak、
六、文件上传，包括花式文件后缀 .php345 .inc .phtml .phpt .phps、各种文件内容检测、花式解析漏洞、
七、Mysql类型差异，包括和PHP弱类型类似的特性,0x、0b、1e之类，varchar和integer相互转换
八、open_basedir、disable_functions花式绕过技巧，包括dl、mail、imagick、bash漏洞、DirectoryIterator及各种二进制选手插足的方法
九、条件竞争，包括竞争删除前生成shell、竞争数据库无锁多扣钱
十、社工，包括花式查社工库、微博、QQ签名、whois
十一、windows特性，包括短文件名、IIS解析漏洞、NTFS文件系统通配符、::$DATA，冒号截断
十二、SSRF，包括花式探测端口，302跳转、花式协议利用、gophar直接取shell等
十三、XSS，各种浏览器auditor绕过、富文本过滤黑白名单绕过、flash xss、CSP绕过
十四、XXE，各种XML存在地方（rss/word/流媒体）、各种XXE利用方法（SSRF、文件读取）
十五、协议，花式IP伪造 X-Forwarded-For/X-Client-IP/X-Real-IP/CDN-Src-IP、花式改UA，花式藏FLAG、花式分析数据包
```

原链接: http://weibo.com/ttarticle/p/show?id=2309403980950244591011  


2016/5/30  
