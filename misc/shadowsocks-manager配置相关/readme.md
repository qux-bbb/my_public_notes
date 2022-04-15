# shadowsocks-manager配置相关

shadowsocks-manager可以更好地管理多用户，进行流量控制、统计等  

## 0x00 准备 
前提，安装shadowsock：  
```r
apt-get install python-pip
pip install git+https://github.com/shadowsocks/shadowsocks.git@master
```

## 0x01 manageer安装
安装正确版本的nodejs：  
```r
curl -sL https://deb.nodesource.com/setup_8.x | bash -
apt-get install nodejs -y
```

从npm安装shadowsocks-manager：  
```r
# 使用该命令也可以更新manager
npm i -g shadowsocks-manager
```

## 0x02 启动

/root/.ssmgr/default.yml内容  
```yaml
type: s

shadowsocks:
  address: 127.0.0.1:6001

manager:
  address: 127.0.0.1:6002
  password: 'need_same'

db: 'db.sqlite'

# db:
#   host: '1.1.1.1'
#   user: 'root'
#   password: 'abcdefg'
#   database: 'ssmgr'
```
/root/.ssmgr/webui.yml内容(email的username和password已改)  
```yaml
type: m

manager:
  address: 127.0.0.1:6002
  password: 'need_same'

plugins:
  flowSaver:
    use: true
  user:
    use: true
  account:
    use: true
  macAccount:
    use: true
  group:
    use: true
  email:
    use: true
    username: '12345678@qq.com'
    password: 'zheshishenmegui'
    host: 'smtp.qq.com'
  webgui:
    use: true
    host: '0.0.0.0'
    port: '80'
    site: 'http://www.mydomain.com'
    # cdn: 'http://xxx.xxx.com'
    # icon: 'icon.png'
    # skin: 'default'
    # googleAnalytics: 'UA-xxxxxxxx-x'
    # gcmSenderId: '456102641793'
    # gcmAPIKey: 'AAAAGzzdqrE:XXXXXXXXXXXXXX'
  # alipay:
  #   use: true
  #   appid: 2015012104922471
  #   notifyUrl: 'http://yourwebsite.com/api/user/alipay/callback'
  #   merchantPrivateKey: 'xxxxxxxxxxxx'
  #   alipayPublicKey: 'xxxxxxxxxxx'
  #   gatewayUrl: 'https://openapi.alipay.com/gateway.do'
  webgui_telegram:
    use: true
    token: '191374681:AAw6oaVPR4nnY7T4CtW78QX-Xy2Q5WD3wmZ'
  # paypal:
  #   use: true
  #   mode: 'live' # sandbox or live
  #   client_id: 'At9xcGd1t5L6OrICKNnp2g9'
  #   client_secret: 'EP40s6pQAZmqp_G_nrU9kKY4XaZph'

db: 'webgui.sqlite'
```


命令：  
```r
# 以管理方式启动ss
ss-manager -m aes-256-cfb -u --manager-address 127.0.0.1:6001

# 以server模式启动ssmgr，使用的是默认配置文件defaul.yml
ssmgr

# 以manager模式启动ssmgr，使用的是webui.yml，指定的配置文件是相对路径的话，ssmgr会去/roo/.ssmgr文件夹下查找
ssmgr -c webui.yml
```

可以将上面的命令写入/etc/rc.local文件，设置后台启动，这样重启之后也能继续提供服务，如下：  
```r
nohup ss-manager -m aes-256-cfb -u --manager-address 127.0.0.1:6001 &
nohup ssmgr &
nohup ssmgr -c webui.yml &
```
放在`exit 0`之前即可  


注意：  
ssmgr会自动移除未经认证(在数据库中不存在)就连接的账号(端口和密码)  

digitalocean的smtp服务需要找客服开一下  

default.yml和webui.yml中manager的部分需要保持对应关系  

如果要限制每个账号的登录数量，可以用iptables规则限制  
```r
iptables -I INPUT -p tcp --dport 1024:10240 -m connlimit --connlimit-above 5 -j DROP
iptables -I OUTPUT -p tcp --dport 1024:10240 -m connlimit --connlimit-above 5 -j DROP
```

如果要配置https，用nginx配置https，做一下端口转发即可，webui中的site要做更改，不然影响密码重置功能，更改为 https://www.mydomain.com:<nginx 服务端口>  


2018/8/19  
