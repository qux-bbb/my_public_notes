# linux--查看和清除登录痕迹

```r
# 查看登录成功记录
last
# 查看登录失败记录
lastd
# 查看历史执行命令
history

# 清除登录成功记录
echo > /var/log/wtmp
# 清除登录失败记录
echo > /var/log/btmp
# 清除历史执行命令 也可以 `echo > ~/.bash_history`
history -c
```


2018/7/18  
