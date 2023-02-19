# kali安装ss配置代理

非常久，不用了，仅转移记录，新的可以用v2raya  

假设已经配好了服务器ss


## 安装配置shadowsocks
```r
pip install git+https://github.com/shadowsocks/shadowsocks.git@master
```
不能直接 `pip install shadowsocks`, 那样有点问题  

创建配置文件ss.json：  
```r
{
    "server":"my_server_ip",
    "server_port":8388,
    "local_address": "127.0.0.1",
    "local_port":1080,
    "password":"mypassword",
    "timeout":300,
    "method":"aes-256-cfb",
    "fast_open": false
}
```
前5个参数修改为自己配置的  

启动shadowsocks：  
```r
sslocal -c ss.json -d start
```

## polipo实现全局代理
安装polipo：  
```r
sudo apt-get install polipo
```

修改polipo的配置文件 `/etc/polipo/config`，添加以下内容：  
```r
proxyAddress = "0.0.0.0"
socksParentProxy = "127.0.0.1:1080"
socksProxyType = socks5
chunkHighMark = 50331648
objectHighMark = 16384
serverMaxSlots = 64
serverSlots = 16
serverSlots1 = 32
```

重启polipo服务：  
```r
/etc/init.d/polipo restart
```

终端使用代理：  
```r
export http_proxy="http://127.0.0.1:8123/"
curl ip.sb
```

firefox使用代理：  
选择 Manual -> proxy -> configuration  
http proxy 填: 127.0.0.1, port填: 8123  
选中 `Use this proxy server for all protocols`  

## 借助proxychains使用代理
也可以不用polipo实现，kali下自带一个proxychains，使用比较简单  

```r
vim /etc/proxychains.conf 
```
把最下方一行注释掉，然后新添加一行，最后如下：  
```r
#socks4 	127.0.0.1 9050
socks5 127.0.0.1 1080
```

打开浏览器例子：  
```r
proxychains firefox
proxychains google-chrome --no-sandbox
```

github地址: https://github.com/haad/proxychains  
官网地址: http://proxychains.sourceforge.net/  


---
2017/9/2  
