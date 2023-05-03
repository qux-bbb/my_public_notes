# Kali渗透测试技术实战-笔记

```
安装在U盘（持久性保存）
Linux系统上安装 可以持久性保存
非加密版
1. fdisk  -l
2. end=7gb
3. read start _ < <(du -bcm kali-linux-1.0.8-amd64.iso | tail -1); echo $start parted /dev/sdb mkpart primary $start $end
4. mkfs.ext3 -L persistence /dev/sdb3
5. e2label /dev/sdb3 persistence
6. mkdir -p /mnt/my_usb
7. mount /dev/sdb3 /mnt/my_usb
8. echo "/ union" > /mnt/my_usb/persistence.conf
9. umount /dev/sdb3

加密版
1. fdisk  -l
2. end=7gb
3. read start _ < <(du -bcm kali-linux-1.0.8-amd64.iso | tail -1); echo $start
parted /dev/sdb mkpart primary $start $end
4. cryptsetup --verbose --verify-passphrase luksFormat /dev/sdb3
5. cryptsetup luksOpen /dev/sdb3 my_usb
6. mkfs.ext3 -L persistence /dev/mapper/my_usb
7. e2label /dev/mapper/my_usb persistence
8.mkdir -p /mnt/my_usb
9. mount /dev/mapper/my_usb /mnt/my_usb
10. echo "/ union" > /mnt/my_usb/persistence.conf
11. umount /dev/mapper/my_usb
12. cryptsetup luksClose /dev/mapper/my_usb


其实可以看kali官方文档：http://docs.kali.org/downloading/kali-linux-live-usb-persistence
命令比较多
--------------------------------------------------------------------------------
APT软件包处理工具
安装软件	
apt-get	install	{package_name}
更新--获得应用程序或软件包的更新版本
apt-get	update
升级软件
apt-get	upgrade
版本升级
apt-get	dist-upgrade
移除应用程序或软件包
apt-get	remove	{package_name}
自动移除--更新后系统不再需要的软件包
apt-get	autoremove
完全移除--清除应用程序软件包和相关的配置文件（慎用）
apt-get	purge	{package_name}
清理--下载的安装软件包
apt-get	clean
自动清理--删除所有已经被新版本替换掉的旧软件包文件
apt-get	autoclean
安装好所有最新的补丁、软件包和更新
1. apt-get  update  && apt-get  upgrade  &&  apt-get  dist-upgrade
2.  apt-get  autoremove  &&  apt-get autoclean
--------------------------------------------------------------------------------
Debian软件包管理器
安装
dpkg  -i  {package_name.deb}
移除
dpkg  -r  {package_name.deb}
完全移除
dpkg  -P  {package_name.deb}	# 大写 P
检查已安装软件包或移除的软件包的状态
dpkg  -l  {package_name.deb}
查看已安装的软件包更详细的信息
dpkg  -p  {package_name.deb}	#小写 p
--------------------------------------------------------------------------------
TAR压缩包
将当前目录中的所有文件压缩成一个文件包
c：创建一个新存档文件
z：压缩这个文件
f：指定选项后的参数作为创建的压缩包的文件名(后缀名 .tar.gz  不是必须，是linux完全兼容的用法，也是压缩文件的标准表示)
tar  -czf  tarball_file.tar.gz  *

从压缩的tar文件包中提取文件
tar  -xf  tarball_file.tar.gz  -C  {directory_for_files}
--------------------------------------------------------------------------------
配置网络接口
ifconfig  -a   查看计算机上的所有网卡的当前配置（eth0是第一个以太网适配器，lo是回路或内部接口）
ifconfig  eth0  down  停止第一个以太网适配器
ifconfig  eth0  up  启动第一个以太网适配器
ifconfig  eth0  192.1687.1.22  更改该适配器的IP地址
ifconfig  eth0  192.1687.1.22  netmask  255.255.255.0  同时更改IP地址和子网掩码

route  add  default  gw  192.168.1.2  更改默认网关

DNS服务器设置
echo  nameserver  4.4.4.4  > /etc/resolv.conf  删除已有DNS服务器并重新设置
echo  nameserver  8.8.8.8  > /etc/resolv.conf  追加域名服务器
（其实就是更改文件内容，利用重定向而已）

配置DHCP
nano  /etc/networking/interfaces
#将下面的行写入文件#
auto  eth0
iface  eht0  inet  static
address  {IP_address}
netmask  {netmask}
gateway  {Gateway_IP_Address}
#保存并退出#
（可能需要重新启动网卡）

dhclient  eth0  将网卡配置成DHCP服务器提供的设置
--------------------------------------------------------------------------------
手动挂载驱动器
mkdir  /media/newdrive
fdisk  查看要挂载的驱动器名称
mount  /dev/hdb1  /media/newdrive
cd  /media/newdrive
(其实就是新建一个文件夹，把驱动器mount到文件夹，就可以在文件夹里查看修改驱动器内容了)
--------------------------------------------------------------------------------
网站镜像
复制网站的html页面，不能复制服务器端的程序页面
wget  -m  -p  -E  -k  -K  -np  -v  http://foo.com
m 镜像，打开该选项，适用于镜像Web站点
P  页面或先决条件，该选项确保包含了请求的图片和css脚本的文件被下载
E 适应扩展，该选项使所有页面能够在本地另存为一个html文件
k  转换链接，该选项确保文件被转换，用于本地浏览
K  转换备份文件，将会以a.orig为后缀备份原始文件
--------------------------------------------------------------------------------
ping
ping  192.168.1.1  判断主机是否存活
traceroute
traceroute  www.google.com  找到并列出在发起traceroute的机器和目标机器之间的设备
（windows上是tacert）
--------------------------------------------------------------------------------
Nmap
不仅可以确定目标网络上计算机的存活状态，在许多情况下，还能确定主机的操作系统、监听的端口、服务，还有可能获得用户的证书
扫描选项
-sS  隐蔽扫描
-sT  TCP连接扫描
-sU  UDP扫描
-sA  ACK扫描

-T0  慢速的网络连接
-T1
-T2
-T3  默认的扫描方式，第一个使用并行处理技术的模板
-T4
-T5

IP地址段
nmap  10.0.2.1-255
nmap 10.0.2.1/24    CIDR寻址表示

使用文本文件作为目标列表输入
nmap  -iL  targets.txt

选择端口
nmap -sS  -p  1-100  连续端口
nmap  -sU  -p  53，137，138	   逐个指定

输出选项
-oN  普通输出：nmap  -oN metascan.txt  10.0.2.100
-oX  XML文件输出：nmap  -oX metascan.xml 10.0.2.100
......
--------------------------------------------------------------------------------
NetCat(nc)
作为指纹采集工具或监听发来的连接
nc  192.168.56.102  80帮助判断Web服务器和它的操作系统

Telnet
同netcat
telnet  192.168.56.102：80

SSLScan
判断Web服务器使用的加密算法，并返回SSL证书
--------------------------------------------------------------------------------
w3af

```


2016/11/9  
