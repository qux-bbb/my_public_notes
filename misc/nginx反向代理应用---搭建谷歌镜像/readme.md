# nginx反向代理应用---搭建谷歌镜像

如果要搭建谷歌镜像，需要自己生成一个服务器证书，这里采用了自签名证书，一定要是外网的服务器  

## 0x01 安装nginx  
```r
apt install nginx
```

## 0x02 生成自签名证书
```r
cd /etc/nginx
mkdir ssl
cd ssl
openssl genrsa -out server.key 2048
openssl req -new -x509 -key server.key -out server.cer
```

## 0x03 编辑nginx配置
编辑 `/etc/nginx/nginx.conf`，在http的大括号中的最后添加如下内容  
```r
server {
    listen 443;
    ssl on;
    ssl_certificate /etc/nginx/ssl/server.cer;
    ssl_certificate_key /etc/nginx/ssl/server.key;
    
    location / {
        proxy_pass https://www.google.com;    
    }    
}
```

## 0x04 重启nginx
```r
service nginx restart
```
这样之后就可以访问 `https://your_domain_or_ip`，看到谷歌搜索页面了  

## 0x05 80端口的问题
nginx有一个默认文件，会在80端口开启一个服务，如果80有其他用途，可以把/etc/nginx/site-enabled/default删掉  


---
2018/8/20  
