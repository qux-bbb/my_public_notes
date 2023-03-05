# 无效的命令ProxyPass

用apache2的时候出了这样的错：  
```r
Problem ⇒ Invalid command 'ProxyPass', perhaps misspelled or defined by a module not included in the server configuration
```

解决方法：  
```r
LoadModule proxy_http_module modules/mod_proxy_http.so  
```

在Ubuntu上这样操作：  
```r
cd /etc/apache2/mods-enabled
sudo ln -s ../mods-available/proxy_http.load proxy_http.load
sudo ln -s ../mods-available/proxy_ajp.load proxy_ajp.load
sudo ln -s ../mods-available/proxy.load proxy.load  sudo service apache2 restart
```

原链接: http://www.kriblog.com/server/webserver/apache/invalid-command-proxypass-perhaps-misspelled-or-defined-by-a-module-not-included-in-the-server-configuration.html  


2017/1/13  
