# linux---重置密码

keywords: 重置root密码

在忘记密码的情况下，如何重置用户密码？  

1. 在启动时可以看到GRUB菜单，按"e"修改启动选项(如果启动速度太快，可以录像看看有没有这个界面)
2. 找到"linux"开头的行，只修改该行，把"ro"以及之后的内容都删掉，换成"rw init=/bin/bash"
3. Ctrl+x, 启动，进入root权限的shell
4. 重新挂载文件系统: mount -no remount,rw /
5. 修改root或其他用户的密码: passwd joe
6. 重启: reboot -f

这样就可以使用新的密码登陆了  


原链接: https://en.wikibooks.org/wiki/Linux_Guide/Reset_a_forgotten_root_password  


2024/10/26  
