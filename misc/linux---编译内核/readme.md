# 编译内核

编译linux内核体验一下  
参考这篇文章: https://linux.cn/article-9665-1.html  
这是原文: https://www.linux.com/topic/desktop/how-compile-linux-kernel-0/  


## 步骤
先看看当前内核版本：  
```sh
$ uname -r
5.4.70-amd64-desktop
```

从https://www.kernel.org/下载最新版本的linux内核源码，我下载的是：  
https://cdn.kernel.org/pub/linux/kernel/v5.x/linux-5.11.3.tar.xz  
只有112M  

解压: `tar -Jxvf linux-5.11.3.tar.xz`, 变成了1.2G  

设置内核配置，看看就好，不了解就不要随便改  
```bash
# 进入目录
cd linux-5.11.3
# 复制当前系统的内核配置
cp /boot/config-$(uname -r) .config
# 打开配置工具进行配置
make menuconfig
```

执行命令: `make`, 要花很长时间  

安装模块: `sudo make modules_install`  

安装内核: `sudo make install`  

找到对应模块名称: `ls /lib/modules`, 我的是`5.11.3-amd64-desktop`  
启用内核作为引导: `sudo update-initramfs -c -k 5.11.3-amd64-desktop`  

更新一下grub: `sudo update-grub`  

重启  

最后看看内核版本：  
```sh
$ uname -r
5.11.3-amd64-desktop
```


## 遇到的问题
### 启用内核作为引导 缺失一些依赖
我这里缺失的依赖都按提示安装了  
```sh
sudo apt install console-setup
sudo apt install plymouth-themes
```

### 启用内核作为引导 报错'gzip: stdout: No space left on device'  
原因是/boot空间不够用了，找一块大磁盘挂载到/boot即可  
比如这样: `sudo mount /dev/mapper/vg0-_dde_data /boot`  
参考：https://askubuntu.com/questions/223248/gzip-stdout-no-space-left-on-device-while-upgrading-the-kernel  

### 重启选择新内核后，报错'end kernel panic - not syncing: System is deadlocked on memory'  
原因是内存不够大，我把虚机关机，内存从4G调成8G，重启就好了  
参考: https://unix.stackexchange.com/questions/492667/compiled-kernel-4-19-will-not-boot-kernel-panic-not-syncing-system-is-deadlo  
