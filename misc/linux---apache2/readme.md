# linux---apache2

官网: https://httpd.apache.org/  
官方文档: https://httpd.apache.org/docs/current/  

Apache HTTP Server ("httpd") 提供与当前HTTP标准同步的HTTP服务。  

安装启动：  
```r
sudo apt install apache2
sudo service apache2 start
```

默认网站路径: /var/www/html/  

配置文件目录：  
```r
/etc/apache2
├── apache2.conf
├── conf-available
│   ├── security.conf
│   └── serve-cgi-bin.conf
├── conf-enabled
│   ├── security.conf -> ../conf-available/security.conf
│   └── serve-cgi-bin.conf -> ../conf-available/serve-cgi-bin.conf
├── ports.conf
├── sites-available
│   ├── 000-default.conf
└── sites-enabled
    └── 000-default.conf -> ../sites-available/000-default.conf
```


2022/6/11  
