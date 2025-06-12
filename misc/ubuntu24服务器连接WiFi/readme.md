# ubuntu24服务器连接WiFi

安装ubuntu24服务器，安装时没有配置联网，装完之后/etc/netplan下没有配置文件，可以自己建一个文件如wifi.yaml：
```yaml
network:
  renderer: networkd
  wifis:
    wlp3s0:  # 无线网卡名称
      dhcp4: true  # 启用 DHCP 获取 IPv4 地址
      access-points:
        "Your-WiFi-SSID":  # 替换为你的 WiFi 名称
          password: "Your-WiFi-Password"  # 替换为 WiFi 密码
```

修改文件权限为root只读写：
```bash
sudo chmod 600 wifi.yaml
```

验证配置：
```bash
sudo netplan generate
```

应用配置：
```bash
sudo netplan apply
```

等一会儿就能连上WiFi了


2025/6/12
