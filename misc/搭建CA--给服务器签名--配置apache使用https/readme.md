# 搭建CA--给服务器签名--配置apache使用https

自建CA，制作服务器证书  

正常的获取web服务器所需证书的过程：  
1. generate a strong private key  
2. create a Certificate Signing Request (CSR) and send it to a CA  
3. install the CA-provided certificate in your web server  

---

## 0x01 CA准备
```sh
# 1. 建立CA目录结构
# 按照OpenSSL的默认配置建立CA，需要在文件系统中建立相应的目录结构。
# -- demoCA/
#     |-- index.txt
#     |-- newcerts/
#     |-- private/
#     |-- serial
# 2. 生成CA证书的RSA密钥对
# 我们知道，要利用公钥机制，必须先建立密钥文件
# 3. 生成CA证书请求
# 4. 对CA证书请求进行自签名

# 自己找一个目录就可以
mkdir -p ./demoCA/{private,newcerts}
touch ./demoCA/index.txt
echo 01 > ./demoCA/serial  
openssl genrsa -out ./demoCA/private/cakey.pem 2048
openssl req -new -x509 -days 3650 -key ./demoCA/private/cakey.pem -out ./demoCA/cacert.pem
# 这里需要填写Common Name，随便写一个
```


## 0x02 服务端证书准备
```sh
# 1. 生成服务端证书的RSA密钥对
# 和根CA一样，生成服务端证书同样也是使用RSA机制，自然也需要为服务端生成一个RSA私钥文件(但不能和CA的一样)
# 2. 生成服务端证书请求
# 3. 使用CA根书对"服务端请求签发证书文件"进行签名 

# 和demoCA在同一级目录下操作
cp /usr/lib/ssl/openssl.cnf ./
# 如果要支持谷歌浏览器，需要修改openssl.conf的内容，在[ v3_req ]下的最后位置增加以下内容(去掉一开始的#号，DNS.1，DNS.2可以没有)
# subjectAltName = @alt_names

# [alt_names]
# IP.1 = your ip
# DNS.1 = your ip
# DNS.2 = your domain

openssl genrsa -out server.key
openssl req -new -days 3650 -key server.key -out serverreq.pem
# ..填写证书申请者的身份信息..(Common Name不能为空，值应该为上面的IP.1 或DNS.1或者DNS.2中的一个， 申请证书的countryName必须和CA的countryName相同，保持相同的方法都默认别写就好了)

# CA生成签名的服务器证书
openssl ca -in serverreq.pem -out servercert.cer -config openssl.cnf -extensions v3_req
```


## 0x03.1 配置apache的SSL证书
要配置apache的SSL通信，需要为apache配置服务端的"服务器根证书"  

```sh
# ubuntu服务器，安装apache2
apt install apache2
# 开启apache2的ssl模块
sudo a2enmod ssl
# 创建相应目录
mkdir /etc/apache2/ssl
# 将0x02中生成的server.key和servercert.cer复制到/etc/apache2/ssl目录下
```
编辑/etc/apache2/sites-enabled/000-default.conf，添加如下内容
```xml
<VirtualHost *:443>
        SSLEngine on
        SSLCertificateFile /etc/apache2/ssl/servercert.cer
        SSLCertificateKeyFile /etc/apache2/ssl/server.key

        ServerAdmin webmaster@localhost
        DocumentRoot /var/www/html

        ErrorLog ${APACHE_LOG_DIR}/error.log
        CustomLog ${APACHE_LOG_DIR}/access.log combined
</VirtualHost>
```
重启apache  
```sh
service apache2 restart
```


## 0x03.2 配置nginx的SSL证书
也可以用nginx来提供服务器的https服务，步骤和Apache基本一致  

```sh
# ubuntu服务器，安装nginx
apt install nginx
# 在/var/www/目录下创建index.html并编辑，之后会作为网站主页使用
# 创建相应目录
mkdir /etc/nginx/ssl
# 将0x02中生成的server.key和servercert.cer复制到/etc/nginx/ssl目录下
```
编辑/etc/nginx/nginx.conf，在http的大括号中的最后添加如下内容
```json
     server {
         listen 443;
         ssl on;
         ssl_certificate /etc/nginx/ssl/servercert.cer;
         ssl_certificate_key /etc/nginx/ssl/server.key;
         root /var/www/;
     }
```
重启nginx  
```sh
service nginx restart
```


## 0x04 本地安装证书
将ca的证书(cacert.pem)复制到客户端，改后缀为cer或者crt，双击安装即可，注意要将证书安装到"受信任的根证书颁发机构"  
(火狐需要另外在浏览器中导入证书)  


参考：  
https://www.cnblogs.com/LittleHann/p/3738141.html  
http://blog.sina.com.cn/s/blog_67938fe30102v80q.html (NET::ERR_CERT_COMMON_NAME_INVALID错误的解决方法)  


---
2018/8/16  
