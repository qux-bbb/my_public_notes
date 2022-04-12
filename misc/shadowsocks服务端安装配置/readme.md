# shadowsocks服务端安装配置

安装：  
```r
pip install shadowsocks
```

写配置文件，随便写在什么位置：  
```r
{
"server":"service_ip",
"server_port":8388,
"local_port":1080,
"password":"your_pass",
"timeout":300,
"method":"aes-256-cfb"
}
```
假设是ss.json  

启动服务：  
```r
ssserver -c ss.json -d start  # 加 -d 可以后台启动
```

2017/9/2  
