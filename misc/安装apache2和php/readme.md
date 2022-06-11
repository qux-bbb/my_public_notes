# 安装apache2和php

Install:  
```r
sudo apt-get install apache2 php7.0 libapache2-mod-php7.0 
```

Verify:  
```r
a2query -m php7.0
```

Load:  
```r
sudo a2enmod php7.0
```

Restart apache:  
```r
sudo service apache2 restart
```

原链接: https://askubuntu.com/questions/451708/php-script-not-executing-on-apache-server  


2019/5/28  
