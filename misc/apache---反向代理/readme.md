# apache---反向代理

编辑 `/etc/apache2/sites-enabled/000-default.conf`  
在 `<VirtualHost *:80>` 标签中的最后添加如下形式：  
```r
ProxyPass /hello/ http://1.2.3.4/world/
```

重启apache即可  


2018/8/21  
