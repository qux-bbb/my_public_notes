# nginx---反向代理

nginx的反向代理，我现在理解就是把别的网站的内容给请求过来，然后返回给客户端  

安装nginx  
```r
apt install nginx
```

编辑 `/etc/nginx/nginx.conf`，在http的大括号中的最后添加如下内容：  
```r
server {
    listen 88;
    location /hello/ {
        proxy_pass http://1.2.3.4/world/;
    }
}
```

重启nginx  
```r
service nginx restart
```

如果要代理整个网站，可以写location为：  
```r
location / {
    proxy_pass http://1.2.3.4;
}
```

要注意的东西：  
80端口有nginx默认的服务，如果想关掉默认服务，需要删除 `/etc/nginx/sites-enabled/default` 文件  

site-available文件夹，写可用的配置  
site-enable文件夹，写启用的部分，是site-available中配置文件的软链接  


---
2018/8/19  
