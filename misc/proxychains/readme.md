# proxychains

proxychains 可以给程序做代理。  

github地址: https://github.com/haad/proxychains  

ubuntu安装: `sudo apt install proxychains`  

修改配置文件 `/etc/proxychains.conf`, 注释最后一行，然后加一行，如下：  
```conf
#socks4 	127.0.0.1 9050
socks5 127.0.0.1 1080
```

使用示例：  
```bash
proxychains firefox
proxychains google-chrome --no-sandbox
```


2021/4/5  
