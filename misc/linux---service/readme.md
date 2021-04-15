# linux---service
service可以自启动，在后台做一些事情。  

创建一个service需要自己写脚本，放在 `/etc/init.d/` 下。  
service命令其实是去`/etc/init.d`目录下，执行相关脚本。  

假设服务名为`redis`, 下面是简单操作：  
```bash
# service命令启动redis脚本
service redis start
# 直接启动redis脚本
/etc/init.d/redis start
# 设置服务开机启动
update-rc.d redis enable
```


原链接: https://www.jb51.net/article/169195.htm  
