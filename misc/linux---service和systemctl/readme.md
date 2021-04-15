# linux---service和systemctl
`service` operates on the files in /etc/init.d and was used in conjunction with the old init system.  
`systemctl` operates on the files in /lib/systemd. If there is a file for your service in /lib/systemd it will use that first and if not it will fall back to the file in /etc/init.d. Also If you are using OS like ubuntu-14.04 only service command will be available.  

So if systemctl is available ,it will be better to use it.  

systemctl比service新而且兼容service，建议优先使用systemctl  


原链接: https://stackoverflow.com/questions/43537851/difference-between-systemctl-and-service-command  


2021/4/11  
