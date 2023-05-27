# ss相关

## Github地址：  
主要就下面两个吧  
https://github.com/shadowsocks/shadowsocks  
https://github.com/shadowsocks/shadowsocks-android  

## 程序下载
电脑客户端下载地址: https://github.com/shadowsocks/shadowsocks-windows/releases  
Android客户端下载: https://github.com/shadowsocks/shadowsocks-android/releases  

## 多端口配置文件
```
{ 
    "server":"ip",
    "port_password":{
        "30696": "pass0" ,
        "30697": "pass1" ,
        "30698": "pass2" ,
        "30699": "pass3" ,
        "30700": "pass4"
        },
    "local_port":1080,
    "timeout":600,
    "method":"aes-256-cfb"
}

```

## 普通用户启动
`ssserver --manager-address /var/run/shadowsocks-manager.sock -c /root/ss/ss.json --user nobody -d start`

## 设置服务端开机运行（linux程序都适用）
在`/etc/rc.local`中添加命令:  
`sudo ssserver -c /etc/shadowsocks.json --user nobody -d start`

## 设置BBR的脚本地址
https://github.com/teddysun/across/


---
2018/8/22  
