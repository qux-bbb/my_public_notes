# termux

termux是一个Android平台的Linux终端环境程序。  
官网: https://termux.com  

对我来说就是可以在Android上用linux的终端，而且生成或下载的文件可以用Android操作。  

## 获取手机存储访问权限
获取手机存储访问权限，执行命令: `termux-setup-storage`  

## 换源
```bash
termux-change-repo
```
注意按"空格"切换源  

## 安装配置fish
```bash
pkg install fish
```

## 设置默认shell
```bash
chsh -s fish
```

## 更新出现403错误
更新可以用 apt 或者 pkg  

如果出现403错误，执行 `rm -f ${PREFIX}/etc/apt/sources.list.d`，然后正常更新即可

原链接: https://www.zhihu.com/question/338094182  

## 管理服务
https://wiki.termux.com/wiki/Termux-services  
https://github.com/termux/termux-services  

termux管理服务的程序是 `sv`，和service命令基本一致，也可以用它自己特征的命令  

```bash
# 启动
sv up sshd
# 停止
sv down sshd
# 开机启动
sv-enable sshd
# 禁止开机启动
sv-disable sshd
```

## cron
cron需要安装启用  
```r
pkg install cronie termux-services
sv-enable crond
```
然后就和正常linux发行版一样了  

原链接: https://www.reddit.com/r/termux/comments/i27szk/how_do_i_crontab_on_termux/  

## Tasker
Tasker插件不能用来定时执行任务  

## signal 9
如果安装了nethunter，启动桌面环境，Termux进入后台，Android大概率会杀死这个占用CPU太高的进程，Termux就会报如下错误：  
```r
[Process completed (signal 9) - press Enter]
```

可以把Termux设置小窗悬浮，可以避免一段时间的这个问题，并不完全有效。  

参考链接: https://www.bilibili.com/read/cv20060713/  
