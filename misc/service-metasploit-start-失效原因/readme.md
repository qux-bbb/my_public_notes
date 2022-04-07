# service metasploit start 失效原因

kali linux 2.0 本身已内置metasploit，没有metasploit 这个服务了，所以 service metasploit start 不起作用。  

在kali 2.0中启动带数据库支持的MSF方式如下：  
1. 首先启动postgresql数据库: `/etc/init.d/postgresql start` 或者 `service postgresql start`
2. 初始化MSF数据库: `msfdb init`
3. 运行msfconsole: `msfconsole`
4. 在msf中查看数据库连接状态: `db_status`
5. 建立缓存: `db_rebuild_cache`


原链接: https://blog.csdn.net/jiangliuzheng/article/details/50546373  


2016/6/8  
