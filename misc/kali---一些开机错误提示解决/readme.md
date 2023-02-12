# kali---一些开机错误提示解决

## 问题1
```r
piix4_smbus 0000:00:007.3: Host SMBus controller not enabled

intel_rapl: no valid rapl domains found in package 0 错误解决
```
2个问题可以一起解决：打开 `/etc/modprobe.d/blacklist.conf` 末尾加入2行内容之后重启  
```r
blacklist i2c-piix4
blacklist intel_rapl
```
如果找不到 `blacklist.conf`，可在 `blacklist-libnfc.conf` 中修改  


## 问题2
```r
failed to start open vulnerability assessment System manager daemon
```
解决：终端下 `chmod 777 /var/log/redis/redis-server.log`  


2016/3/17  
