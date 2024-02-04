# 构建live镜像相关

在Debian12下构建成功  


## 安装工具和依赖
```bash
sudo apt-get update
sudo apt-get install live-build
```

## 构建默认镜像
配置  
```bash
mkdir tutorial1 ; cd tutorial1 ; lb config
```

切换到root  
```bash
sudo su
```

构建  
```bash
lb build 2>&1 | tee build.log
```


## 构建包含图形界面和浏览器的镜像
配置阶段增加一条命令，其它阶段不变  
```bash
echo "task-lxde-desktop firefox-esr" >> config/package-lists/my.list.chroot
```


## 一些问题解决
### 问题
```r
E: Failed getting release file http://archive.ubuntu.com/ubuntu/dists/precise/Release
```

解决方法：  
precise是ubuntu12的代号，太老了，可以全局搜索"precise"替换成ubuntu22的代号"jammy"  


### 问题2
```r
E: Package 'firmware-linux' has no installation candidate
```

解决方法：
```bash
sudo apt install firmware-linux
```

### 问题3
```r
cp: cannot stat 'chroot/boot/vmlinuz-*': No such file or directory
E: An unexpected failure occurred, exiting...
```

解决方法：  
chroot切换根目录(chroot chroot)之后安装依赖，装完之后再退出来(exit)  
```bash
apt update
apt install linux-image-amd64  # 需要根据架构安装相应的包
```


## 信息来源
1. Debian Live Manual: https://live-team.pages.debian.net/live-manual/
2. 一些简单的示例: https://live-team.pages.debian.net/live-manual/html/live-manual/examples.en.html
3. chatgpt
4. 文心一言


---
2024/2/3  
