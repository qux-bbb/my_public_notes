# 配置manjarocn仓库

## 正常导入流程
添加 manjarocn 到 /etc/pacman.conf(如果使用archlinuxcn，确保manjarocn在前面)  
```
[manjarocn]
Server = https://repo.manjarocn.org/stable/x86_64
```
导入GPG keys  
```bash
sudo pacman-key --recv-keys 974B3711CFB9BF2D && sudo pacman-key --lsign-key 974B3711CFB9BF2D
```

## 问题解决
如果导入出现这样的错误：  
```
gpg: 从公钥服务器接收失败：无名称
==> 错误： 无法从密匙服务器中正确取回远端密匙。
```
编辑 /etc/pacman.d/gnupg/gpg.conf，在最后添加一行：  
```
keyserver hkp://pgp.mit.edu:11371
```
这样应该就可以正常导入了  


参考链接：  
1. https://github.com/manjarocn/repo
2. https://www.reddit.com/r/archlinux/comments/o5rcs6/psa_you_need_to_update_your_keyserver/
