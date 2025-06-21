# v2rayA

Qv2ray不维护了，发现了v2rayA。  
一个易用而强大的，跨平台的 V2Ray 客户端。  

官网: https://v2raya.org/  

默认监听0.0.0.0:2017，设置密码时需要保证强度


## Windows安装
在这里下载名称类似 installer_windows_inno_x64_*.exe，执行即可按步骤安装  
https://github.com/v2rayA/v2rayA/releases  

安装后通过运行桌面快捷方式或直接访问 http://127.0.0.1:2017 打开管理页面  
创建账号、导入节点、启动服务，开始使用  
可以新增出站(即新分组)，便于分组使用，每组可以选择多个节点，实现负载均衡  
选节点前先关闭服务，选完之后再启动服务，这样快很多，不然每选一个节点就要重启内容，等待时间比较长  


## kubuntu安装
参考链接：https://v2raya.org/docs/prologue/installation/debian/  

安装v2raya  
```r
# 添加公钥，看到终端有公钥输出才算添加成功
wget -qO - https://apt.v2raya.org/key/public-key.asc | sudo tee /etc/apt/keyrings/v2raya.asc

# 添加 V2RayA 软件源
echo "deb [signed-by=/etc/apt/keyrings/v2raya.asc] https://apt.v2raya.org/ v2raya main" | sudo tee /etc/apt/sources.list.d/v2raya.list
sudo apt update

# 安装 V2RayA
sudo apt install v2raya v2ray ## 也可以使用 xray 包
```

注意!!!：建议就用方法一安装，方法二手动安装deb包会出现下面的错误，还不知道怎么解决
```r
failed to connect: failed to connect: geoip.dat or geosite.dat file does not exists

Get "https://github.com/v2rayA/dist-v2ray-rules-dat/raw/202410012212/geosite.dat": dial tcp: lookup github.com on 127.0.0.53:53: server misbehaving
```

启动 v2rayA / 设置 v2rayA 自动启动  
```r
# 启动 v2rayA
sudo systemctl start v2raya.service
# 设置开机自动启动
sudo systemctl enable v2raya.service
```

然后可以访问: http://localhost:2017  
创建账号、导入节点、启动服务，开始使用  

如果忘记了密码，可以执行命令重置密码：  
```r
sudo systemctl stop v2raya
sudo v2raya --reset-password
sudo systemctl start v2raya
```


---
2021/12/30  
