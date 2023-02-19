# kali---新建用户的Desktop问题

keywords: 桌面 Desktop 中文 英文

新建用户，如果直接切成中文，Desktop 之类的目录就都是中文了，改不回来  

所以可以先全部设置成英文，退出重登，直到看到用户目录下已经生成英文的目录，这样之后再切到中文，目录就不会变成中文了，就很舒服  


如果上述方法不行，我们强制设置一下:  
1. 输出当前语言：`echo $LANG`，我这里是 "zh_CN.UTF-8"  
2. 设置当前语言：`export LANG=en_US.UTF-8`  
3. 执行命令：`xdg-user-dirs-update --force`  
4. 还原语言：`export LANG=zh_CN.UTF-8`  
5. 删除原来的中文目录
6. log out 重新登录

参考链接：https://wiki.archlinux.org/index.php/XDG_user_directories_(%E7%AE%80%E4%BD%93%E4%B8%AD%E6%96%87)  


20201213  
