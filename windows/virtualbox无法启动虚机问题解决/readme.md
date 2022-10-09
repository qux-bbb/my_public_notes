# virtualbox无法启动虚机问题解决

virtualbox用得好好的，有一天突然就打不开了，报错如下：  
```r
Error relaunching VirtualBox VM process:5
Command line:
'60eaff78-4bdd-042d-2e72-669728efd737-suplib-3rdchild --comment_ubuntu_64 --startvm 542c46f2-6ed8-4ead-83ff-257ee5f0d2cc --no-startvm-errormsgbox --sup-hardening-log=D:\virtualboxvm\ubuntu_64\Logs\VBoxHardening.log'
(rc=-104)
Please try reinstalling VirtualBox.
where:supR3HardenedWinReSpawn what:5
VERRINVALID_NAME(-104)-lnvalid(malformed)file/path name.
```

检查了一下最近安装的程序，把 `完美世界竞技平台` 卸载掉重启就好了。  

在网上搜了一下，也有卸载其它软件的，所以这个问题的解决办法就是把最近装的软件卸载掉重启试试。  


2022/10/9  
