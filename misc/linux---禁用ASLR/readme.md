# linux---禁用ASLR
ASLR  
Address Space Layout Randomization : : 地址空间布局随机化  

默认远程服务器开启，开启之后 堆/栈/libc 的地址会有一段偏移，代码段不变  

## 临时修改
root用户  
```bash
echo 0 > /proc/sys/kernel/randomize_va_space
```

如果不是root用户, 而且有sudo的权限, 可以这样  
```bash
sudo sh -c "echo 0 > /proc/sys/kernel/randomize_va_space"
```

参考: https://www.cnblogs.com/scrat/p/3505930.html  

## 永久修改
编辑 /etc/sysctl.conf, 添加：  
```r
kernel.randomize_va_space=0
```
这样系统启动时就会禁用ASLR，如果想立即生效，可以执行命令：  
```r
sudo sysctl -p
```

参考：chatgpt  


2020/6/30  
