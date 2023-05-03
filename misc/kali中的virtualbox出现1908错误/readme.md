# kali中的virtualbox出现1908错误

没解决问题，直接重装了，也是个办法  

```bash
# 卸载virtualbox
apt purge virtualbox

# 更新到最新状态
apt update
apt upgrade

# 安什么头的东西
apt-get install linux-headers-$(uname -r)

# 重装virtualbox
apt install virtualbox
```


2018/1/16  
